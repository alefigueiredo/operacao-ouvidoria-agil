import streamlit as st
import re
import os
import time
import importlib
import utils
importlib.reload(utils)
from PIL import Image

# Configuração da página principal
st.set_page_config(
    page_title="Operação Ouvidoria Ágil - Trilha Completa",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Globais do Sistema
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #38BDF8;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 25px;
    }
    .mascote-box {
        background-color: #1E293B;
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #F8FAFC;
    }
    .mascote-title {
        font-weight: bold;
        color: #60A5FA;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar Estado da Sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
if "nome" not in st.session_state:
    st.session_state.nome = ""
if "matricula" not in st.session_state:
    st.session_state.matricula = ""
if "openrouter_key" not in st.session_state:
    st.session_state.openrouter_key = ""
if "xp" not in st.session_state:
    st.session_state.xp = 0

# Conclusão das Fases
for f_key in ["fase0a_concluida", "fase0b_concluida", "fase0c_concluida", "fase0d_concluida", "fase0e_concluida", "fase0f_concluida", "fase1_concluida", "fase2_concluida", "fase3_concluida", "fase4_concluida"]:
    if f_key not in st.session_state:
        st.session_state[f_key] = False

# Carregar Imagens
logo_img = None
mascote_img = None

if os.path.exists("operacao_ouvidoria_agil_logo.jpg"):
    try:
        logo_img = Image.open("operacao_ouvidoria_agil_logo.jpg")
    except Exception:
        pass

if os.path.exists("operacao_ouvidoria_agil_mascote.jpg"):
    try:
        mascote_img = Image.open("operacao_ouvidoria_agil_mascote.jpg")
    except Exception:
        pass

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    if logo_img:
        st.image(logo_img, width=280)
    else:
        st.markdown("<h2 style='text-align: center; color: #38BDF8;'>🌧️ Ouvidoria Ágil</h2>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    if st.session_state.logado:
        st.success(f"**Participante:** {st.session_state.nome}\n\n**E-mail:** {st.session_state.matricula}")
        
        # Calcular XP Total (10 Fases = 1000 XP máximo, ajustado para 75% caso a Dica de Ouro tenha sido usada)
        def get_xp(fase_id, val_base, concluida):
            if not concluida:
                return 0
            if st.session_state.get(f"ajuda_usada_{fase_id}", False):
                return int(val_base * 0.75)
            return val_base

        xp_total = 50
        xp_total += get_xp("0A", 50, st.session_state.fase0a_concluida)
        xp_total += get_xp("0B", 50, st.session_state.fase0b_concluida)
        xp_total += get_xp("0C", 50, st.session_state.fase0c_concluida)
        xp_total += get_xp("0D", 75, st.session_state.fase0d_concluida)
        xp_total += get_xp("0E", 75, st.session_state.fase0e_concluida)
        xp_total += get_xp("0F", 100, st.session_state.fase0f_concluida)
        xp_total += get_xp("1",  150, st.session_state.fase1_concluida)
        xp_total += get_xp("2",  150, st.session_state.fase2_concluida)
        xp_total += get_xp("3",  150, st.session_state.fase3_concluida)
        xp_total += get_xp("4",  100, st.session_state.fase4_concluida)
        st.session_state.xp = xp_total
        utils.salvar_progresso_estudante(st.session_state)
        
        st.markdown(f"**Progresso de XP:** {st.session_state.xp} / 1000")
        st.progress(st.session_state.xp / 1000)
        
        st.markdown("### 🏅 Conquistas Desbloqueadas")
        if st.session_state.fase0a_concluida: st.markdown("🧠 **Fundamentos de GenAI**")
        if st.session_state.fase0b_concluida: st.markdown("✍️ **Mestre em Prompting RTF**")
        if st.session_state.fase0c_concluida: st.markdown("🐍 **Arquiteto de Fichas Python**")
        if st.session_state.fase0d_concluida: st.markdown("🔀 **Orquestrador de Fluxogramas**")
        if st.session_state.fase0e_concluida: st.markdown("⚡ **Especialista em n8n**")
        if st.session_state.fase0f_concluida: st.markdown("🤖 **Engenheiro de Agentes & Skills**")
        if st.session_state.fase1_concluida:  st.markdown("👾 **Mestre dos Dados (JSON)**")
        if st.session_state.fase2_concluida:  st.markdown("⚡ **Engenheiro de Triagem**")
        if st.session_state.fase3_concluida:  st.markdown("🛡️ **Guardião Digital (Red Team)**")
        if st.session_state.fase4_concluida:  st.markdown("👑 **Especialista em Crises**")
        if st.session_state.fase4_concluida:  st.markdown("🏆 **Mestre em Gestão de Crises (Certificado)**")
            
        st.markdown("---")
        st.markdown("### ⚙️ Integração OpenRouter API (Opcional)")
        key_input = st.text_input(
            "Chave OpenRouter (sk-or-v1-...):",
            value=st.session_state.openrouter_key,
            type="password",
            help="Opcional. Permite usar modelos gratuitos na Fase 3."
        )
        if key_input != st.session_state.openrouter_key:
            st.session_state.openrouter_key = key_input
            
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚪 Sair", use_container_width=True):
                st.session_state.clear()
                st.rerun()
        with col_btn2:
            if st.button("🔄 Resetar Teste", help="Deleta o progresso salvo deste e-mail para testar os bloqueios de fase do zero", use_container_width=True):
                email = st.session_state.get("matricula")
                if email:
                    utils.deletar_progresso_estudante(email)
                st.session_state.clear()
                st.rerun()
    else:
        st.info("👋 Identifique-se na página inicial para começar a trilha.")

    st.markdown("---")
    with st.expander("📊 Painel do Instrutor (Baixar Acessos)", expanded=False):
        pass_adm = st.text_input("Senha de Acesso Instrutor:", type="password", key="pass_adm_input")
        if pass_adm.strip().lower() == "admin2026":
            csv_data = utils.obter_relatorio_acessos_csv()
            if csv_data:
                st.download_button(
                    "📥 Baixar Relatório de Participantes (CSV)",
                    data=csv_data,
                    file_name=f"participantes_ouvidoria_agil_{time.strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    type="primary",
                    use_container_width=True
                )
                st.caption("📋 Arquivo CSV contendo: Nome, E-mail, Data/Hora, XP e Fases Concluídas.")
            else:
                st.info("Nenhum participante registrado até o momento.")
        elif pass_adm:
            st.error("Senha incorreta.")

# --- VISTA DA PÁGINA INICIAL / LOGIN ---
def home_page_view():
    st.markdown("<div class='main-title'>🌧️ OPERAÇÃO OUVIDORIA ÁGIL</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Trilha Completa de Aprendizado: Do Básico ao Avançado com Exercícios Visuais</div>", unsafe_allow_html=True)
    
    # Mapa Mario Bros da Trilha
    st.markdown(utils.render_mario_map("HOME", st.session_state), unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        with st.container(border=True):
            st.subheader("📖 A Jornada do Aprendiz Moderno")
            st.markdown("""
            Bem-vindo à **Trilha Integrada de Programação em Inteligência Artificial Generativa e Automação Pública**!
            
            Você começará nos **Módulos de Nivelamento & Exercícios Visuais (Fases 0A a 0F)** e avançará para o **Simulado de Crise da Ouvidoria Ágil de Nova Esperança (Fases 1 a 4)**.
            
            📌 **MAPA DAS 10 FASES DE APRENDIZADO:**
            - **Fase 0A (Fundamentos):** Quiz de IA Generativa, Ética Pública ("Ethics by Design") e Parâmetros.
            - **Fase 0B (Prompting):** Construção de Prompts Estruturados no Padrão RTF/CRISP.
            - **Fase 0C (Estruturas):** Criação de Fichas Digitais em Python utilizando Listas e Dicionários.
            - **Fase 0D (Fluxogramas):** Construtor Visual de Diagramas e Orquestração de Agentes de IA.
            - **Fase 0E (n8n):** Simulador Visual de Workflows de Automação No-Code (Forms + IA + Sheets + Email).
            - **Fase 0F (Agentes & Skills):** Criador de Agentes Autônomos e Habilidades Modulares com YAML (`SKILL.md`).
            - **Fase 1 (Parsing JSON):** Extração semântica com trava anti-cola por Checksum de Matrícula.
            - **Fase 2 (Sandbox Python):** Algoritmo de Triagem em Lote testado contra 20 casos de estresse.
            - **Fase 3 (Red Teaming):** Arena de Batalha contra Injeções Hacker e Teste de Falso Positivo.
            - **Fase 4 (Gabinete Executivo):** Síntese estratégica em Markdown.
            - **Conclusão & Certificado:** Emissão do Certificado Oficial com Autenticação SHA-256!
            """)
            
            if mascote_img:
                st.image(mascote_img, caption="Ágil-Bot: Seu assistente na jornada de IA", width=320)
                
    with col2:
        with st.container(border=True):
            st.markdown("""
            <div class='mascote-box'>
                <div class='mascote-title'>🤖 Mensagem do Ágil-Bot</div>
                "Pronto para dominar a IA Generativa? Registre suas credenciais para gerar suas sementes de segurança e iniciar o Nivelamento na Fase 0A!"
            </div>
            """, unsafe_allow_html=True)
            
            if not st.session_state.logado:
                with st.form("login_form"):
                    nome_in = st.text_input("Nome Completo do Participante:")
                    email_in = st.text_input("E-mail do Participante:", placeholder="Ex: joao.silva@email.com", help="Seu e-mail será utilizado como semente individual para gerar seus dados e chaves únicas de desbloqueio.")
                    sub_login = st.form_submit_button("🚀 Acessar Trilha de Capacitação", type="primary")
                    
                    if sub_login:
                        clean_email = email_in.strip().lower()
                        if not nome_in.strip() or not clean_email:
                            st.error("Preencha o Nome Completo e o E-mail para acessar.")
                        elif "@" not in clean_email or "." not in clean_email or len(clean_email) < 5:
                            st.error("Por favor, informe um endereço de E-mail válido (ex: seu.nome@dominio.com).")
                        else:
                            st.session_state.nome = nome_in.strip()
                            st.session_state.matricula = clean_email
                            st.session_state.logado = True
                            restaurado = utils.carregar_progresso_estudante(clean_email, st.session_state)
                            utils.salvar_progresso_estudante(st.session_state)
                            if restaurado:
                                st.session_state.msg_boas_vindas = f"🎉 Bem-vindo de volta, {st.session_state.nome}! Seu progresso foi restaurado automaticamente."
                            else:
                                st.session_state.msg_boas_vindas = f"✅ Acesso autorizado! Bem-vindo(a), {nome_in}."
                            st.rerun()
            else:
                if st.session_state.get("msg_boas_vindas"):
                    st.success(st.session_state.msg_boas_vindas)
                else:
                    st.success(f"✅ Logado como: **{st.session_state.nome}** (E-mail: {st.session_state.matricula})")
                
                st.write("")
                st.caption("🧪 **Área de Testes do Instrutor:**")
                if st.button("🔄 Resetar Meu Progresso (Testar do Zero)", type="secondary", use_container_width=True, help="Deleta o progresso salvo deste e-mail para testar as travas do zero"):
                    email = st.session_state.get("matricula")
                    if email:
                        utils.deletar_progresso_estudante(email)
                    st.session_state.clear()
                    st.rerun()
                st.markdown("""
                **Como Progredir nas Fases:**
                1. Clique no botão abaixo para ir direto para a **Fase 0A: Fundamentos**.
                2. Ao concluir cada fase com sucesso, você receberá o **Código de Desbloqueio**.
                3. Utilize o botão **Avançar para a Próxima Fase** no final de cada nível!
                """)
                if st.button("🚀 Iniciar Trilha de Capacitação (Fase 0A)", type="primary", use_container_width=True):
                    st.switch_page("app_pages/0A_🧠_Fase_0A_Fundamentos.py")

# --- NAVEGAÇÃO MULTIPÁGINAS (st.navigation) ---
pages = {
    "Trilha Completa de Capacitação": [
        st.Page(home_page_view, title="Página Inicial / Login", icon=":material/login:", default=True),
        st.Page("app_pages/0A_🧠_Fase_0A_Fundamentos.py", title="Fase 0A: Fundamentos & Ética", icon=":material/psychology:"),
        st.Page("app_pages/0B_✍️_Fase_0B_Prompting.py", title="Fase 0B: Prompting RTF", icon=":material/edit_note:"),
        st.Page("app_pages/0C_🐍_Fase_0C_Estruturas.py", title="Fase 0C: Fichas Python", icon=":material/code:"),
        st.Page("app_pages/0D_🔀_Fase_0D_Fluxograma.py", title="Fase 0D: Fluxogramas IA", icon=":material/alt_route:"),
        st.Page("app_pages/0E_⚡_Fase_0E_n8n.py", title="Fase 0E: Simulador n8n", icon=":material/hub:"),
        st.Page("app_pages/0F_🤖_Fase_0F_Agentes.py", title="Fase 0F: Agentes & Skills", icon=":material/smart_toy:"),
        st.Page("app_pages/1_📂_Fase_1_Parsing.py", title="Fase 1: Parsing JSON", icon=":material/folder:"),
        st.Page("app_pages/2_⚡_Fase_2_Automacao.py", title="Fase 2: Automação & Risco", icon=":material/bolt:"),
        st.Page("app_pages/3_🛡️_Fase_3_RedTeaming.py", title="Fase 3: Red Teaming", icon=":material/shield:"),
        st.Page("app_pages/4_📊_Fase_4_Relatorio.py", title="Fase 4: Relatório Executivo", icon=":material/bar_chart:"),
        st.Page("app_pages/5_🏆_Certificado_Final.py", title="Conclusão & Certificado", icon=":material/emoji_events:")
    ]
}

pg = st.navigation(pages)
pg.run()
