# app.py

import streamlit as st
import pandas as pd
from solver import solve_meeting_scheduling
import plotly.express as px

# (A função parse_single_sheet_data permanece a mesma)
def parse_single_sheet_data(uploaded_file):
    try:
        df_raw = pd.read_excel(uploaded_file, sheet_name='Folha 1', header=None)
        header_rows = {}
        for idx, row in df_raw.iterrows():
            cell_value = str(row.iloc[0])
            if 'Reuniões devem acontecer em' in cell_value:
                header_rows['time_slots'] = idx
            elif 'Salas de Reunião' in cell_value:
                header_rows['rooms'] = idx
            elif 'Reuniões a Serem Agendadas' in cell_value:
                header_rows['meetings'] = idx

        if len(header_rows) < 3:
            raise ValueError("Não foi possível encontrar todos os cabeçalhos necessários.")

        def extract_table(start_row, num_cols):
            end_row = start_row + 1
            # A tabela termina quando encontra uma linha totalmente vazia
            while end_row < len(df_raw) and not df_raw.iloc[end_row].isnull().all():
                end_row += 1
            
            headers_raw = df_raw.iloc[start_row].tolist()
            # Pega cabeçalhos a partir da segunda coluna
            headers = [h for h in headers_raw[1:1+num_cols] if pd.notna(h)]

            data = df_raw.iloc[start_row + 1:end_row, 1:1+len(headers)].copy()
            data.columns = headers
            return data.dropna(how='all')

        time_slots_df = extract_table(header_rows['time_slots'], 3)
        time_slots_df.columns = ['Reuniões devem acontecer em', '8:00-12:00', '13:00-18:00']
        rooms_df = extract_table(header_rows['rooms'], 2)
        meetings_df = extract_table(header_rows['meetings'], 8)
        
        meetings_df.dropna(subset=['Topic'], inplace=True)
        rooms_df.dropna(subset=['Nome'], inplace=True)
        time_slots_df.dropna(subset=['Reuniões devem acontecer em'], inplace=True)
        
        if 'Preferred attendance list' not in meetings_df.columns:
            meetings_df['Preferred attendance list'] = ''
        meetings_df['Preferred attendance list'] = meetings_df['Preferred attendance list'].fillna('')

        return meetings_df, rooms_df, time_slots_df
    except Exception as e:
        st.error(f"Erro ao processar o arquivo Excel: {e}")
        return None, None, None


st.set_page_config(layout="wide")
st.title("📅 Planejador de Reuniões Flexível")
st.markdown("Este solver tentará encontrar a melhor solução, mesmo que precise violar algumas regras de conflito de horário.")

st.header("1. Carregue seu arquivo de planejamento (.xlsx)")
uploaded_file = st.file_uploader("Selecione o arquivo Excel com os dados na 'Folha 1'", type="xlsx")

if uploaded_file:
    meetings_df, rooms_df, time_slots_df = parse_single_sheet_data(uploaded_file)

    if meetings_df is not None:
        st.success(f"Arquivo carregado com sucesso! {len(meetings_df)} reuniões a agendar.")

        with st.expander("Visualizar Dados Interpretados"):
            st.subheader("Reuniões a Agendar")
            st.dataframe(meetings_df)
        
        st.header("2. Ajuste as prioridades e o tempo de busca")
        col1, col2, col3 = st.columns(3)
        weights = {}
        with col1:
            weights['person_conflict'] = st.number_input(
                "Penalidade por Conflito de Pessoa", 
                min_value=100, max_value=10000, value=1000, step=100,
                help="Custo altíssimo para forçar uma pessoa a estar em duas reuniões. Aumente se ainda houver muitos conflitos."
            )
        with col2:
            weights['early_as_possible'] = st.slider("Peso para Agendar Cedo", 0, 10, 1)
        with col3:
            weights['room_fit'] = st.slider("Peso para 'Bom Encaixe' da Sala", 0, 10, 2)
        
        timeout_seconds = st.number_input(
            "Tempo limite do solver (segundos)", 
            min_value=30, max_value=600, value=120, step=30,
            help="Para problemas grandes, aumente o tempo para 180s ou mais."
        )
        
        st.header("3. Gere o Planejamento")
        if st.button("🚀 Planejar Reuniões"):
            spinner_message = f"Otimizando a grade horária... Isso pode levar até {timeout_seconds} segundos..."
            with st.spinner(spinner_message):
                schedule_df, status_message, violated_constraints = solve_meeting_scheduling(
                    meetings_df, rooms_df, time_slots_df, weights, timeout_seconds
                )
            
            st.info(f"**Status do Solver:** {status_message}")

            if violated_constraints:
                st.warning("Relatório de Conflitos:")
                for violation in violated_constraints:
                    st.write(f"- {violation}")

            if schedule_df is not None:
                st.balloons()
                st.subheader("✅ Grade Horária Otimizada")
                
                schedule_df_sorted = schedule_df.sort_values(by=['Dia', 'Início', 'Sala']).reset_index(drop=True)
                st.dataframe(schedule_df_sorted)
                
                @st.cache_data
                def convert_df_to_csv(df):
                    return df.to_csv(index=False).encode('utf-8')

                csv = convert_df_to_csv(schedule_df_sorted)
                st.download_button("📥 Baixar Grade em CSV", csv, 'grade_horaria_otimizada.csv', 'text/csv')
                
                st.subheader("📊 Visualização da Alocação (Gráfico de Gantt)")
                
                # >>> INÍCIO DA CORREÇÃO <<<
                # A lógica de destacar conflitos foi removida, pois a nova mensagem de violação é diferente.
                # O gráfico agora mostra a alocação padrão, que ainda é muito útil.
                plot_df = schedule_df_sorted.copy()
                plot_df['Início Completo'] = pd.to_datetime(plot_df['Dia'].str.extract(r'(\d{4}-\d{2}-\d{2})')[0] + ' ' + plot_df['Início'])
                plot_df['Fim Completo'] = pd.to_datetime(plot_df['Dia'].str.extract(r'(\d{4}-\d{2}-\d{2})')[0] + ' ' + plot_df['Fim'])

                fig = px.timeline(
                    plot_df, 
                    x_start="Início Completo", 
                    x_end="Fim Completo", 
                    y="Sala", 
                    color="Tópico", # Volta a colorir pelo tópico da reunião
                    hover_name="Tópico",
                    title="Alocação de Reuniões por Sala e Horário"
                )
                fig.update_yaxes(categoryorder="total ascending")
                fig.update_layout(xaxis_title="Data e Hora", yaxis_title="Sala de Reunião")
                st.plotly_chart(fig, use_container_width=True)
                # >>> FIM DA CORREÇÃO <<<

else:
    st.info("Aguardando o upload de um arquivo .xlsx para começar.")