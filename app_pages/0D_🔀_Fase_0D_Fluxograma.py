import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0D: Fluxograma de Agente IA - Ouvidoria Ágil", page_icon="🔀", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #4ADE80; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
    .node-card {
        background-color: #1E293B;
        border: 2px solid #3B82F6;
        border-radius: 10px;
        padding: 15px;
        color: #F8FAFC;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 0D por CÓDIGO NÍVEL-0C
if "fase0d_desbloqueada" not in st.session_state:
    st.session_state.fase0d_desbloqueada = False

if not st.session_state.fase0d_desbloqueada:
    st.markdown("<div class='main-title'>🔀 FASE 0D: Arquitetura de Agentes & Fluxograma de Decisão</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar a Fase 0D, insira abaixo o <b>CÓDIGO NÍVEL-0C</b> obtido na Fase 0C.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_0c = st.text_input("🔑 Digite seu CÓDIGO NÍVEL-0C aqui:", placeholder="Ex: NÍVEL-0C-12345")
            if st.button("Desbloquear Fase 0D 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_c(st.session_state.matricula)
                if input_0c.strip() == codigo_esperado or (st.session_state.get("codigo_0c") and input_0c.strip() == st.session_state.get("codigo_0c")):
                    st.session_state.fase0d_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 0D.")
                    st.rerun()
                else:
                    st.error("❌ Código NÍVEL-0C inválido para o seu e-mail. Conclua a Fase 0C para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 0D ---
st.markdown("<div class='main-title'>🔀 FASE 0D: Canvas Visual de Fluxograma de Agentes de IA</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Construção da Arquitetura Lógica de Roteamento (Visual Pipeline Builder)</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0D", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Um agente público é um pipeline orquestrado! Organize a sequência visual dos nós do início ao fim.",
    "Coloque a Entrada de Dados primeiro, seguida pelo Classificador LLM e o Roteador Condicional!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0D", st.session_state)

with st.container(border=True):
    st.subheader("🧩 O Desafio de Orquestração do Agente Público")
    st.markdown("""
    Um **Agente de IA Generativa** eficiente no setor público não é apenas uma caixa de chat; é um **pipeline de decisão orquestrado**.
    
    Organize os **5 nós visuais** abaixo na sequência lógica correta de execução para garantir que chamados de emergência acionem a Defesa Civil e chamados normais alimentem a Ouvidoria:
    """)

col_f0d_a, col_f0d_b = st.columns([1, 1])

NOS_DISPONIVEIS = {
    "entrada": "📥 Entrada de Dados (Formulário / Webhook do Cidadão)",
    "classificador": "🧠 Agente LLM Classificador de Risco (Gemini 2.5)",
    "roteamento": "🔀 Roteador Condicional (If Risco == ALTA)",
    "acao_emergencia": "🚨 Alerta Imediato Defesa Civil 199 (SMS/Chamada)",
    "acao_ouvidoria": "📋 Registro de Manutenção (Planilha Ouvidoria)"
}

with col_f0d_a:
    with st.container(border=True):
        st.subheader("⚙️ Montagem do Fluxograma (Selecione a Sequência de Nós)")
        
        n1 = st.selectbox("1º Nó do Pipeline (Gatilho Inicial):", ["Selecione...", "classificador", "entrada", "roteamento", "acao_emergencia", "acao_ouvidoria"], format_func=lambda x: NOS_DISPONIVEIS.get(x, x))
        n2 = st.selectbox("2º Nó do Pipeline (Processamento IA):", ["Selecione...", "entrada", "classificador", "roteamento", "acao_ouvidoria", "acao_emergencia"], format_func=lambda x: NOS_DISPONIVEIS.get(x, x))
        n3 = st.selectbox("3º Nó do Pipeline (Decisão Lógica):", ["Selecione...", "roteamento", "classificador", "entrada", "acao_emergencia", "acao_ouvidoria"], format_func=lambda x: NOS_DISPONIVEIS.get(x, x))
        n4 = st.selectbox("4º Nó do Pipeline (Ramificação de Emergência):", ["Selecione...", "acao_emergencia", "roteamento", "classificador", "entrada", "acao_ouvidoria"], format_func=lambda x: NOS_DISPONIVEIS.get(x, x))
        n5 = st.selectbox("5º Nó do Pipeline (Ramificação de Ouvidoria):", ["Selecione...", "acao_ouvidoria", "acao_emergencia", "roteamento", "classificador", "entrada"], format_func=lambda x: NOS_DISPONIVEIS.get(x, x))
        
        btn_validar_fluxo = st.button("🚀 Validar e Executar Fluxograma de IA", type="primary")

with col_f0d_b:
    with st.container(border=True):
        st.subheader("👁️ Pré-visualização do Diagrama de Agentes")
        
        ordem_selecionada = [n for n in [n1, n2, n3, n4, n5] if n != "Selecione..."]
        
        if not ordem_selecionada:
            st.info("Selecione a sequência dos nós à esquerda para visualizar o diagrama interativo.")
        else:
            for idx, key_no in enumerate(ordem_selecionada):
                label = NOS_DISPONIVEIS.get(key_no, key_no)
                st.markdown(f"""
                <div class='node-card'>
                    <b style='color: #60A5FA;'>NÓ #{idx+1}:</b> {label}
                </div>
                """, unsafe_allow_html=True)
                if idx < len(ordem_selecionada) - 1:
                    st.markdown("<div style='text-align: center; color: #38BDF8; font-size: 1.5rem;'>⬇️</div>", unsafe_allow_html=True)

if btn_validar_fluxo:
    sucesso, msg = utils.validar_fluxograma_fase0d(ordem_selecionada)
    
    if sucesso:
        st.session_state.fase0d_concluida = True
        codigo_0d = utils.gerar_codigo_zero_d(st.session_state.matricula)
        st.session_state.codigo_0d = codigo_0d
        
        st.success(f"✨ {msg}")
        st.balloons()
        
        st.markdown(f"""
        <div class='code-banner'>
            <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO NÍVEL-0D DE DESBLOQUEIO GERADO:</span>
            <div class='code-text'>{codigo_0d}</div>
            <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
            <b>Copie este código!</b> Insira-o na <b>Fase 0E: Simulador n8n</b> no menu lateral.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"❌ {msg}")

if st.session_state.get("fase0d_concluida", False):
    st.success("✅ Fase 0D Concluída! Utilize seu CÓDIGO NÍVEL-0D para abrir a Fase 0E.")
    if st.button("🚀 Avançar para a Fase 0E: Simulador n8n ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/0E_⚡_Fase_0E_n8n.py")
