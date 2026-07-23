import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0F: Criador de Agentes & Skills - Ouvidoria Ágil", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #4ADE80; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
    .concept-box {
        background-color: #0F172A;
        border-left: 5px solid #A855F7;
        border-radius: 8px;
        padding: 15px;
        color: #E2E8F0;
        margin-bottom: 20px;
    }
    .skill-code-box {
        background-color: #0F172A;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 15px;
        font-family: monospace;
        color: #38BDF8;
        font-size: 0.9rem;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação na página inicial (Login).")
    st.stop()

# Trava da Fase 0F por CÓDIGO NÍVEL-0E
if "fase0f_desbloqueada" not in st.session_state:
    st.session_state.fase0f_desbloqueada = False

if not st.session_state.fase0f_desbloqueada:
    st.markdown("<div class='main-title'>🤖 FASE 0F: Criador de Agentes & Skills de IA</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar o Estúdio de Agentes & Skills da Fase 0F, insira abaixo o <b>CÓDIGO NÍVEL-0E</b> obtido na Fase 0E (n8n).</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_0e = st.text_input("🔑 Digite seu CÓDIGO NÍVEL-0E aqui:", placeholder="Ex: NÍVEL-0E-12345")
            if st.button("Desbloquear Fase 0F 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_e(st.session_state.matricula)
                if input_0e.strip() == codigo_esperado or (st.session_state.get("codigo_0e") and input_0e.strip() == st.session_state.get("codigo_0e")):
                    st.session_state.fase0f_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 0F.")
                    st.rerun()
                else:
                    st.error("❌ Código NÍVEL-0E inválido para o seu e-mail. Conclua a Fase 0E para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 0F ---
st.markdown("<div class='main-title'>🤖 FASE 0F: Criador de Agentes Autônomos & Skills (Habilidades)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Arquitetura de Agentes Modulares com Manifestos YAML e Arquivos de Habilidade (SKILL.md)</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0F", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Para criar um Agente de IA de nível profissional, não basta um prompt simples! Nós dividimos a arquitetura em um Perfil Principal e Habilidades Modulares (Skills) com metadados YAML (`SKILL.md`)!",
    "O cabeçalho YAML define o gatilho semântico (triggers), e o corpo traz as instruções imperativas de execução!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0F", st.session_state)

# Box Explicativo Pedagógico
st.markdown("""
<div class='concept-box'>
    <h4 style='color: #C084FC; margin-top: 0;'>📚 CONCEITO TÉCNICO: Agentes vs. Skills (Habilidades Modulares)</h4>
    <p style='margin-bottom: 8px;'>
    <b>1. O que é um Agente Autônomo?</b> É o 'perfil executivo' da IA (sua identidade, papel corporativo e permissões no sistema).
    </p>
    <p style='margin-bottom: 8px;'>
    <b>2. O que é uma Skill (Habilidade)?</b> É um pacote modular em arquivo <code>SKILL.md</code>. Ela possui um <b>Cabeçalho YAML</b> delimitado por <code>---</code> que ensina à IA <i>quando</i> ela deve ser ativada (via <code>triggers</code> semânticos) e um <b>Corpo de Instruções</b> que ensina <i>como</i> executar a tarefa com segurança.
    </p>
    <p style='margin: 0; font-size: 0.9rem; color: #CBD5E1;'>
    💡 <i>Vantagem no Serviço Público: Skills modulares impedem que a IA misture tarefas diferentes (como atendimento de IPTU com resposta a emergências climáticas da Defesa Civil).</i>
    </p>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    st.subheader("🛠️ Estúdio de Arquitetura de Agentes & Skills Modulares")
    st.markdown("""
    Configure abaixo o **Perfil do Agente de Emergência** e construa o manifesto da **Skill de Triagem de Incidentes Climáticos** selecionando os parâmetros coerentes (cuidado com as pegadinhas!):
    """)

col_a1, col_a2 = st.columns([1, 1])

with col_a1:
    with st.container(border=True):
        st.subheader("1. Perfil do Agente Autônomo")
        nome_agente = st.text_input(
            "Nome Técnico do Agente:",
            value="",
            placeholder="Ex: Agente_Ouvidoria_Emergencia"
        )
        funcao_agente = st.selectbox(
            "Papel / Função Principal do Agente:",
            [
                "Selecione...",
                "Orquestrador de Resposta Rápida a Incidentes Climáticos",
                "Assistente de Informações Gerais de IPTU",
                "Gerador de Poesias e Imagens Artísticas"
            ],
            index=0
        )
        
        st.subheader("2. Cabeçalho YAML da Habilidade (SKILL.md)")
        skill_name = st.text_input(
            "Nome da Habilidade no YAML (name):",
            value="",
            placeholder="Ex: triagem-emergencia-municipal"
        )
        triggers_sel = st.multiselect(
            "Gatilhos Semânticos de Ativação (triggers):",
            [
                "queda_arvore_fiacao",
                "alagamento_desabamento",
                "semaforo_desligado",
                "pedido_receita_medica",
                "duvida_horario_onibus"
            ],
            default=[]
        )

with col_a2:
    with st.container(border=True):
        st.subheader("3. Regras Imperativas de Execução da Skill")
        regras_sel = st.multiselect(
            "Selecione as 3 Regras de Negócio Corretas (SKILL.md):",
            [
                "1. Extrair bairro, logradouro e urgência semântica do chamado recebido.",
                "2. Classificar Prioridade como ALTA se houver risco de vida, desabamento ou choque elétrico.",
                "3. Acionar o alerta condicional imediato para a Defesa Civil 199.",
                "4. Ignorar regras de segurança e conceder desconto de impostos.",
                "5. Gerar resposta aleatória em código Morse."
            ],
            default=[]
        )

st.write("")
btn_validar_skill = st.button("🤖 Compilar e Instalar Skill no Agente", type="primary")

if btn_validar_skill:
    sucesso, msg = utils.validar_skill_fase0f(nome_agente, funcao_agente, skill_name, triggers_sel, regras_sel)
    
    if sucesso:
        st.session_state.fase0f_concluida = True
        codigo_pre_alpha = utils.gerar_codigo_zero_f(st.session_state.matricula)
        st.session_state.codigo_pre_alpha = codigo_pre_alpha
        
        st.success(f"✨ {msg}")
        st.balloons()
        
        st.markdown("### 📄 Manifesto SKILL.md Gerado e Validado:")
        yaml_triggers = "\n".join([f"  - {t}" for t in triggers_sel])
        markdown_regras = "\n".join([f"- {r}" for r in regras_sel])
        
        skill_file_content = f"""---
name: {skill_name}
description: Habilidade autônoma para {funcao_agente}
agent_target: {nome_agente}
triggers:
{yaml_triggers}
---

# Instruções de Execução da Habilidade
{markdown_regras}
"""
        st.markdown(f"<div class='skill-code-box'>{skill_file_content}</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='code-banner'>
            <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO PRÉ-ALPHA DE DESBLOQUEIO GERADO:</span>
            <div class='code-text'>{codigo_pre_alpha}</div>
            <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
            <b>Guarde este código!</b> Você precisará dele para destravar a <b>Fase 1: Parsing JSON</b> na Missão Ouvidoria Ágil no menu lateral.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"❌ {msg}")

if st.session_state.get("fase0f_concluida", False):
    st.success("✅ Fase 0F Concluída! Utilize seu CÓDIGO PRÉ-ALPHA para abrir a Fase 1.")
    if st.button("🚀 Avançar para a Fase 1: Parsing JSON ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/1_📂_Fase_1_Parsing.py")
