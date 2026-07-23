import streamlit as st
import pandas as pd
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 2: Sandbox Python - Ouvidoria Ágil", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #38BDF8; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #38BDF8; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 2 por CÓDIGO ALPHA
if "fase2_desbloqueada" not in st.session_state:
    st.session_state.fase2_desbloqueada = False

if not st.session_state.fase2_desbloqueada:
    st.markdown("<div class='main-title'>⚡ FASE 2: Motor de Código & Matriz de Risco</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar o Sandbox de Código da Fase 2, insira abaixo o <b>CÓDIGO ALPHA</b> obtido na Fase 1.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_alpha = st.text_input("🔑 Digite seu CÓDIGO ALPHA aqui:", placeholder="Ex: ALPHA-12345")
            if st.button("Desbloquear Fase 2 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_alpha(st.session_state.matricula, 15)
                if input_alpha.strip() == codigo_esperado or (st.session_state.get("codigo_alpha") and input_alpha.strip() == st.session_state.get("codigo_alpha")):
                    st.session_state.fase2_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 2.")
                    st.rerun()
                else:
                    st.error("❌ Código ALPHA inválido para o seu e-mail. Conclua a Fase 1 para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 2 ---
st.markdown("<div class='main-title'>⚡ FASE 2: Sandbox de Código Python & Automação de Risco</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Programação da Função de Triagem em Lote com 20 Casos de Teste de Estresse</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("2", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Projete o algoritmo `def triar_chamado(item):` em Python! Teste suas condições contra os 20 casos de estresse!",
    "Trate as exceções de BAIXA prioridade (como podas preventivas) no topo da função `if` antes das emergências de alta tensão!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("2", st.session_state)

col_f2_a, col_f2_b = st.columns([1, 1])

with col_f2_a:
    with st.container(border=True):
        st.subheader("👨‍💻 Escreva sua Função Python: `triar_chamado(item)`")
        st.markdown("""
        Projete o algoritmo de triagem municipal em Python. Sua função deve receber o objeto `item` e retornar **`'ALTA'`**, **`'MÉDIA'`** ou **`'BAIXA'`**.
        
        📌 **Estrutura do parâmetro `item` recebido:**
        - `item["texto"]`: Texto bruto da ocorrência.
        - `item["categoria_enum"]`: Categoria normalizada (`ARVORE_FIAÇÃO`, `ALAGAMENTO_DESABAMENTO`, `BURACO_VIA`, `FALTA_ENERGIA`, `SEMAFORO`, `ENTULHO`).
        - `item["nivel_urgencia_declarado"]`: `EMERGENCIA` ou `NORMAL`.
        
        ⚠️ **DIRETRIZES DA DEFESA CIVIL (RISCO E EXCEÇÕES):**
        - **ALTA:** Risco à vida, fiação de alta tensão soltando faísca, desabamentos, inundações com resgate ou acidentes com feridos.
        - **MÉDIA:** Semáforos apagados, buracos em vias, fiação telefônica caída sem faísca ou apagões gerais de bairro.
        - **BAIXA:** Manutenções rotineiras, entulhos na calçada, lâmpadas queimadas individuais e **podas preventivas de árvores sem risco imediato**.
        """)
        
        # Template zerado (sem código pré-pronto de gabarito)
        codigo_starter = """def triar_chamado(item):
    # item["texto"] -> Texto bruto da ocorrência
    # item["categoria_enum"] -> 'ARVORE_FIAÇÃO', 'ALAGAMENTO_DESABAMENTO', 'BURACO_VIA', 'FALTA_ENERGIA', 'SEMAFORO', 'ENTULHO'
    # item["nivel_urgencia_declarado"] -> 'EMERGENCIA' ou 'NORMAL'
    
    # Escreva suas regras de triagem abaixo e retorne 'ALTA', 'MÉDIA' ou 'BAIXA':
    pass
"""
        
        codigo_usuario = st.text_area(
            "Editor de Código Python (Sandbox):",
            value=codigo_starter,
            height=280
        )
        
        btn_executar = st.button("Executar Código Sandbox (20 Casos) ⚙️", type="primary")

with col_f2_b:
    with st.container(border=True):
        st.subheader("📊 Output de Execução dos Testes")
        
        if btn_executar:
            if not codigo_usuario.strip() or "pass" in codigo_usuario and len(codigo_usuario.strip().splitlines()) <= 8:
                st.warning("Escreva a sua lógica de código na função antes de executar os testes.")
            else:
                sucesso, msg, resultados, acertos = utils.executar_script_sandbox_fase2(
                    codigo_usuario, 
                    st.session_state.matricula
                )
                
                df_res = pd.DataFrame(resultados)
                
                if sucesso:
                    st.session_state.fase2_concluida = True
                    st.session_state.total_alta = 6
                    
                    codigo_beta = utils.gerar_codigo_beta(st.session_state.matricula, acertos)
                    st.session_state.codigo_beta = codigo_beta
                    
                    st.success(f"✨ {msg}")
                    st.balloons()
                    
                    st.markdown(f"""
                    <div class='code-banner'>
                        <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO BETA DE DESBLOQUEIO GERADO:</span>
                        <div class='code-text'>{codigo_beta}</div>
                        <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                        <b>Guarde este código acima!</b> Você precisará dele para abrir a <b>Fase 3: Red Teaming</b> no menu lateral.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ {msg}")
                    
                st.dataframe(df_res, use_container_width=True)

if st.session_state.get("fase2_concluida", False):
    st.success("✅ Fase 2 Concluída com êxito! Utilize seu CÓDIGO BETA para abrir a Fase 3.")
    if st.button("🚀 Avançar para a Fase 3: Red Teaming ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/3_🛡️_Fase_3_RedTeaming.py")
