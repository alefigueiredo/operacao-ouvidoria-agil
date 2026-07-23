import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 1: Parsing JSON Avançado - Ouvidoria Ágil", page_icon="📂", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #22C55E; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #4ADE80; letter-spacing: 2px; }
    .spec-box { background-color: #1E293B; border: 1px solid #334155; color: #F8FAFC; padding: 18px; border-radius: 8px; font-size: 0.92rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); }
    .spec-box code { background-color: #0F172A; color: #38BDF8; border: 1px solid #334155; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.88rem; display: inline-block; margin: 2px 0; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 1 por CÓDIGO PRÉ-ALPHA
if "fase1_desbloqueada" not in st.session_state:
    st.session_state.fase1_desbloqueada = False

if not st.session_state.fase1_desbloqueada:
    st.markdown("<div class='main-title'>📂 FASE 1: Parsing e Limpeza Semântica de Dados</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar a Fase 1 da Missão Ouvidoria Ágil, insira abaixo o <b>CÓDIGO PRÉ-ALPHA</b> obtido na Fase 0F (Agentes & Skills).</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_pre_alpha = st.text_input("🔑 Digite seu CÓDIGO PRÉ-ALPHA aqui:", placeholder="Ex: PRÉ-ALPHA-12345")
            if st.button("Desbloquear Fase 1 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_zero_f(st.session_state.matricula)
                if input_pre_alpha.strip() == codigo_esperado or (st.session_state.get("codigo_pre_alpha") and input_pre_alpha.strip() == st.session_state.get("codigo_pre_alpha")):
                    st.session_state.fase1_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 1.")
                    st.rerun()
                else:
                    st.error("❌ Código PRÉ-ALPHA inválido para o seu e-mail. Conclua a Fase 0F para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 1 ---
chamados_aluno = utils.obter_chamados_estudante(st.session_state.matricula)
checksum_val = utils.calcular_checksum_matricula(st.session_state.matricula)

st.markdown("<div class='main-title'>📂 FASE 1: Parsing e Limpeza Semântica de Dados</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>Estruturação de Dados com Trava Anti-Cola para a Matrícula: <b>{st.session_state.matricula}</b></div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("1", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    f"A tempestade desabou! Extraia os 15 chamados em JSON limpo com as 9 chaves obrigatórias, incluindo a trava anti-cola `checksum_matricula`!",
    f"Sua chave `checksum_matricula` deve conter o número exato {checksum_val} calculado para a sua Matrícula!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("1", st.session_state)

col_a, col_b = st.columns([1, 1])

with col_a:
    with st.container(border=True):
        st.subheader("🎯 O Desafio de Prompt Engineering")
        st.markdown(f"""
        Os 15 chamados abaixo foram gerados de forma **única e personalizada para a sua Matrícula**.
        
        Você deve projetar um prompt de IA capaz de extrair os dados e remover ruídos como informações entre parênteses `"(nao a atriz rs)"`, formatando o JSON estritamente conforme o contrato técnico de **9 chaves obrigatórias**:
        """)
        
        st.markdown(f"""
        <div class='spec-box'>
            <b style='color: #60A5FA;'>📌 CONTRATO TÉCNICO DAS 9 CHAVES DO JSON:</b><br/><br/>
            1. <code>id_chamado</code>: Número de 1 a 15.<br/>
            2. <code>cidadao_formatado</code>: Nome limpo no formato <b>'SOBRENOME, Nome'</b> (Ex: <i>'SILVA, Marcos'</i> - sem ruídos parentéticos).<br/>
            3. <code>bairro</code>: Nome do bairro extraído.<br/>
            4. <code>logradouro</code>: Nome da rua/avenida sem o número.<br/>
            5. <code>numero</code>: Número do imóvel extraído como string (Ex: <i>'45'</i>, <i>'72'</i>) ou <b>'S/N'</b> se não houver número.<br/>
            6. <code>categoria_enum</code>: Constante exata: <code>'ARVORE_FIAÇÃO'</code>, <code>'ALAGAMENTO_DESABAMENTO'</code>, <code>'BURACO_VIA'</code>, <code>'FALTA_ENERGIA'</code>, <code>'SEMAFORO'</code> ou <code>'ENTULHO'</code>.<br/>
            7. <code>nivel_urgencia_declarado</code>: Retornar <code>'EMERGENCIA'</code> se contiver alerta/socorro, senão <code>'NORMAL'</code>.<br/>
            8. <code>descricao_limpa</code>: Resumo formal e corrigido do problema.<br/>
            9. 🛡️ <code>checksum_matricula</code>: Valor numérico obrigatório: <b><code>{checksum_val}</code></b> (soma dos dígitos da sua Matrícula {st.session_state.matricula}).
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"#### 📋 15 Chamados Brutos (Matrícula {st.session_state.matricula}):")
        texto_bruto_concat = "\n".join([c["texto"] for c in chamados_aluno])
        st.code(texto_bruto_concat, language="text")

with col_b:
    with st.container(border=True):
        st.subheader("🤖 Validador Anti-Cola por Checksum de Servidor")
        st.info(f"💡 **Trava Anti-Cola Ativa:** Cada objeto JSON deve conter a 9ª chave `\"checksum_matricula\": {checksum_val}`. Respostas genéricas sem esta instrução serão rejeitadas!")
        
        json_input = st.text_area(
            "Cole aqui o código JSON gerado pelo seu Prompt de IA:",
            height=360,
            placeholder=f"[\n  {{\n    \"id_chamado\": 1,\n    \"cidadao_formatado\": \"SILVA, Marcos\",\n    \"bairro\": \"Bairro das Flores\",\n    \"logradouro\": \"rua das Palmeiras\",\n    \"numero\": \"45\",\n    \"categoria_enum\": \"ARVORE_FIAÇÃO\",\n    \"nivel_urgencia_declarado\": \"EMERGENCIA\",\n    \"descricao_limpa\": \"Árvore de grande porte caiu bloqueando a via...\",\n    \"checksum_matricula\": {checksum_val}\n  }}\n]"
        )
        
        if st.button("Validar Estrutura e Dados do JSON 🛠️", type="primary"):
            sucesso, msg, data_parsed = utils.validar_json_fase1_estudante(json_input, st.session_state.matricula)
            
            if sucesso:
                st.session_state.json_validado = data_parsed
                st.session_state.fase1_concluida = True
                
                codigo_alpha = utils.gerar_codigo_alpha(st.session_state.matricula, len(json_input))
                st.session_state.codigo_alpha = codigo_alpha
                
                st.success(f"✨ {msg}")
                st.balloons()
                
                st.markdown(f"""
                <div class='code-banner'>
                    <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO ALPHA DE DESBLOQUEIO GERADO:</span>
                    <div class='code-text'>{codigo_alpha}</div>
                    <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                    <b>Copie este código!</b> Insira-o na <b>Fase 2: Automação & Risco</b> no menu lateral.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"❌ Validação Falhou:\n{msg}")

if st.session_state.get("fase1_concluida", False):
    st.success("✅ Fase 1 Concluída com êxito! Utilize seu CÓDIGO ALPHA para desbloquear a Fase 2.")
    if st.button("🚀 Avançar para a Fase 2: Automação & Risco ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/2_⚡_Fase_2_Automacao.py")
