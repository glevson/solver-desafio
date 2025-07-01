# solver.py

import pandas as pd
from ortools.sat.python import cp_model
import multiprocessing

def solve_meeting_scheduling(meetings_df, rooms_df, time_slots_df, weights, timeout_seconds):
    """
    Resolve o problema de agendamento de reuniões.
    Versão final com AddCumulative para máxima estabilidade e flexibilidade.
    """
    model = cp_model.CpModel()

    # --- 1. Pré-processamento ---
    meetings_df.reset_index(drop=True, inplace=True)
    rooms_df.reset_index(drop=True, inplace=True)
    meetings_df['duration_slots'] = (meetings_df['Duration'] / 15).astype(int)
    
    all_meetings = meetings_df['Topic'].tolist()
    all_rooms = rooms_df['Nome'].tolist()
    all_people = set()
    for _, row in meetings_df.iterrows():
        for col in ['Required attendance list', 'Preferred attendance list']:
            participants_str = str(row[col]).strip()
            if participants_str and participants_str.lower() != 'nan':
                 all_people.update([p.strip() for p in participants_str.split(',')])
    all_people = sorted(list(filter(None, all_people)))

    time_slots = []
    for _, row in time_slots_df.iterrows():
        day_str_raw = str(row['Reuniões devem acontecer em'])
        parts = day_str_raw.split()
        clean_day_str = ' '.join(parts[1:]) if len(parts) > 1 else day_str_raw
        for time_range in ['8:00-12:00', '13:00-18:00']:
            if not pd.isna(row[time_range]):
                start_time_str, end_time_str = row[time_range].split('-')
                try:
                    start_dt = pd.to_datetime(f"{clean_day_str} {start_time_str}", dayfirst=True)
                    end_dt = pd.to_datetime(f"{clean_day_str} {end_time_str}", dayfirst=True)
                    current = start_dt
                    while current < end_dt:
                        time_slots.append(current)
                        current += pd.Timedelta(minutes=15)
                except Exception as e:
                    print(f"Aviso: Não foi possível processar a data '{clean_day_str}'. Erro: {e}")
    if not time_slots: return None, "Erro crítico: Nenhum horário disponível foi processado.", []

    num_meetings = len(all_meetings)
    num_rooms = len(all_rooms)
    num_time_slots = len(time_slots)

    # --- 2. Variáveis de Decisão ---
    starts, ends, rooms, presences = {}, {}, {}, {}
    intervals = {}

    for m_idx in range(num_meetings):
        duration = meetings_df.at[m_idx, 'duration_slots']
        if duration <= 0: duration = 1
        name = meetings_df.at[m_idx, 'Topic'].replace(" ", "_")
        
        starts[m_idx] = model.NewIntVar(0, num_time_slots, f'start_{name}')
        ends[m_idx] = model.NewIntVar(0, num_time_slots, f'end_{name}')
        rooms[m_idx] = model.NewIntVar(0, num_rooms - 1, f'room_{name}')
        intervals[m_idx] = model.NewIntervalVar(starts[m_idx], duration, ends[m_idx], f'interval_{name}')
        
        for r_idx in range(num_rooms):
            presences[(m_idx, r_idx)] = model.NewBoolVar(f'presence_{name}_r{r_idx}')

    # --- 3. Restrições Rígidas (As que NUNCA podem ser quebradas) ---
    for m_idx in range(num_meetings):
        model.AddExactlyOne([presences[(m_idx, r_idx)] for r_idx in range(num_rooms)])
        for r_idx in range(num_rooms):
            model.Add(rooms[m_idx] == r_idx).OnlyEnforceIf(presences[(m_idx, r_idx)])

    for r_idx in range(num_rooms):
        room_intervals = []
        for m_idx in range(num_meetings):
            duration = meetings_df.at[m_idx, 'duration_slots']
            if duration <= 0: duration = 1
            room_intervals.append(model.NewOptionalIntervalVar(
                starts[m_idx], duration, ends[m_idx], presences[(m_idx, r_idx)], f'opt_interval_m{m_idx}_r{r_idx}'
            ))
        model.AddNoOverlap(room_intervals)

    for m_idx in range(num_meetings):
        req_list_str = str(meetings_df.at[m_idx, 'Required attendance list'])
        required_attendees = len([p.strip() for p in req_list_str.split(',') if p.strip()])
        if required_attendees == 0: required_attendees = 1
        for r_idx in range(num_rooms):
            if rooms_df.at[r_idx, 'Capacidade'] < required_attendees:
                model.Add(presences[(m_idx, r_idx)] == 0)

    # --- 4. Restrições Flexíveis (com Penalidades) ---
    penalties = []
    
    # >>> CONFLITO DE PESSOAS COM AddCumulative FLEXÍVEL <<<
    person_capacities = {}
    for person_name in all_people:
        person_intervals = []
        for m_idx in range(num_meetings):
            req_list = [p.strip() for p in str(meetings_df.at[m_idx, 'Required attendance list']).split(',') if p.strip()]
            pref_list = [p.strip() for p in str(meetings_df.at[m_idx, 'Preferred attendance list']).split(',') if p.strip()]
            if person_name in req_list or person_name in pref_list:
                person_intervals.append(intervals[m_idx])
        
        if len(person_intervals) > 1:
            # A capacidade da pessoa é uma variável. Queremos que seja 1.
            # O limite superior (10) é arbitrário, apenas para dar folga.
            capacity = model.NewIntVar(1, 10, f'capacity_{person_name.replace(" ", "_")}')
            model.AddCumulative(person_intervals, [1] * len(person_intervals), capacity)
            person_capacities[person_name] = capacity
            
            # Adiciona uma penalidade enorme por usar mais capacidade que 1
            penalties.append((capacity - 1) * weights['person_conflict'])

    # S1: Quanto antes, melhor
    for m_idx in range(num_meetings):
        penalties.append(starts[m_idx] * weights['early_as_possible'])

    # S4: Bom encaixe da sala
    for m_idx in range(num_meetings):
        req_list_str = str(meetings_df.at[m_idx, 'Required attendance list'])
        required_attendees = len([p.strip() for p in req_list_str.split(',') if p.strip()])
        if required_attendees == 0: required_attendees = 1
        for r_idx in range(num_rooms):
            idle_capacity = rooms_df.at[r_idx, 'Capacidade'] - required_attendees
            penalties.append(presences[(m_idx, r_idx)] * idle_capacity * weights['room_fit'])

    # --- 5. Objetivo e Solução ---
    model.Minimize(sum(penalties))
    
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(timeout_seconds)
    solver.parameters.num_search_workers = multiprocessing.cpu_count()
    solver.parameters.log_search_progress = True
    status = solver.Solve(model)

    # --- 6. Pós-processamento ---
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # Verifica quais pessoas tiveram conflitos
        violated_constraints = []
        for person_name, capacity_var in person_capacities.items():
            if solver.Value(capacity_var) > 1:
                violated_constraints.append(
                    f"Conflito de Horário para '{person_name}' (agendado em {solver.Value(capacity_var)} reuniões simultâneas)."
                )

        status_message = f"Solução Viável/Ótima encontrada em {solver.WallTime():.2f} segundos."
        if violated_constraints:
            status_message += " **AVISO: Alguns conflitos de pessoas foram permitidos para viabilizar a agenda.**"

        output_schedule = []
        for m_idx in range(num_meetings):
            start_slot_idx = solver.Value(starts[m_idx])
            room_idx = solver.Value(rooms[m_idx])
            start_time = time_slots[start_slot_idx]
            duration_minutes = int(meetings_df.at[m_idx, 'Duration'])
            end_time = start_time + pd.Timedelta(minutes=duration_minutes)
            
            output_schedule.append({
                'Tópico': meetings_df.at[m_idx, 'Topic'],
                'Sala': all_rooms[room_idx],
                'Início': start_time.strftime('%H:%M'),
                'Fim': end_time.strftime('%H:%M'),
                'Dia': start_time.strftime('%Y-%m-%d (%A)'),
                'Participantes Obrigatórios': meetings_df.at[m_idx, 'Required attendance list']
            })
            
        return pd.DataFrame(output_schedule), status_message, violated_constraints
    elif status == cp_model.INFEASIBLE:
         return None, "Problema INVIÁVEL: É impossível satisfazer as restrições mais rígidas (conflito de sala, capacidade). Verifique os dados de entrada.", []
    else:
        return None, f"Não foi possível encontrar uma solução. Status do Solver: {solver.StatusName(status)}", []