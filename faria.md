# Relatório Técnico Final: Simulação de Clínica Médica
**Projeto Laboratorial - Engenharia Biomédica (2º Ano)** **Unidade Curricular:** Algoritmos e Técnicas de Programação  
**Instituição:** Universidade do Minho / Escola de Engenharia  
**Coordenação:** José Carlos Ramalho e Luís Filipe Cunha  
**Data de Execução:** Novembro de 2025 - Janeiro de 2026

---

## 1. Introdução
Este projeto visa a modelação computacional e simulação de um ambiente clínico real, utilizando a metodologia de Simulação de Eventos Discretos (DES). O sistema desenvolvido permite estudar o comportamento de filas de espera, a ocupação de recursos médicos e a satisfação dos utentes sob diferentes condições de pressão (taxas de chegada). A solução integra um motor de simulação estocástico, uma interface gráfica interativa e um módulo de análise de dados.

---

## 2. Objetivos do Projeto
O principal objetivo foi a construção de uma ferramenta capaz de simular o fluxo de atendimento de doentes, cumprindo os seguintes requisitos pedagógicos e técnicos:
* **Modelação Estocástica:** Implementação de chegadas segundo uma distribuição de Poisson e tempos de serviço variáveis (Exponencial, Normal, Uniforme).
* **Gestão de Recursos:** Monitorização de filas de espera e ocupação de médicos.
* **Análise de Sensibilidade:** Capacidade de testar "cenários 10-30" (variação da taxa de chegada) para observar o comportamento exponencial da fila.
* **Visualização de Dados:** Geração de gráficos evolutivos e estatísticos para suporte à decisão.

---

## 3. Arquitetura do Sistema
A aplicação foi estruturada de forma modular para garantir a separação entre a lógica de negócio, a interface e a visualização.

### 3.1. Módulo de Simulação (clinic.py)
Este é o "motor" do sistema. A função simula gere o relógio da simulação e a lista de eventos (Queue de Eventos).
* **Lógica de Prioridade (Protocolo de Manchester Adaptado):**
Ao contrário de uma fila FIFO (First-In, First-Out) simples, o sistema implementa uma fila prioritária baseada na gravidade clínica. A gravidade é atribuída probabilisticamente:
    * **Vermelha (Emergência):** Prioridade 0. Atribuída se a frequência cardíaca (simulada) for <50 ou >100, ou através de uma combinação de testes booleanos aleatórios.
    * **Laranja (Muito Urgente):** Prioridade 1.
    * **Amarela (Urgente):** Prioridade 2.
    * **Verde (Pouco Urgente):** Prioridade 3.  
    *Implementação:* A fila é reordenada dinamicamente `fila.sort(key=lambda x: (x['prioridade'], x['tempo']))` sempre que um novo doente entra, garantindo que casos graves passem à frente.

* **Fatores de Envelhecimento:**
Foi introduzida uma regra de negócio específica onde doentes idosos (> 65 anos) requerem, em média, 20% mais tempo de consulta. Isto adiciona realismo ao modelo, impactando a ocupação dos médicos quando a demografia dos doentes é mais envelhecida.

* **Estrutura de Dados dos Doentes:**
Os doentes não são apenas números. O sistema carrega um dataset real (`pessoas (1).json`), permitindo associar nomes, idades e géneros aos eventos, o que enriquece a análise demográfica posterior.

### 3.2. Interface Gráfica (gui_app.py)
Desenvolvida com FreeSimpleGUI, a interface permite a configuração em tempo real sem necessidade de alterar o código fonte.
* **Funcionalidades de Controlo:**
    * Configuração de parâmetros: Nº de Médicos, Taxa de Chegada, Tempo Médio de Consulta e Duração da Simulação.
    * Seleção de Distribuição Estatística: Exponencial, Normal ou Uniforme.
    * Modo Escuro/Claro: O utilizador pode alternar o tema visual da aplicação dinamicamente.
* **Feedback Imediato:** Um painel de relatório apresenta, após a execução, os KPIs (Key Performance Indicators) principais: média de idades, distribuição de sexos e contagem por cor de triagem.

### 3.3. Módulo de Visualização (plots.py)
Utiliza a biblioteca matplotlib para gerar quatro tipos de visualizações essenciais:
* **Evolução da Fila:** Um gráfico de linha preenchido que mostra os picos de afluência ao longo do tempo.
* **Ocupação Médica:** Gráfico degrau (step plot) que visualiza a percentagem de médicos ocupados a cada minuto.
* **Correlação Taxa/Fila:** Executa múltiplas simulações em background variando a taxa de chegada de 10 a 30, demonstrando o ponto de rutura do sistema.
* **Distribuição Demográfica e Clínica:** Gráficos de barras para faixas etárias e gráficos circulares (pie charts) para as cores de Manchester.

---

## 4. Manual de Utilização e Parâmetros

### 4.1

<img width="922" height="470" alt="Captura de ecrã 2026-01-13 152633" src="https://github.com/user-attachments/assets/154c8a0e-2df3-465a-9ff8-3793189ad13d" />

Projeto realizado por: Afonso Faria (a111747), Duarte Matos (a110102), Simão Ribeiro (a111844).
