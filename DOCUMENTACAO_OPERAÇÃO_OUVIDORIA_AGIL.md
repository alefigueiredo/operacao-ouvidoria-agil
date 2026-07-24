# 📖 Manual Completo & Documentação de Arquitetura
## Operação Ouvidoria Ágil — O Caos da Tempestade Municipal

> **Plataforma Interativa de Capacitação em Inteligência Artificial Generativa e Automação de Processos para o Setor Público.**

---

## 🎯 1. Visão Geral do Projeto

A **Operação Ouvidoria Ágil** é uma aplicação web completa desenvolvida em **Python** e **Streamlit**, desenhada para capacitar servidores públicos, ouvidores e profissionais de tecnologia na aplicação prática de **Inteligência Artificial Generativa (LLMs)**, **Engenharia de Prompts**, **Automação No-Code (n8n)** e **Programação Python Aplicada**.

A aplicação combina **metodologia gamificada** baseada em um mapa de progressão (estilo *Super Mario Bros*), simulado de crise municipal em tempo real (*A Tempestade do Município de Nova Esperança*) e **mecanismos rigorosos de validação técnica e anti-cola**.

---

## 🏗️ 2. Arquitetura do Sistema & Estrutura de Arquivos

```
C:\Operação Ouvidoria Ágil\
├── operacao_ouvidoria_agil_app.py   # Aplicação Principal e Roteador de Navegação
├── utils.py                         # Motor de Validação, Criptografia SHA-256 e Utilitários
├── requirements.txt                 # Dependências do Projeto para Deploy na Nuvem
├── .gitignore                       # Filtro de Arquivos Rastreados pelo Git
├── operacao_ouvidoria_agil_logo.jpg # Identidade Visual (Logo Oficial)
├── operacao_ouvidoria_agil_mascote.jpg# Mascote Ágil-Bot
├── acessos_participantes.csv        # Log Automático de Acessos dos Alunos (CSV)
│
├── app_pages/                       # Páginas das 10 Fases de Aprendizado
│   ├── 0A_🧠_Fase_0A_Fundamentos.py # Quiz 6 Estudos de Caso de GenAI & LGPD
│   ├── 0B_✍️_Fase_0B_Prompting.py   # Engenharia de Prompts RTF/CRISP
│   ├── 0C_🐍_Fase_0C_Estruturas.py  # Fichas Digitais e Filtros em Python
│   ├── 0D_🔀_Fase_0D_Fluxograma.py  # Construtor Visual de Pipeline de 7 Nós
│   ├── 0E_⚡_Fase_0E_n8n.py         # Simulador de Automação n8n (5 Nós)
│   ├── 0F_🤖_Fase_0F_Agentes.py     # Arquitetura de Agentes e 2 Skills Modulares
│   ├── 1_📂_Fase_1_Parsing.py       # Extração Semântica e JSON Estruturado
│   ├── 2_⚡_Fase_2_Automacao.py     # Sandbox Python & 20 Casos de Estresse
│   ├── 3_🛡️_Fase_3_RedTeaming.py    # Arena Hacker contra Prompt Injection
│   ├── 4_📊_Fase_4_Relatorio.py     # Relatório Executivo e Trava por Matrícula
│   └── 5_🏆_Certificado_Final.py    # Emissão de Certificado com SHA-256
│
└── progresso_alunos/                # Armazenamento JSON de Progresso Individual
    └── progresso_{hash_email}.json  # Estado do Aluno (Carregamento Automático)
```

---

## 🎮 3. Detalhamento das 10 Fases de Aprendizado

### 🧠 Fase 0A: Fundamentos & Ética Pública
- **Objetivo:** Garantir alinhamento teórico sobre IA Generativa x Discriminativa e governança no setor público.
- **Validação:** Quiz interativo contendo **6 Questões de Estudo de Caso** (LGPD no envio de dados à nuvem, prevenção contra alucinações via *Human-in-the-Loop*, viés no RH e parâmetros de criatividade).
- **Código Gerado:** `NÍVEL-0A-{SHA256}`.

### ✍️ Fase 0B: Engenharia de Prompts Estruturada (RTF/CRISP)
- **Objetivo:** Ensinar a construção de prompts corporativos de alta fidelidade.
- **Validação (7 Trava Rígidas):**
  1. Mínimo de **250 caracteres**.
  2. Persona operacional explicita (*"Aja como..."*).
  3. Tarefa delimitada (*"Resuma..."*).
  4. Formato de saída definido (*Markdown, tabela...*).
  5. Delimitadores isolando o texto (`###` ou `---`).
  6. Configuração de Parâmetros declarada (`[Temperatura: 0.2]`).
  7. Variáveis dinâmicas (`{{bairro}}`, `{{protocolo}}`) e Restrições Negativas (*"NUNCA..."*).

### 🐍 Fase 0C: Fichas Digitais e Filtros em Python
- **Objetivo:** Capacitar no manuseio de estruturas de dados fundamentais (`dict` e `list`).
- **Validação:** Criação de lista de dicionários Python e escrita obrigatória de uma **função de filtragem ou List Comprehension** para isolar chamados de emergência (`[f for f in fichas if f['urgencia'] == 'ALTA']`).

### 🔀 Fase 0D: Fluxogramas & Orquestração de Agentes
- **Objetivo:** Ensinar a lógica de pipeline por trás de agentes de IA.
- **Validação:** Sequenciamento correto de **7 Nós de Automação Visual**:
  `Entrada ➔ Mascaramento LGPD ➔ Classificador LLM ➔ Roteador Condicional ➔ Alerta Emergencial ➔ Registro Ouvidoria ➔ Escalação Humana`.

### ⚡ Fase 0E: Simulador No-Code no n8n
- **Objetivo:** Simular pipelines de integração entre formulários, IA e planilhas.
- **Validação:** Configuração precisa de **5 Nós de Automação Visual**:
  `Webhook POST /ouvidoria ➔ Privacy Anonymizer LGPD ➔ Gemini 2.5 Categorization ➔ Google Sheets ➔ Gmail Alerta`.

### 🤖 Fase 0F: Arquitetura de Agentes & Skills Modulares
- **Objetivo:** Ensinar o padrão de Skills em arquivos `SKILL.md` com cabeçalho YAML.
- **Validação:** Criação do manifesto do Agente configurado com **2 Skills Modulares distintas**:
  - `triagem-emergencia-municipal` (Skill de Crise Climática)
  - `atendimento-cidadao-padrao` (Skill de Rotina da Ouvidoria)

### 📂 Fase 1: Parsing Semântico & Validação de JSON
- **Objetivo:** Converter relatórios desestruturados de cidadãos em JSON padronizado.
- **Validação:** Verificação de 9 chaves obrigatórias e validação do `checksum_matricula` dinâmico do aluno.

### ⚡ Fase 2: Sandbox Python & Triagem em Lote
- **Objetivo:** Escrever a função `triar_chamado(item)` para automatizar a classificação de chamados.
- **Validação:** Execução em ambiente de testes isolado contra **20 chamados reais de estresse** (testando casos de borda, semáforos, árvores sobre fiação e contaminações).

### 🛡️ Fase 3: Red Teaming & Arena de Batalha Hacker
- **Objetivo:** Blindar o System Prompt da IA contra ataques de *Prompt Injection* e *Jailbreaks*.
- **Validação:** Batalha interativa em **6 Rodadas** contra ataques de desvio de persona, engenharia social e injeção indireta, exigindo aprovação em testes de falso positivo.

### 📊 Fase 4: Gabinete Executivo & Relatório Estratégico
- **Objetivo:** Sintetizar os dados da crise em um relatório executivo para o Prefeito.
- **Validação Anti-Cola:**
  - **Trava por E-mail:** O validador checa se os bairros citados no relatório coincidem exatamente com os chamados sorteados para a matrícula do aluno (impede colar textos prontos de IA).
  - **Cálculo Orçamentário:** Exigência de cálculo de estimativa financeira de contingência.
  - **Embasamento Jurídico:** Citação obrigatória do *Decreto Municipal de Calamidade nº 4.820/2026*.

### 🏆 Certificado Final
- Emissão automatizada do certificado contendo o nome do servidor, carga horária e hash SHA-256 para verificação de autenticidade.

---

## 🔒 4. Mecanismos de Segurança e Anti-Cola

1. **Validação SHA-256 por E-mail:**
   Cada aluno possui uma semente única gerada a partir do seu endereço de E-mail (`matricula`). Os códigos de desbloqueio de fase (`gerar_codigo_zero_X`) são calculados dinamicamente via Hash SHA-256, impedindo que os alunos compartilhem senhas genéricas.

2. **Cronômetro de Apoio com JavaScript (Ao Vivo):**
   - Fases de Nivelamento (0A-0F): **30 minutos**.
   - Fases de Crise (1-4): **60 minutos**.
   - A *Dica de Ouro do Ágil-Bot* fica estritamente bloqueada até que o tempo expire. Caso o aluno utilize a dica, o sistema aplica uma penalidade, registrando **75% do XP total**.

3. **Trava Anti-Cola de IA na Fase 4:**
   Impede que o participante apenas copie a tela e cole em ferramentas externas de IA, exigindo dados estritamente alinhados com o e-mail cadastrado.

---

## 📊 5. Gestão de Alunos & Painel do Instrutor

### 📥 Exportação de Log de Acessos (CSV)
- O aplicativo grava silenciosamente todas as interações no arquivo `acessos_participantes.csv`.
- **Como Acessar:** Na barra lateral do app, acesse a aba **`📊 Painel do Instrutor (Baixar Acessos)`**, digite a senha secreta **`admin2026`** e clique em **`📥 Baixar Relatório de Participantes (CSV)`**.

### 🔄 Botão de Reset para Testes
- Disponível na barra lateral e na página inicial para permitir que o instrutor limpe o progresso do seu e-mail e teste a experiência dos bloqueios do zero.

---

## ☁️ 6. Publicação e Deploy (Streamlit Community Cloud)

O projeto está configurado para deploy automático integrado ao GitHub:

- **Repositório:** `https://github.com/alefigueiredo/operacao-ouvidoria-agil.git`
- **Branch Principal:** `main`
- **Arquivo Principal (Main File):** `operacao_ouvidoria_agil_app.py`
- **Atualização:** Qualquer alteração enviada para o GitHub via `git push origin main` recompila a aplicação na nuvem em tempo real!

---

*Documentação gerada para a Operação Ouvidoria Ágil.* 🚀
