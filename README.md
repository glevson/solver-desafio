
# Desafio Solver de Agendamento - Valorian

Solução para o desafio de otimização de agendamento de reuniões, desenvolvida com Python, Google OR-Tools e Streamlit.
Este projeto implementa um solver capaz de encontrar a melhor grade horária para um conjunto de reuniões, respeitando uma série de regras (restrições) e objetivos de otimização.

# 🎯 O Desafio
O objetivo principal é criar um planejador de reuniões a partir de um arquivo de dados (Excel), considerando as seguintes regras:

# Restrições Rígidas (Invioláveis)
Conflito de Sala: Duas reuniões não podem usar a mesma sala simultaneamente.

Conflito de Participante (Obrigatório): Uma pessoa não pode participar de duas reuniões obrigatórias ao mesmo tempo.

Capacidade da Sala: A sala deve comportar todos os participantes da reunião.

Período da Reunião: A reunião deve começar e terminar no mesmo dia.

# Restrições Flexíveis (Desejáveis)
O solver também busca otimizar a agenda com base em preferências, que são tratadas como objetivos a serem maximizados ou penalidades a serem minimizadas:
Conflito de Participante (Preferencial): Evitar que uma pessoa tenha conflito entre reuniões preferenciais ou entre uma preferencial e uma obrigatória.
Agendar o Mais Cedo Possível: Priorizar horários no início do dia.
Intervalo Mínimo: Garantir um intervalo entre reuniões de uma mesma pessoa.

## Minimizar Reuniões Paralelas:
Reduzir o número de reuniões ocorrendo ao mesmo tempo.
Estabilidade de Sala: Manter participantes na mesma sala para reuniões consecutivas.

# 🧠 Análise e Estratégia da Solução
O problema de agendamento com múltiplas restrições é um clássico problema de otimização combinatória, classificado como NP-Hard. Isso significa que encontrar a solução ótima por força bruta é computacionalmente inviável para datasets realistas.

## A estratégia adotada foi:
Modelagem como um Problema de Programação por Restrições (CP - Constraint Programming): Esta abordagem é ideal para problemas de alocação e agendamento, pois foca em encontrar soluções viáveis que satisfaçam um conjunto de regras complexas.

## Uso do Google OR-Tools:
Em vez de reinventar a roda, optei por usar o Google OR-Tools, um solver de otimização open-source, poderoso e maduro. Especificamente, foi utilizado o CP-SAT Solver, que é excelente para problemas com restrições lógicas e objetivos múltiplos.
Tratamento de Restrições:
Restrições Rígidas (Hard): Foram modeladas como regras absolutas. O solver não pode gerar uma solução que as viole.
## Restrições Flexíveis (Soft):
Foram incorporadas à função objetivo. O solver recebe uma "recompensa" por atender a uma preferência (ex: agendar cedo) e uma "penalidade" por violá-la (ex: não ter intervalo). O objetivo final é maximizar a soma total de recompensas.

## Pipeline de Dados Robusto: 
O script de leitura de dados foi projetado para ser resiliente a variações no arquivo Excel. Ele localiza as tabelas dinamicamente, independentemente de linhas em branco ou outras formatações, garantindo que o solver sempre receba os dados no formato correto.


# 🛠️ Stack e Estrutura do Projeto
Linguagem: Python 3.9+
Solver de Otimização: Google OR-Tools (CP-SAT)
Interface Web: Streamlit
## Manipulação de Dados: Pandas & OpenPyXL
## A estrutura do código foi dividida para separar as responsabilidades:
Generated code
solver-desafio/
├── 📂 dados/                  # Pasta com exemplos de arquivos de entrada
│   └── desafio_valorian.xlsx
├── 📜 app.py                   # Lógica da interface com o usuário (Streamlit)
├── 📜 solver.py                 # O "cérebro": modelagem e resolução do problema
└── 📜 requirements.txt          # Dependências do projeto
Use code with caution.

# 🚀 Como Executar a Aplicação
Siga os passos abaixo para rodar o projeto localmente.
1. Pré-requisitos
Ter o Python 3.9+ instalado.
Ter o Git instalado.
2. Clone o Repositório
Generated bash
git clone desafio-solver
cd solver-desafio
Use code with caution.
Bash
3. Crie e Ative um Ambiente Virtual (Recomendado)
Generated bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
4. Instale as Dependências
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
5. Execute a Aplicação
Generated bash
streamlit run app.py
Use code with caution.
Bash

Após executar o comando, uma aba será aberta no seu navegador com a aplicação rodando.


# 💻 Como Usar
Com a aplicação aberta no navegador, você verá uma área para upload.

Clique em "Procurar arquivos" e selecione um arquivo Excel formatado como o desafio_valorian.xlsx.
Após o upload, clique no botão "Otimizar Agenda".

O solver irá processar os dados e, se uma solução for encontrada, exibirá a grade de horários otimizada na tela.

