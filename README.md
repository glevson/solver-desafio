Pontos importantes que foram analisados para resolução do problema:

1- Conhecer os conceitos de problemas NP-complete/NP-hard.

1. Classe P (Tempo Polinomial)

A classe P contém todos os problemas que podem ser resolvidos rapidamente por um

computador.

O que significa "rapidamente"? Significa que o tempo necessário para encontrar a solução

cresce de forma "razoável" (polinomial) à medida que o problema aumenta de tamanho.

Exemplo: Ordenar uma lista de números. Se você dobrar o número de itens, o tempo para

ordenar não explode; ele aumenta de forma previsível e gerenciável. Encontrar o caminho

mais curto entre dois pontos em um mapa (usando o algoritmo de Dijkstra) também está em

P.

Em resumo: P = Problemas fáceis de resolver.

2. Classe NP (Tempo Polinomial Não Determinístico)

A classe NP contém problemas em que, embora possa ser difícil encontrar a solução, é fácil

verificar se uma suposta solução está correta.

A chave é a verificação: Se alguém lhe der uma possível resposta, você consegue checar

se ela é válida em tempo rápido (polinomial).

Analogia do Sudoku: Resolver um Sudoku difícil pode levar horas. Mas se eu lhe entregar

um Sudoku já preenchido, você consegue verificar se ele está correto (checando as linhas,

colunas e quadrados) em poucos minutos. Portanto, Sudoku está em NP.

Exemplo clássico: O Problema do Caixeiro-Viajante. Dado um conjunto de cidades, qual é o

caminho mais curto que visita cada cidade exatamente uma vez e retorna ao ponto de

partida? Encontrar esse caminho é extremamente difícil para muitas cidades. Mas se eu lhe

apresentar uma rota e disser "Esta é a mais curta, com 3.000 km", você pode facilmente

calcular o comprimento dessa rota específica para verificar se ela tem mesmo 3.000 km.

(Verificar se é a mais curta de todas ainda é o problema difícil).

Em resumo: NP = Problemas fáceis de verificar.

A grande questão da computação: Ninguém sabe se P = NP. Ou seja, será que os

problemas que são fáceis de verificar (NP) são também fáceis de resolver (P)? A maioria

dos cientistas acredita que não (P ≠ NP), mas isso nunca foi provado. Ganhar um prêmio de

1 milhão de dólares espera por quem provar.

2.Conhecer os conceitos de Objetivo e Restrições (Hard e Soft) no âmbito de planejamento.

Visão Geral

Imagine que você está usando um GPS para planejar uma viagem de carro.

O Objetivo: É o seu destino. Por exemplo, "chegar ao Cristo Redentor". Mais

especificamente, pode ser "chegar ao Cristo Redentor no menor tempo possível".


As Restrições: São as regras da estrada que você não pode (ou não quer) quebrar. Por

exemplo, "respeitar os limites de velocidade", "não dirigir na contramão" e "preferir não

pagar pedágio".

Agora, vamos aprofundar a definição de cada um.

1. O Objetivo (Objective)

O objetivo (ou função-objetivo) é a meta final que o plano busca alcançar. É aquilo que você

quer maximizar ou minimizar. Ele define o que é uma "boa" solução. Um bom objetivo é

sempre mensurável.

Função no Planejamento:

O objetivo é o critério usado para comparar duas soluções válidas e decidir qual é a melhor.

Se a Solução A atinge o objetivo melhor que a Solução B, então a Solução A é preferível.

Exemplos em diferentes contextos:

Logística: Minimizar o custo total de entrega.

Manufatura: Maximizar o número de produtos fabricados por hora.

Gerenciamento de Projetos: Entregar o projeto com o menor desvio possível do orçamento.

Marketing: Maximizar o retorno sobre o investimento (ROI) de uma campanha.

2. As Restrições (Constraints)

As restrições são as regras, condições ou limitações que o plano deve respeitar. Elas

definem o "espaço de soluções viáveis", ou seja, o que é um plano válido ou inválido.

É aqui que a distinção entre Hard e Soft se torna crucial.

a) Restrições Hard (Rígidas, Invioláveis ou Obrigatórias)

As restrições hard são absolutamente inegociáveis. A violação de uma única restrição hard

torna o plano inteiro inválido, impossível ou ilegal. Não há margem para flexibilidade.

Características:

São do tipo "deve" ou "não pode".

Se não forem satisfeitas, a solução não existe ou é inútil.

Representam leis da física, regulamentações legais, limitações de recursos ou regras

lógicas.

Exemplos:

Física: Um caminhão não pode carregar mais de 10 toneladas (sua capacidade máxima).

Legal: Um motorista de caminhão não pode dirigir por mais de 8 horas seguidas sem uma

pausa.

Lógica: Um professor não pode dar duas aulas em duas salas diferentes ao mesmo tempo.

Recurso: Um projeto deve ser concluído com a equipe de 5 pessoas que foi designada, pois

não há mais ninguém disponível.

b) Restrições Soft (Flexíveis, Desejáveis ou Preferenciais)

As restrições soft são desejos ou preferências. Violar uma restrição soft não invalida o

plano, mas o torna menos ideal ou de menor qualidade. Elas introduzem um "custo" ou

"penalidade" à solução.

Características:

São do tipo "deveria", "preferencialmente" ou "seria bom se".

São negociáveis; o planejador tentará satisfazê-las ao máximo, mas pode violá-las se for

necessário para encontrar uma solução (ou para otimizar melhor o objetivo principal).

Muitas vezes, são incorporadas à função-objetivo como uma penalidade. O objetivo passa a

ser, por exemplo, "minimizar o custo E minimizar a violação de restrições soft".

Exemplos:

Preferência: O motorista prefere não dirigir durante a noite. (Mas ele pode, se for a única

forma de cumprir o prazo).

Qualidade: As entregas deveriam ser feitas antes do meio-dia para aumentar a satisfação

do cliente. (Entregar à tarde não é o fim do mundo, mas é pior).

Custo: Evitar rotas com pedágio, a menos que a economia de tempo compense o custo

extra.

Conveniência: Seria bom que as reuniões de uma mesma equipe ocorressem no mesmo

dia para evitar que os funcionários venham ao escritório desnecessariamente.

Exemplo Prático: Planejamento da Grade Horária de uma Escola

Vamos amarrar todos os conceitos com um exemplo clássico:

Objetivo: Criar uma grade horária que minimize o número de "janelas" (horários vagos) para

os alunos e maximize a satisfação das preferências dos professores.

Restrições Hard (Invioláveis):

Um professor não pode estar em duas salas ao mesmo tempo.

Uma sala de aula não pode ser usada por duas turmas ao mesmo tempo.

Toda disciplina obrigatória deve ser alocada na grade.

A disciplina de Química deve ser alocada em um laboratório (e não em uma sala comum).

Restrições Soft (Desejáveis):

O professor Silva prefere não dar aulas às sextas-feiras.

Deveria-se evitar que os alunos do 1º ano tenham aulas no último horário.

Seria bom que as aulas de Matemática e Física não fossem no mesmo dia.

Tentar minimizar o deslocamento de professores entre prédios diferentes.

Um bom software de planejamento buscará uma solução que nunca viole as restrições hard

e, entre todas as soluções válidas, escolherá aquela que melhor atende ao objetivo (ou

seja, viola o mínimo possível de restrições soft e atinge a meta principal).

Tabela Resumo

Característica Objetivo Restrição Hard Restrição Soft

O que é? A meta a ser otimizada (maximizada ou minimizada). Uma regra

inegociável que deve ser cumprida. Uma preferência ou um desejo.

Função Define o que é uma solução "boa" ou "ótima". Define o que é uma

solução "válida" ou "possível". Contribui para a qualidade da solução.

Consequência da Violação A solução é menos ótima. A solução é inválida/impossível.

A solução é válida, mas menos desejável.

Exemplo de Frase "Minimizar o custo." "Não pode exceder 10 unidades."

"Preferencialmente antes do meio-dia."

3.Ser capaz de processar dados para criação de datasets.

Podemos dividir o processo em um fluxo de trabalho estruturado, muitas vezes chamado de

Pipeline de Dados. Aqui estão as etapas fundamentais, do início ao fim.

O Fluxo de Trabalho para Criação de Datasets

Imagine que você está preparando os ingredientes para uma receita de alta gastronomia.

Você não pode simplesmente jogar tudo na panela. É preciso selecionar, lavar, cortar e

preparar cada item com cuidado. O mesmo vale para os dados.

Definição -> Coleta -> Limpeza -> Transformação/Enriquecimento -> Estruturação ->

Validação/Documentação

Etapa 1: Definição do Objetivo e Escopo

Antes de escrever uma única linha de código, você precisa responder a perguntas cruciais:

Qual problema estou tentando resolver? (Ex: Prever o preço de imóveis em São Paulo).

Que tipo de dados eu preciso para resolver isso? (Ex: Área do imóvel, número de quartos,
bairro, idade do prédio). A variável que você quer prever (preço) é chamada de alvo (target),
e as informações usadas para prever são as features.
Qual é o escopo? (Ex: Apenas apartamentos? Apenas na cidade de São Paulo? Dados dos
últimos 2 anos?).
Resultado desta etapa: Um plano claro sobre quais dados coletar e por quê. Sem isso, você
corre o risco de coletar dados inúteis.
4.Ser capaz de usar algoritmos heurísticos para resolver problemas de planejamento
muilt-restrição e multi-objetivo.
algoritmos heurísticos para planejamento multi-restrição e multi-objetivo são métodos
avançados de otimização projetados para encontrar um conjunto de soluções de alta
qualidade e viáveis para problemas complexos e do mundo real, onde não há uma única
resposta "perfeita" e o tempo para decisão é limitado.
1. O Problema: Planejamento Multi-Restrição e Multi-Objetivo
Imagine um chef de cozinha de um restaurante de luxo que precisa planejar o menu da
semana. Ele enfrenta um problema complexo:
Planejamento: Ele precisa definir uma sequência de ações (comprar ingredientes, preparar
pratos, alocar cozinheiros).
Multi-Restrição: Ele tem muitas regras a seguir:
Restrições Hard (invioláveis): O orçamento semanal não pode passar de R$ 5.000. O peixe
só pode ser comprado na terça e na sexta. Cada cozinheiro só pode trabalhar 40 horas.
Restrições Soft (desejáveis): Preferencialmente, não repetir o mesmo tipo de carne em dias
seguidos. Evitar usar ingredientes que a crítica gastronômica da cidade não gosta.
Multi-Objetivo: Ele não tem uma única meta, mas várias, que muitas vezes entram em
conflito:
Objetivo 1: Minimizar o custo do menu.
Objetivo 2: Maximizar a satisfação do cliente (usando ingredientes de alta qualidade).
Objetivo 3: Minimizar o tempo de preparo dos pratos.
Perceba o conflito: usar ingredientes melhores (maximizar satisfação) geralmente aumenta
o custo (conflito com o Objetivo 1). Pratos mais rápidos (minimizar tempo) podem não ser
os mais saborosos (conflito com o Objetivo 2).
O desafio: Encontrar um "plano" (menu) que respeite todas as regras invioláveis (restrições
hard) e encontre o melhor equilíbrio possível entre os objetivos conflitantes, ao mesmo
tempo que tenta satisfazer as regras desejáveis (restrições soft).
Para problemas assim, encontrar a solução perfeita e ótima é computacionalmente inviável
(muitas vezes são problemas NP-Hard). O número de combinações possíveis explode
rapidamente. É aqui que entram os algoritmos heurísticos.
2. A Solução: Algoritmos Heurísticos
Um algoritmo heurístico é, em essência, um "atalho inteligente". Ele não garante encontrar a
melhor solução absoluta, mas é projetado para encontrar uma solução muito boa (ou "boa o
suficiente") em um tempo de execução razoável.
Eles funcionam explorando o "espaço de soluções" de maneira inteligente, em vez de testar
todas as possibilidades de forma exaustiva (força bruta).
Como os Algoritmos Heurísticos Lidão com Multi-Objetivo e Multi-Restrição?

Eles usam estratégias específicas para lidar com essa complexidade:

Para lidar com as Restrições:

Viabilidade Primeiro: Muitas heurísticas só trabalham com soluções que respeitam as

restrições hard. Se uma solução gerada viola uma regra inviolável, ela é imediatamente

descartada ou "consertada".

Funções de Penalidade: Para as restrições soft, a abordagem mais comum é adicionar uma

"penalidade" à avaliação da solução. A função-objetivo se torna algo como:

Qualidade da Solução = (Valor dos Objetivos) - (Soma das Penalidades por violar restrições

soft)

Dessa forma, o algoritmo é incentivado a evitar soluções que quebram as regras desejáveis.

Para lidar com os Multi-Objetivos:

Aqui está o grande truque. Como comparar uma solução que é mais barata mas menos

saborosa com outra que é mais cara mas deliciosa?

Conceito-Chave: A Fronteira de Pareto

Uma heurística multi-objetivo não busca uma única "melhor" solução, mas sim um conjunto

de soluções ótimas de compromisso, conhecido como Fronteira de Pareto (ou Pareto

Front).

Uma solução domina outra se ela for melhor em pelo menos um objetivo e não for pior em

nenhum dos outros.

A Fronteira de Pareto é o conjunto de todas as soluções não-dominadas. Nenhuma solução

na fronteira é estritamente melhor que outra em todos os sentidos. Elas representam

diferentes "trocas" (trade-offs) entre os objetivos.

Exemplo da Fronteira de Pareto para o Chef:

O algoritmo não retornaria "O melhor menu é este". Em vez disso, ele retornaria um

conjunto de opções:

Menu A: Custo baixíssimo, satisfação média.

Menu B: Custo médio, satisfação alta.

Menu C: Custo um pouco mais alto, satisfação altíssima.

Cabe ao tomador de decisão (o chef) escolher qual desses compromissos é o mais

adequado para o seu restaurante naquela semana.

Exemplos de Algoritmos Heurísticos (Meta-heurísticas)

Estes são alguns dos "atalhos inteligentes" mais famosos usados para esses problemas:

Algoritmos Genéticos (Genetic Algorithms - GA):

Como funciona: Inspirado na evolução de Darwin. Ele cria uma "população" de soluções

candidatas (diferentes menus) e as faz "evoluir" ao longo de gerações. As melhores

soluções (menor custo, maior satisfação) têm mais chances de "acasalar" (combinar suas

características) e gerar "filhos" (novos menus), que podem ser ainda melhores. Mutações

aleatórias introduzem novas ideias.

Multi-Objetivo: É excelente para encontrar a Fronteira de Pareto, pois mantém uma

população diversificada de soluções de compromisso. Algoritmos como NSGA-II são

especificamente projetados para isso.

Simulated Annealing (Recozimento Simulado):

Como funciona: Inspirado no processo de resfriamento de metais. Começa com uma

solução aleatória e a explora fazendo pequenas mudanças. No início ("quente"), aceita até

mesmo mudanças que pioram a solução, para evitar ficar preso em um "ótimo local" (uma

solução boa, mas não a melhor). Conforme o tempo passa ("esfria"), torna-se mais seletivo,

aceitando apenas melhorias.


Multi-Objetivo: Pode ser adaptado, mas é menos natural para encontrar uma fronteira inteira

do que os algoritmos genéticos.

Tabu Search (Busca Tabu):

Como funciona: É um algoritmo de busca local que possui "memória". Ele explora vizinhos

de uma solução atual, mas mantém uma "lista tabu" de movimentos recentes para evitar

andar em círculos e incentivar a exploração de novas áreas do espaço de busca.

Multi-Objetivo: Também pode ser adaptado, muitas vezes focando em um objetivo de cada

vez ou usando uma função de ponderação.

Resumo

Conceito O que é? Como a Heurística Lida?

Planejamento Encontrar uma sequência de ações para atingir metas. Explora de forma

inteligente as possíveis sequências de ações.

Multi-Restrição Múltiplas regras a seguir (obrigatórias e desejáveis). Descarta

soluções que violam regras hard; penaliza soluções que violam regras soft.

Multi-Objetivo Múltiplos objetivos conflitantes a serem otimizados. Não busca uma única

solução, mas um conjunto de bons compromissos (Fronteira de Pareto).

Heurística Um "atalho inteligente" para encontrar soluções muito boas em tempo

razoável. Usa inspirações (evolução, física, etc.) para guiar a busca por soluções de

alta qualidade.


# solver-desafio
Descrição do Problema - Solver Valorian

Criar um solver para planejar as reuniões para qualquer dataset no formato dos

fornecidos.

Restrições Rígidas (Hard Constraints):

• Conflito de sala: Duas reuniões não devem utilizar a mesma sala ao mesmo tempo.

• Participação obrigatória: Uma pessoa não pode ter duas reuniões obrigatórias ao mesmo

tempo.

• Capacidade mínima da sala: Uma reunião não pode ser alocada em uma sala que não

comporte todos os seus participantes.

• Início e término no mesmo dia: Uma reunião não deve ser agendada atravessando mais

de um dia.

Restrições Médias (Medium Constraints):

• Participação preferencial: Uma pessoa não pode ter duas reuniões preferenciais ao

mesmo tempo, nem uma reunião obrigatória e uma preferencial no mesmo horário.

Restrições Leves (Soft Constraints):

• Quanto antes, melhor: Agendar todas as reuniões o mais cedo possível.

• Intervalo entre reuniões: Duas reuniões devem ter pelo menos um intervalo de tempo

entre elas.

• Reuniões simultâneas: Minimizar o número de reuniões paralelas, para evitar que as

pessoas tenham que escolher entre uma ou outra.

• Alocar salas maiores primeiro: Se houver uma sala maior disponível, a reunião deve ser

alocada nela para acomodar o máximo possível de pessoas, mesmo que não estejam

formalmente inscritas.

• Estabilidade de sala: Se uma pessoa tiver duas reuniões consecutivas com até dois

intervalos de tempo entre elas, é preferível que ambas ocorram na mesma sala.

O solver pode usar qualquer framework e algoritmo. É preferível usar solvers

opensource e de mercado que implementar a o solver do zer



Solução aplicada ao problema usando Python e Streamlit.

Estrutura do Projeto
Para organizar o código, vamos dividi-lo em dois arquivos:

1. app.py: Contém toda a lógica da interface do Streamlit (upload de arquivo, botões,
exibição de resultados).
2. solver.py: Contém o "cérebro" da aplicação – o modelo de otimização que recebe
os dados e encontra a melhor grade horária.

Pré-requisitos
Antes de executar, você precisa instalar as bibliotecas necessárias. 

Crie um arquivo
requirements.txt com o seguinte conteúdo:

streamlit
pandas
openpyxl
google-ortools

1. Leitura de Aba Única: O código agora espera um arquivo com uma única aba chamada
Folha 1 (padrão do Excel).
2. Nova Função
○ Carregamento Bruto: A função primeiro carrega toda a planilha sem tentar
adivinhar cabeçalhos (header=None).
○ Encontra as "Âncoras": Ela varre a primeira coluna em busca dos
textos-chave: Reuniões devem acontecer em, Salas de Reunião e
Reuniões a Serem Agendadas. Isso permite que ela saiba em qual linha cada
seção de dados começa, não importando quantas linhas em branco existam
entre elas.
○ Extração Inteligente: Para cada âncora encontrada, ela usa uma função auxiliar
extract_table para "recortar" a tabela correta.

○ Fim Dinâmico da Tabela: A extração sabe que uma tabela termina quando
encontra uma linha em branco na segunda coluna (a primeira coluna de dados
reais), tornando o processo robusto a espaços extras.
○ Cabeçalhos Corretos: Os cabeçalhos de cada tabela são lidos da linha da
âncora, garantindo que os DataFrames sejam criados com os nomes de coluna
corretos.

○ Limpeza e Retorno: Ao final, a função retorna os três DataFrames limpos, no
formato exato que o solver.py precisa.
4.

5. Interface Atualizada: A mensagem no st.file_uploader foi atualizada para refletir o
novo formato de entrada.

6. Robustez: O código agora é muito mais resiliente a pequenas variações no layout do

Excel, como adicionar mais ou menos linhas em branco entre as seções.
Como Usar:

1. Salve o código Certifique-se de que o solver.py da solução anterior está na mesma
pasta.

2. Execute Pontos importantes que foram analisados para resolução do problema:

1- Conhecer os conceitos de problemas NP-complete/NP-hard.

1. Classe P (Tempo Polinomial)

A classe P contém todos os problemas que podem ser resolvidos rapidamente por um

computador.

O que significa "rapidamente"? Significa que o tempo necessário para encontrar a solução

cresce de forma "razoável" (polinomial) à medida que o problema aumenta de tamanho.

Exemplo: Ordenar uma lista de números. Se você dobrar o número de itens, o tempo para

ordenar não explode; ele aumenta de forma previsível e gerenciável. Encontrar o caminho

mais curto entre dois pontos em um mapa (usando o algoritmo de Dijkstra) também está em

P.

Em resumo: P = Problemas fáceis de resolver.

2. Classe NP (Tempo Polinomial Não Determinístico)

A classe NP contém problemas em que, embora possa ser difícil encontrar a solução, é fácil

verificar se uma suposta solução está correta.

A chave é a verificação: Se alguém lhe der uma possível resposta, você consegue checar

se ela é válida em tempo rápido (polinomial).

Analogia do Sudoku: Resolver um Sudoku difícil pode levar horas. Mas se eu lhe entregar

um Sudoku já preenchido, você consegue verificar se ele está correto (checando as linhas,

colunas e quadrados) em poucos minutos. Portanto, Sudoku está em NP.

Exemplo clássico: O Problema do Caixeiro-Viajante. Dado um conjunto de cidades, qual é o

caminho mais curto que visita cada cidade exatamente uma vez e retorna ao ponto de

partida? Encontrar esse caminho é extremamente difícil para muitas cidades. Mas se eu lhe

apresentar uma rota e disser "Esta é a mais curta, com 3.000 km", você pode facilmente

calcular o comprimento dessa rota específica para verificar se ela tem mesmo 3.000 km.

(Verificar se é a mais curta de todas ainda é o problema difícil).

Em resumo: NP = Problemas fáceis de verificar.

A grande questão da computação: Ninguém sabe se P = NP. Ou seja, será que os

problemas que são fáceis de verificar (NP) são também fáceis de resolver (P)? A maioria

dos cientistas acredita que não (P ≠ NP), mas isso nunca foi provado. Ganhar um prêmio de

1 milhão de dólares espera por quem provar.

2.Conhecer os conceitos de Objetivo e Restrições (Hard e Soft) no âmbito de planejamento.

Visão Geral

Imagine que você está usando um GPS para planejar uma viagem de carro.

O Objetivo: É o seu destino. Por exemplo, "chegar ao Cristo Redentor". Mais

especificamente, pode ser "chegar ao Cristo Redentor no menor tempo possível".


As Restrições: São as regras da estrada que você não pode (ou não quer) quebrar. Por

exemplo, "respeitar os limites de velocidade", "não dirigir na contramão" e "preferir não

pagar pedágio".

Agora, vamos aprofundar a definição de cada um.

1. O Objetivo (Objective)

O objetivo (ou função-objetivo) é a meta final que o plano busca alcançar. É aquilo que você

quer maximizar ou minimizar. Ele define o que é uma "boa" solução. Um bom objetivo é

sempre mensurável.

Função no Planejamento:

O objetivo é o critério usado para comparar duas soluções válidas e decidir qual é a melhor.

Se a Solução A atinge o objetivo melhor que a Solução B, então a Solução A é preferível.

Exemplos em diferentes contextos:

Logística: Minimizar o custo total de entrega.

Manufatura: Maximizar o número de produtos fabricados por hora.

Gerenciamento de Projetos: Entregar o projeto com o menor desvio possível do orçamento.

Marketing: Maximizar o retorno sobre o investimento (ROI) de uma campanha.

2. As Restrições (Constraints)

As restrições são as regras, condições ou limitações que o plano deve respeitar. Elas

definem o "espaço de soluções viáveis", ou seja, o que é um plano válido ou inválido.

É aqui que a distinção entre Hard e Soft se torna crucial.

a) Restrições Hard (Rígidas, Invioláveis ou Obrigatórias)

As restrições hard são absolutamente inegociáveis. A violação de uma única restrição hard

torna o plano inteiro inválido, impossível ou ilegal. Não há margem para flexibilidade.

Características:

São do tipo "deve" ou "não pode".

Se não forem satisfeitas, a solução não existe ou é inútil.

Representam leis da física, regulamentações legais, limitações de recursos ou regras

lógicas.

Exemplos:

Física: Um caminhão não pode carregar mais de 10 toneladas (sua capacidade máxima).

Legal: Um motorista de caminhão não pode dirigir por mais de 8 horas seguidas sem uma

pausa.

Lógica: Um professor não pode dar duas aulas em duas salas diferentes ao mesmo tempo.

Recurso: Um projeto deve ser concluído com a equipe de 5 pessoas que foi designada, pois

não há mais ninguém disponível.

b) Restrições Soft (Flexíveis, Desejáveis ou Preferenciais)

As restrições soft são desejos ou preferências. Violar uma restrição soft não invalida o

plano, mas o torna menos ideal ou de menor qualidade. Elas introduzem um "custo" ou

"penalidade" à solução.

Características:

São do tipo "deveria", "preferencialmente" ou "seria bom se".

São negociáveis; o planejador tentará satisfazê-las ao máximo, mas pode violá-las se for

necessário para encontrar uma solução (ou para otimizar melhor o objetivo principal).

Muitas vezes, são incorporadas à função-objetivo como uma penalidade. O objetivo passa a

ser, por exemplo, "minimizar o custo E minimizar a violação de restrições soft".

Exemplos:

Preferência: O motorista prefere não dirigir durante a noite. (Mas ele pode, se for a única

forma de cumprir o prazo).

Qualidade: As entregas deveriam ser feitas antes do meio-dia para aumentar a satisfação

do cliente. (Entregar à tarde não é o fim do mundo, mas é pior).

Custo: Evitar rotas com pedágio, a menos que a economia de tempo compense o custo

extra.

Conveniência: Seria bom que as reuniões de uma mesma equipe ocorressem no mesmo

dia para evitar que os funcionários venham ao escritório desnecessariamente.

Exemplo Prático: Planejamento da Grade Horária de uma Escola

Vamos amarrar todos os conceitos com um exemplo clássico:

Objetivo: Criar uma grade horária que minimize o número de "janelas" (horários vagos) para

os alunos e maximize a satisfação das preferências dos professores.

Restrições Hard (Invioláveis):

Um professor não pode estar em duas salas ao mesmo tempo.

Uma sala de aula não pode ser usada por duas turmas ao mesmo tempo.

Toda disciplina obrigatória deve ser alocada na grade.

A disciplina de Química deve ser alocada em um laboratório (e não em uma sala comum).

Restrições Soft (Desejáveis):

O professor Silva prefere não dar aulas às sextas-feiras.

Deveria-se evitar que os alunos do 1º ano tenham aulas no último horário.

Seria bom que as aulas de Matemática e Física não fossem no mesmo dia.

Tentar minimizar o deslocamento de professores entre prédios diferentes.

Um bom software de planejamento buscará uma solução que nunca viole as restrições hard

e, entre todas as soluções válidas, escolherá aquela que melhor atende ao objetivo (ou

seja, viola o mínimo possível de restrições soft e atinge a meta principal).

Tabela Resumo

Característica Objetivo Restrição Hard Restrição Soft

O que é? A meta a ser otimizada (maximizada ou minimizada). Uma regra

inegociável que deve ser cumprida. Uma preferência ou um desejo.

Função Define o que é uma solução "boa" ou "ótima". Define o que é uma

solução "válida" ou "possível". Contribui para a qualidade da solução.

Consequência da Violação A solução é menos ótima. A solução é inválida/impossível.

A solução é válida, mas menos desejável.

Exemplo de Frase "Minimizar o custo." "Não pode exceder 10 unidades."

"Preferencialmente antes do meio-dia."

3.Ser capaz de processar dados para criação de datasets.

Podemos dividir o processo em um fluxo de trabalho estruturado, muitas vezes chamado de

Pipeline de Dados. Aqui estão as etapas fundamentais, do início ao fim.

O Fluxo de Trabalho para Criação de Datasets

Imagine que você está preparando os ingredientes para uma receita de alta gastronomia.

Você não pode simplesmente jogar tudo na panela. É preciso selecionar, lavar, cortar e

preparar cada item com cuidado. O mesmo vale para os dados.

Definição -> Coleta -> Limpeza -> Transformação/Enriquecimento -> Estruturação ->

Validação/Documentação

Etapa 1: Definição do Objetivo e Escopo

Antes de escrever uma única linha de código, você precisa responder a perguntas cruciais:

Qual problema estou tentando resolver? (Ex: Prever o preço de imóveis em São Paulo).

Que tipo de dados eu preciso para resolver isso? (Ex: Área do imóvel, número de quartos,
bairro, idade do prédio). A variável que você quer prever (preço) é chamada de alvo (target),
e as informações usadas para prever são as features.
Qual é o escopo? (Ex: Apenas apartamentos? Apenas na cidade de São Paulo? Dados dos
últimos 2 anos?).
Resultado desta etapa: Um plano claro sobre quais dados coletar e por quê. Sem isso, você
corre o risco de coletar dados inúteis.
4.Ser capaz de usar algoritmos heurísticos para resolver problemas de planejamento
muilt-restrição e multi-objetivo.
algoritmos heurísticos para planejamento multi-restrição e multi-objetivo são métodos
avançados de otimização projetados para encontrar um conjunto de soluções de alta
qualidade e viáveis para problemas complexos e do mundo real, onde não há uma única
resposta "perfeita" e o tempo para decisão é limitado.
1. O Problema: Planejamento Multi-Restrição e Multi-Objetivo
Imagine um chef de cozinha de um restaurante de luxo que precisa planejar o menu da
semana. Ele enfrenta um problema complexo:
Planejamento: Ele precisa definir uma sequência de ações (comprar ingredientes, preparar
pratos, alocar cozinheiros).
Multi-Restrição: Ele tem muitas regras a seguir:
Restrições Hard (invioláveis): O orçamento semanal não pode passar de R$ 5.000. O peixe
só pode ser comprado na terça e na sexta. Cada cozinheiro só pode trabalhar 40 horas.
Restrições Soft (desejáveis): Preferencialmente, não repetir o mesmo tipo de carne em dias
seguidos. Evitar usar ingredientes que a crítica gastronômica da cidade não gosta.
Multi-Objetivo: Ele não tem uma única meta, mas várias, que muitas vezes entram em
conflito:
Objetivo 1: Minimizar o custo do menu.
Objetivo 2: Maximizar a satisfação do cliente (usando ingredientes de alta qualidade).
Objetivo 3: Minimizar o tempo de preparo dos pratos.
Perceba o conflito: usar ingredientes melhores (maximizar satisfação) geralmente aumenta
o custo (conflito com o Objetivo 1). Pratos mais rápidos (minimizar tempo) podem não ser
os mais saborosos (conflito com o Objetivo 2).
O desafio: Encontrar um "plano" (menu) que respeite todas as regras invioláveis (restrições
hard) e encontre o melhor equilíbrio possível entre os objetivos conflitantes, ao mesmo
tempo que tenta satisfazer as regras desejáveis (restrições soft).
Para problemas assim, encontrar a solução perfeita e ótima é computacionalmente inviável
(muitas vezes são problemas NP-Hard). O número de combinações possíveis explode
rapidamente. É aqui que entram os algoritmos heurísticos.
2. A Solução: Algoritmos Heurísticos
Um algoritmo heurístico é, em essência, um "atalho inteligente". Ele não garante encontrar a
melhor solução absoluta, mas é projetado para encontrar uma solução muito boa (ou "boa o
suficiente") em um tempo de execução razoável.
Eles funcionam explorando o "espaço de soluções" de maneira inteligente, em vez de testar
todas as possibilidades de forma exaustiva (força bruta).
Como os Algoritmos Heurísticos Lidão com Multi-Objetivo e Multi-Restrição?

Eles usam estratégias específicas para lidar com essa complexidade:

Para lidar com as Restrições:

Viabilidade Primeiro: Muitas heurísticas só trabalham com soluções que respeitam as

restrições hard. Se uma solução gerada viola uma regra inviolável, ela é imediatamente

descartada ou "consertada".

Funções de Penalidade: Para as restrições soft, a abordagem mais comum é adicionar uma

"penalidade" à avaliação da solução. A função-objetivo se torna algo como:

Qualidade da Solução = (Valor dos Objetivos) - (Soma das Penalidades por violar restrições

soft)

Dessa forma, o algoritmo é incentivado a evitar soluções que quebram as regras desejáveis.

Para lidar com os Multi-Objetivos:

Aqui está o grande truque. Como comparar uma solução que é mais barata mas menos

saborosa com outra que é mais cara mas deliciosa?

Conceito-Chave: A Fronteira de Pareto

Uma heurística multi-objetivo não busca uma única "melhor" solução, mas sim um conjunto

de soluções ótimas de compromisso, conhecido como Fronteira de Pareto (ou Pareto

Front).

Uma solução domina outra se ela for melhor em pelo menos um objetivo e não for pior em

nenhum dos outros.

A Fronteira de Pareto é o conjunto de todas as soluções não-dominadas. Nenhuma solução

na fronteira é estritamente melhor que outra em todos os sentidos. Elas representam

diferentes "trocas" (trade-offs) entre os objetivos.

Exemplo da Fronteira de Pareto para o Chef:

O algoritmo não retornaria "O melhor menu é este". Em vez disso, ele retornaria um

conjunto de opções:

Menu A: Custo baixíssimo, satisfação média.

Menu B: Custo médio, satisfação alta.

Menu C: Custo um pouco mais alto, satisfação altíssima.

Cabe ao tomador de decisão (o chef) escolher qual desses compromissos é o mais

adequado para o seu restaurante naquela semana.

Exemplos de Algoritmos Heurísticos (Meta-heurísticas)

Estes são alguns dos "atalhos inteligentes" mais famosos usados para esses problemas:

Algoritmos Genéticos (Genetic Algorithms - GA):

Como funciona: Inspirado na evolução de Darwin. Ele cria uma "população" de soluções

candidatas (diferentes menus) e as faz "evoluir" ao longo de gerações. As melhores

soluções (menor custo, maior satisfação) têm mais chances de "acasalar" (combinar suas

características) e gerar "filhos" (novos menus), que podem ser ainda melhores. Mutações

aleatórias introduzem novas ideias.

Multi-Objetivo: É excelente para encontrar a Fronteira de Pareto, pois mantém uma

população diversificada de soluções de compromisso. Algoritmos como NSGA-II são

especificamente projetados para isso.

Simulated Annealing (Recozimento Simulado):

Como funciona: Inspirado no processo de resfriamento de metais. Começa com uma

solução aleatória e a explora fazendo pequenas mudanças. No início ("quente"), aceita até

mesmo mudanças que pioram a solução, para evitar ficar preso em um "ótimo local" (uma

solução boa, mas não a melhor). Conforme o tempo passa ("esfria"), torna-se mais seletivo,

aceitando apenas melhorias.


Multi-Objetivo: Pode ser adaptado, mas é menos natural para encontrar uma fronteira inteira

do que os algoritmos genéticos.

Tabu Search (Busca Tabu):

Como funciona: É um algoritmo de busca local que possui "memória". Ele explora vizinhos

de uma solução atual, mas mantém uma "lista tabu" de movimentos recentes para evitar

andar em círculos e incentivar a exploração de novas áreas do espaço de busca.

Multi-Objetivo: Também pode ser adaptado, muitas vezes focando em um objetivo de cada

vez ou usando uma função de ponderação.

Resumo

Conceito O que é? Como a Heurística Lida?

Planejamento Encontrar uma sequência de ações para atingir metas. Explora de forma

inteligente as possíveis sequências de ações.

Multi-Restrição Múltiplas regras a seguir (obrigatórias e desejáveis). Descarta

soluções que violam regras hard; penaliza soluções que violam regras soft.

Multi-Objetivo Múltiplos objetivos conflitantes a serem otimizados. Não busca uma única

solução, mas um conjunto de bons compromissos (Fronteira de Pareto).

Heurística Um "atalho inteligente" para encontrar soluções muito boas em tempo

razoável. Usa inspirações (evolução, física, etc.) para guiar a busca por soluções de

alta qualidade.


# solver-desafio
Descrição do Problema - Solver Valorian

Criar um solver para planejar as reuniões para qualquer dataset no formato dos

fornecidos.

Restrições Rígidas (Hard Constraints):

• Conflito de sala: Duas reuniões não devem utilizar a mesma sala ao mesmo tempo.

• Participação obrigatória: Uma pessoa não pode ter duas reuniões obrigatórias ao mesmo

tempo.

• Capacidade mínima da sala: Uma reunião não pode ser alocada em uma sala que não

comporte todos os seus participantes.

• Início e término no mesmo dia: Uma reunião não deve ser agendada atravessando mais

de um dia.

Restrições Médias (Medium Constraints):

• Participação preferencial: Uma pessoa não pode ter duas reuniões preferenciais ao

mesmo tempo, nem uma reunião obrigatória e uma preferencial no mesmo horário.

Restrições Leves (Soft Constraints):

• Quanto antes, melhor: Agendar todas as reuniões o mais cedo possível.

• Intervalo entre reuniões: Duas reuniões devem ter pelo menos um intervalo de tempo

entre elas.

• Reuniões simultâneas: Minimizar o número de reuniões paralelas, para evitar que as

pessoas tenham que escolher entre uma ou outra.

• Alocar salas maiores primeiro: Se houver uma sala maior disponível, a reunião deve ser

alocada nela para acomodar o máximo possível de pessoas, mesmo que não estejam

formalmente inscritas.

• Estabilidade de sala: Se uma pessoa tiver duas reuniões consecutivas com até dois

intervalos de tempo entre elas, é preferível que ambas ocorram na mesma sala.

O solver pode usar qualquer framework e algoritmo. É preferível usar solvers

opensource e de mercado que implementar a o solver do zer



Solução aplicada ao problema usando Python e Streamlit.

Estrutura do Projeto
Para organizar o código, vamos dividi-lo em dois arquivos:

1. app.py: Contém toda a lógica da interface do Streamlit (upload de arquivo, botões,
exibição de resultados).
2. solver.py: Contém o "cérebro" da aplicação – o modelo de otimização que recebe
os dados e encontra a melhor grade horária.

Pré-requisitos
Antes de executar, você precisa instalar as bibliotecas necessárias. 

Crie um arquivo
requirements.txt com o seguinte conteúdo:

streamlit
pandas
openpyxl
google-ortools

1. Leitura de Aba Única: O código agora espera um arquivo com uma única aba chamada
Folha 1 (padrão do Excel).
2. Nova Função
○ Carregamento Bruto: A função primeiro carrega toda a planilha sem tentar
adivinhar cabeçalhos (header=None).
○ Encontra as "Âncoras": Ela varre a primeira coluna em busca dos
textos-chave: Reuniões devem acontecer em, Salas de Reunião e
Reuniões a Serem Agendadas. Isso permite que ela saiba em qual linha cada
seção de dados começa, não importando quantas linhas em branco existam
entre elas.
○ Extração Inteligente: Para cada âncora encontrada, ela usa uma função auxiliar
extract_table para "recortar" a tabela correta.

○ Fim Dinâmico da Tabela: A extração sabe que uma tabela termina quando
encontra uma linha em branco na segunda coluna (a primeira coluna de dados
reais), tornando o processo robusto a espaços extras.
○ Cabeçalhos Corretos: Os cabeçalhos de cada tabela são lidos da linha da
âncora, garantindo que os DataFrames sejam criados com os nomes de coluna
corretos.

○ Limpeza e Retorno: Ao final, a função retorna os três DataFrames limpos, no
formato exato que o solver.py precisa.
4.

5. Interface Atualizada: A mensagem no st.file_uploader foi atualizada para refletir o
novo formato de entrada.

6. Robustez: O código agora é muito mais resiliente a pequenas variações no layout do

Excel, como adicionar mais ou menos linhas em branco entre as seções.
Como Usar:

1. Salve o código Certifique-se de que o solver.py da solução anterior está na mesma
pasta.

2. Execute o comando no seu terminal (com o ambiente virtual ativado):
3. Generated bash
4. streamlit run app.py




o comando no seu terminal (com o ambiente virtual ativado):
3. Generated bash
4. streamlit run app.py




