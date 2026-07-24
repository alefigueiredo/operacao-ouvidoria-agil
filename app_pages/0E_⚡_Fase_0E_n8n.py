import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0E: Simulador n8n - Ouvidoria Ágil", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #4ADE80; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
    .n8n-node {
        background-color: #0F172A;
        border: 2px solid #EC4899;
        border-radius: 10px;
        padding: 15px;
        color: #F8FAFC;
        margin-bottom: 15px;
    }
    .n8n-title {
        color: #F472B6;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 0E por CÓDIGO NÍVEL-0D
if "fase0e_desbloqueada" not in st.session_state:
    st.session_state.fase0e_desbloqueada = False

if not st.session_state.fase0e_desbloqueada:
    st.markdown("<div class='main-title'>⚡ FASE 0E: Simulador de Automação Visual n8n</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar o Simulador n8n da Fase 0E, insira abaixo o <b>CÓDIGO NÍVEL-0D</b> obtido na Fase 0D.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_0d = st.text_input("🔑 Digite seu CÓDIGO NÍVEL-0D aqui:", placeholder="Ex: NÍVEL-0D-12345")
            if st.button("Desbloquear Fase 0E 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_d(st.session_state.matricula)
                if input_0d.strip() == codigo_esperado or (st.session_state.get("codigo_0d") and input_0d.strip() == st.session_state.get("codigo_0d")):
                    st.session_state.fase0e_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 0E.")
                    st.rerun()
                else:
                    st.error("❌ Código NÍVEL-0D inválido para o seu e-mail. Conclua a Fase 0D para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 0E ---
st.markdown("<div class='main-title'>⚡ FASE 0E: Simulador Visual de Workflows n8n</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Oficina Prática de Automação Municipal sem Código (Forms + IA + Planilhas + E-mail)</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0E", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Hora de integrar o workflow sem código! Configure o Webhook com `POST /ouvidoria`, conecte o Gemini 2.5 Flash, a planilha Sheets e o e-mail de alerta!",
    "Certifique-se de preencher e configurar as opções de todos os 4 nós!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0E", st.session_state)

with st.container(border=True):
    st.subheader("🛠️ O Cenário Real da Oficina de n8n")
    st.markdown("""
    Conforme a política de governança de IA pública, o workflow do **n8n** deve possuir **5 Nós de Automação Visual** para capturar, anonimizar via LGPD, classificar via IA, armazenar e notificar.
    """)

col_n1, col_n2 = st.columns(2)

with col_n1:
    st.markdown("""
    <div class='n8n-node'>
        <div class='n8n-title'>⚡ NÓ 1: Webhook Trigger (Entrada do Formulário)</div>
        Recepção HTTP das solicitações enviadas pelos cidadãos.
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        http_method = st.selectbox("Método HTTP do Webhook:", ["Selecione...", "GET", "POST", "PUT"], index=0)
        route_path = st.text_input("Caminho da Rota de Recepção:", value="", placeholder="Ex: /ouvidoria")
        webhook_ok = (http_method == "POST" and route_path.strip() == "/ouvidoria")

    st.markdown("""
    <div class='n8n-node'>
        <div class='n8n-title'>🛡️ NÓ 2: Privacy Anonymizer (Filtro LGPD)</div>
        Mascaramento automático de CPF, Nome e Telefone antes de enviar à API externa.
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        lgpd_mask_action = st.selectbox("Ação do Filtro LGPD:", ["Selecione...", "Manter dados pessoais abertos", "Mascarar CPF/Nome/Telefone com HASH", "Descartar payload"], index=0)
        lgpd_filter_ok = ("Mascarar" in lgpd_mask_action)

    st.markdown("""
    <div class='n8n-node'>
        <div class='n8n-title'>🧠 NÓ 3: Google Gemini AI (Processador LLM)</div>
        Análise semântica e extração de prioridade dos chamados.
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        ai_action = st.selectbox("Ação do Nó da IA:", ["Selecione...", "Text Generation", "Text Analysis & Categorization", "Image Generation"], index=0)
        ai_model = st.selectbox("Modelo Generativo Selecionado:", ["Selecione...", "Google Gemini 2.5 Flash", "GPT-3.5 Legacy", "Claude 2"], index=0)
        ai_model_ok = ("Categorization" in ai_action and "Gemini 2.5" in ai_model)

with col_n2:
    st.markdown("""
    <div class='n8n-node'>
        <div class='n8n-title'>📊 NÓ 4: Google Sheets (Planilha de Controle)</div>
        Registro automático das colunas de Bairro e Prioridade.
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        sheet_operation = st.selectbox("Operação na Planilha:", ["Selecione...", "Read Rows", "Append / Upsert Row", "Delete Sheet"], index=0)
        map_cols = st.multiselect("Mapeamento de Colunas:", ["ID_Protocolo", "Bairro", "Prioridade_Risco", "Data_Hora"])
        sheet_ok = ("Append" in sheet_operation and "Prioridade_Risco" in map_cols)

    st.markdown("""
    <div class='n8n-node'>
        <div class='n8n-title'>✉️ NÓ 5: Gmail / Notificação (E-mail Automático)</div>
        Disparo de alerta imediato para a Secretaria de Obras.
    </div>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        email_trigger = st.selectbox("Gatilho de Envio do E-mail:", ["Selecione...", "Enviar para todos os inscritos", "Enviar apenas se Prioridade == ALTA", "Não enviar"], index=0)
        email_target = st.text_input("E-mail de Destino:", value="", placeholder="Ex: obras@novaesperanca.sp.gov.br")
        email_ok = ("ALTA" in email_trigger and "@" in email_target and "novaesperanca" in email_target)

st.write("")
btn_executar_n8n = st.button("⚡ Executar e Simular Pipeline do n8n (5 Nós)", type="primary")

if btn_executar_n8n:
    if http_method == "Selecione..." or lgpd_mask_action == "Selecione..." or ai_action == "Selecione..." or sheet_operation == "Selecione..." or email_trigger == "Selecione...":
        st.warning("⚠️ Preencha as configurações de todos os 5 nós do n8n antes de simular a execução!")
    else:
        sucesso, msg = utils.validar_n8n_fase0e(webhook_ok, lgpd_filter_ok, ai_model_ok, sheet_ok, email_ok)
        
        if sucesso:
            st.session_state.fase0e_concluida = True
            codigo_0e = utils.gerar_codigo_zero_e(st.session_state.matricula)
            st.session_state.codigo_0e = codigo_0e
            
            st.success(f"✨ {msg}")
            st.balloons()
            
            st.markdown(f"""
            <div class='code-banner'>
                <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO NÍVEL-0E DE DESBLOQUEIO GERADO:</span>
                <div class='code-text'>{codigo_0e}</div>
                <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                <b>Copie este código!</b> Insira-o na <b>Fase 0F: Criador de Agentes & Skills</b> no menu lateral.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"❌ {msg}")

if st.session_state.get("fase0e_concluida", False):
    st.success("✅ Fase 0E Concluída! Utilize seu CÓDIGO NÍVEL-0E para abrir a Fase 0F.")
    if st.button("🚀 Avançar para a Fase 0F: Agentes & Skills ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/0F_🤖_Fase_0F_Agentes.py")
