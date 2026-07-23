import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0B: Prompting Estruturado - Ouvidoria Ágil", page_icon="✍️", layout="wide")

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

# Trava da Fase 0B por CÓDIGO NÍVEL-0A
if "fase0b_desbloqueada" not in st.session_state:
    st.session_state.fase0b_desbloqueada = False

if not st.session_state.fase0b_desbloqueada:
    st.markdown("<div class='main-title'>✍️ FASE 0B: Engenharia de Prompt Estruturada</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar a Fase 0B, insira abaixo o <b>CÓDIGO NÍVEL-0A</b> obtido na Fase 0A.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_0a = st.text_input("🔑 Digite seu CÓDIGO NÍVEL-0A aqui:", placeholder="Ex: NÍVEL-0A-12345")
            if st.button("Desbloquear Fase 0B 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_a(st.session_state.matricula)
                if input_0a.strip() == codigo_esperado or (st.session_state.get("codigo_0a") and input_0a.strip() == st.session_state.get("codigo_0a")):
                    st.session_state.fase0b_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 0B.")
                    st.rerun()
                else:
                    st.error("❌ Código NÍVEL-0A inválido para o seu e-mail. Conclua a Fase 0A para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 0B ---
st.markdown("<div class='main-title'>✍️ FASE 0B: Construção de Prompts Estruturados (RTF / CRISP)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Aplicação Prática de Role (Persona), Task (Tarefa), Format (Formato) e Delimitadores</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0B", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Para o modelo não alucinar no resumo da Ata Legislativa, estruture seu prompt no padrão RTF/CRISP!",
    "Isolar o texto de entrada entre delimitadores (como ###) impede que a IA confunda as instruções com a ata de entrada!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0B", st.session_state)

col_f0b_a, col_f0b_b = st.columns([1, 1])

with col_f0b_a:
    with st.container(border=True):
        st.subheader("🎯 O Desafio de Síntese de Ata Legislativa")
        st.markdown("""
        A Câmara Municipal de Nova Esperança aprovou o plano de contingência para a tempestade. 
        Sua tarefa é escrever um **Prompt Estruturado Profissional** que instrua uma IA a resumir o texto da ata abaixo sem alucinar.
        
        📌 **REQUISITOS MANDATÓRIOS DO PROMPT (Estrutura RTF/CRISP):**
        1. **Role (Persona):** Declarar o papel (Ex: *"Aja como um redator técnico da prefeitura..."*).
        2. **Task (Tarefa):** Definir o objetivo (Ex: *"Resuma os 3 pontos estratégicos da ata legislativa..."*).
        3. **Format (Formato):** Exigir a estrutura de saída (Ex: *"Apresente o resultado em tópicos Markdown..."*).
        4. **Delimitador:** Utilizar marcas como `###` ou `---` isolando o texto da ata de entrada.
        """)
        
        st.markdown("#### 📜 Texto da Ata Legislativa Ordinária (Entrada):")
        texto_ata = """### ATA DA SESSÃO EXTRAORDINÁRIA DE CONTINGÊNCIA
Em 22 de Julho de 2026, a Câmara Municipal aprovou por unanimidade:
1. Liberação de crédito suplementar emergencial de R$ 2,5 milhões para a Defesa Civil.
2. Contratação em caráter emergencial de 10 caminhões-pipa e equipes de poda de árvores de grande porte.
3. Isenção temporária da taxa de religação de água e energia para os moradores afetados no Bairro Industrial."""
        st.code(texto_ata, language="text")

with col_f0b_b:
    with st.container(border=True):
        st.subheader("📝 Laboratório de Prompting")
        
        prompt_input = st.text_area(
            "Escreva seu Prompt Estruturado abaixo:",
            height=280,
            placeholder="Escreva aqui o seu prompt estruturado definindo a Persona (Role), a Tarefa (Task), o Formato de saída desejado e os Delimitadores..."
        )
        
        btn_validar_prompt = st.button("Validar Estrutura do Prompt ⚙️", type="primary")
        
        if btn_validar_prompt:
            sucesso, msg = utils.validar_prompt_fase0b(prompt_input)
            
            if sucesso:
                st.session_state.fase0b_concluida = True
                codigo_0b = utils.gerar_codigo_zero_b(st.session_state.matricula)
                st.session_state.codigo_0b = codigo_0b
                
                st.success(f"✨ {msg}")
                st.balloons()
                
                st.markdown(f"""
                <div class='code-banner'>
                    <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO NÍVEL-0B DE DESBLOQUEIO GERADO:</span>
                    <div class='code-text'>{codigo_0b}</div>
                    <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                    <b>Copie este código!</b> Insira-o na <b>Fase 0C: Fichas Digitais em Python</b> no menu lateral.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"❌ Validação Falhou:\n{msg}")

if st.session_state.get("fase0b_concluida", False):
    st.success("✅ Fase 0B Concluída! Utilize seu CÓDIGO NÍVEL-0B para abrir a Fase 0C.")
    if st.button("🚀 Avançar para a Fase 0C: Fichas Python ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/0C_🐍_Fase_0C_Estruturas.py")
