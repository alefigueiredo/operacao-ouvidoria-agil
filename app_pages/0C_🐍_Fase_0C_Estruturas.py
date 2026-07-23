import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0C: Fichas Digitais em Python - Ouvidoria Ágil", page_icon="🐍", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #4ADE80; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 0C por CÓDIGO NÍVEL-0B
if "fase0c_desbloqueada" not in st.session_state:
    st.session_state.fase0c_desbloqueada = False

if not st.session_state.fase0c_desbloqueada:
    st.markdown("<div class='main-title'>🐍 FASE 0C: Fichas Digitais em Python</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar a Fase 0C, insira abaixo o <b>CÓDIGO NÍVEL-0B</b> obtido na Fase 0B.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_0b = st.text_input("🔑 Digite seu CÓDIGO NÍVEL-0B aqui:", placeholder="Ex: NÍVEL-0B-12345")
            if st.button("Desbloquear Fase 0C 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_b(st.session_state.matricula)
                if input_0b.strip() == codigo_esperado or (st.session_state.get("codigo_0b") and input_0b.strip() == st.session_state.get("codigo_0b")):
                    st.session_state.fase0c_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 0C.")
                    st.rerun()
                else:
                    st.error("❌ Código NÍVEL-0B inválido para o seu e-mail. Conclua a Fase 0B para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 0C ---
st.markdown("<div class='main-title'>🐍 FASE 0C: Fichas Digitais e Estruturas de Dados em Python</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Organização Administrativa de Registros usando Listas `[...]` e Dicionários `{...}`</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0C", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Modernize a prefeitura! Crie a variável `fichas_manutencao` recebendo uma Lista `[...]` de Dicionários `{...}` contendo os atributos dos chamados!",
    "Estruturar dados em dicionários facilita a integração automática com APIs e LLMs no futuro!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0C", st.session_state)

col_f0c_a, col_f0c_b = st.columns([1, 1])

with col_f0c_a:
    with st.container(border=True):
        st.subheader("🎯 O Desafio da Ficha Digital Municipal")
        st.markdown("""
        A modernização administrativa de Nova Esperança exige a transição de métodos analógicos para **fichas digitais em Python**.
        
        Sua missão é escrever um script Python simples criando uma **Lista de Dicionários** para armazenar pelo menos **2 registros de chamados de manutenção**.
        
        📌 **REQUISITOS DO CÓDIGO PYTHON:**
        1. Criar uma variável contendo uma Lista `fichas_manutencao = [...]`.
        2. Cada item da lista deve ser um Dicionário `{...}` contendo pelo menos 3 atributos:
           - `'protocolo'`: número inteiro.
           - `'bairro'`: nome do bairro (string).
           - `'descricao'`: resumo do problema (string).
        """)

with col_f0c_b:
    with st.container(border=True):
        st.subheader("💻 Editor Python (Fichas Digitais)")
        
        code_starter = """# Escreva abaixo a sua estrutura de Fichas Digitais em Python:
# Crie uma variável 'fichas_manutencao' contendo uma lista de dicionários [...]

"""
        
        codigo_input = st.text_area(
            "Código Python (Dicionários & Listas):",
            value=code_starter,
            height=260
        )
        
        btn_validar_py = st.button("Executar e Validar Ficha Digital ⚙️", type="primary")
        
        if btn_validar_py:
            sucesso, msg = utils.validar_python_fase0c(codigo_input)
            
            if sucesso:
                st.session_state.fase0c_concluida = True
                codigo_0c = utils.gerar_codigo_zero_c(st.session_state.matricula)
                st.session_state.codigo_0c = codigo_0c
                
                st.success(f"✨ {msg}")
                st.balloons()
                
                st.markdown(f"""
                <div class='code-banner'>
                    <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO NÍVEL-0C DE DESBLOQUEIO GERADO:</span>
                    <div class='code-text'>{codigo_0c}</div>
                    <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                    <b>Guarde este código!</b> Você precisará dele para destravar a <b>Fase 0D: Fluxograma de Agentes</b> no menu lateral.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"❌ Validação Falhou:\n{msg}")

if st.session_state.get("fase0c_concluida", False):
    st.success("✅ Fase 0C Concluída! Utilize seu CÓDIGO NÍVEL-0C para abrir a Fase 0D.")
    if st.button("🚀 Avançar para a Fase 0D: Fluxogramas IA ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/0D_🔀_Fase_0D_Fluxograma.py")
