import streamlit as st
import hashlib
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 4: Relatório Executivo - Ouvidoria Ágil", page_icon="📊", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
    .cert-box {
        background-color: #0F172A;
        border: 3px solid #EAB308;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 4 por CÓDIGO GAMA
if "fase4_desbloqueada" not in st.session_state:
    st.session_state.fase4_desbloqueada = False

if not st.session_state.fase4_desbloqueada:
    st.markdown("<div class='main-title'>📊 FASE 4: Relatório Executivo & Gabinete de Crise</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar o Gabinete Executivo e gerar seu Certificado, insira abaixo o <b>CÓDIGO GAMA</b> obtido na Fase 3.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_gama = st.text_input("🔑 Digite seu CÓDIGO GAMA aqui:", placeholder="Ex: GAMA-12345")
            if st.button("Desbloquear Fase 4 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_gama(st.session_state.matricula)
                if input_gama.strip() == codigo_esperado or (st.session_state.get("codigo_gama") and input_gama.strip() == st.session_state.get("codigo_gama")):
                    st.session_state.fase4_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase Final.")
                    st.rerun()
                else:
                    st.error("❌ Código GAMA inválido para o seu e-mail. Conclua a Fase 3 para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 4 ---
st.markdown("<div class='main-title'>👑 FASE 4: Relatório Executivo e Síntese de Crise</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Consolidação Estratégica dos Dados de Emergência para o Gabinete do Prefeito</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("4", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Você chegou ao Gabinete do Prefeito! Escreva o Boletim de Emergência em Markdown com tabela, métricas dos 6 casos críticos e nota de imprensa!",
    "Substitua todos os marcadores entre colchetes pelos dados apurados na triagem!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("4", st.session_state)

with st.container(border=True):
    st.subheader("📋 Diretrizes da Coletiva de Imprensa Municipal (4 Seções Obrigatórias)")
    st.markdown("""
    O Prefeito e a Defesa Civil de Nova Esperança precisam apresentar um **Boletim de Resposta Rápida**. 
    Escreva ou gere via IA um relatório corporativo completo em Markdown.
    
    📌 **REQUISITOS OBRIGATÓRIOS DO RELATÓRIO:**
    1. **Tabela de Dados em Markdown:** Pelo menos uma tabela formatada (`| Coluna 1 | Coluna 2 |`) consolidando o total de chamados por prioridade.
    2. **Métricas Numéricas da Triagem:** Deve citar explicitamente a quantidade exata de **6 chamados de ALTA prioridade** calculados na Fase 2.
    3. **Zonas de Risco:** Mencionar os bairros críticos reais (ex: Bairro Industrial, Flores, Centro, Alto).
    4. **Plano Emergencial SLA 24h:** Atribuir ações a órgãos municipais (Defesa Civil, Concessionária de Energia, Secretaria de Obras).
    5. **Nota Oficial de Imprensa:** Incluir uma seção com a nota formal a ser lida pelo Prefeito na coletiva.
    """)

col_f4_a, col_f4_b = st.columns([1, 1])

with col_f4_a:
    with st.container(border=True):
        st.subheader("📝 Editor Markdown (Escreva seu Relatório)")
        
        # Template de estrutura sem os dados preenchidos (exige escrita do aluno)
        template_estrutura = f"""# Boletim de Emergência Municipal - Nova Esperança
**Responsável Técnico:** {st.session_state.nome} (Matrícula: {st.session_state.matricula})

## 1. Resumo Quantitativo da Triagem (Tabela Markdown)
[Crie aqui uma tabela em Markdown consolidando as métricas de chamados em ALTA, MÉDIA e BAIXA prioridade]

## 2. Mapeamento de Zonas Críticas por Bairro
[Descreva aqui os bairros mais afetados identificados nos seus chamados]

## 3. Plano de Ação SLA 24 Horas
[Liste 3 ações emergenciais distribuídas entre a Defesa Civil, Concessionária de Energia e Secretaria de Obras]

## 4. Nota Oficial para a Coletiva de Imprensa
[Escreva a declaração oficial que o Prefeito de Nova Esperança apresentará na imprensa]
"""
        
        relatorio_user = st.text_area(
            "Escreva ou ajuste seu relatório Markdown abaixo:",
            value=template_estrutura,
            height=380
        )
        
        btn_enviar = st.button("Enviar Relatório Final e Validar Certificado 📨", type="primary")

with col_f4_b:
    with st.container(border=True):
        st.subheader("👁️ Pré-visualização do Boletim Oficial")
        st.markdown(relatorio_user)

if btn_enviar:
    if "[crie aqui" in relatorio_user.lower() or "[descreva aqui" in relatorio_user.lower() or "[liste" in relatorio_user.lower() or "[escreva" in relatorio_user.lower():
        st.error("❌ Preencha os campos entre colchetes no relatório antes de submeter!")
    else:
        sucesso, msg = utils.validar_relatorio_fase4_rigoroso(relatorio_user, st.session_state.matricula, total_alta_esperado=6)
        
        if sucesso:
            st.session_state.fase4_concluida = True
            st.session_state.xp = 1000
            
            st.success(f"🎉 {msg}")
            st.balloons()
            
            st.markdown("""
            <div style="background-color: #064E3B; border: 2px solid #10B981; border-radius: 12px; padding: 20px; margin: 20px 0; text-align: center;">
                <h2 style="color: #34D399; margin-top: 0;">🎓 VOCÊ CONCLUIU TODAS AS FASES DO DESAFIO!</h2>
                <p style="color: #F8FAFC; font-size: 1.1rem;">Seu Relatório Executivo foi aprovado e você acumulou <b>1000 / 1000 XP</b>!</p>
                <p style="color: #CBD5E1; font-size: 1rem; margin-bottom: 0;">
                Acesse agora a página <b>🏆 Conclusão & Certificado</b> no menu lateral para visualizar, imprimir ou baixar o seu <b>Certificado Oficial de Conclusão</b>!
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.download_button(
                label="📥 Baixar Relatório Técnico Final (.md)",
                data=relatorio_user,
                file_name="Relatorio_Executivo_Ouvidoria_Agil.md",
                mime="text/markdown"
            )
        else:
            st.error(f"❌ {msg}")

if st.session_state.get("fase4_concluida", False):
    st.success("✅ Fase 4 Concluída com Nota Máxima (1000 XP)!")
    if st.button("🎓 Ir para Conclusão & Emitir Certificado 🏆", type="primary", use_container_width=True):
        st.switch_page("app_pages/5_🏆_Certificado_Final.py")
