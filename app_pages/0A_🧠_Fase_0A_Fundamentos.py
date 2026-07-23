import streamlit as st
import importlib
import random
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 0A: Fundamentos & Ética em IA - Ouvidoria Ágil", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #38BDF8; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #38BDF8; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

st.markdown("<div class='main-title'>🧠 FASE 0A: Fundamentos da IA Generativa & Ética no Setor Público</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>Módulo de Nivelamento — Servidor Operador: <b>{st.session_state.nome}</b> (Matrícula / ID: {st.session_state.matricula})</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("0A", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Bem-vindo à primeira etapa da nossa jornada! IAs Discriminativas classificam rótulos, enquanto Generativas criam conteúdos autorregressivamente.",
    "No serviço público, a diretriz essencial é sempre 'Ethics by Design'! O formulário abaixo é personalizado e embaralhado para sua matrícula."
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("0A", st.session_state)

with st.container(border=True):
    st.subheader("📚 Desafio Teórico de Nivelamento (Semente Individual por Matrícula)")
    st.markdown("""
    Valide seus conhecimentos nos conceitos centrais de Inteligência Artificial Generativa, Parâmetros e Ética Pública. 
    *Nota: A ordem das perguntas e das alternativas é aleatorizada exclusivamente para a sua matrícula para garantir a integridade da avaliação.*
    """)

# Gerar semente matemática individual baseada no e-mail / matrícula
seed_val = utils.calcular_matricula_int(st.session_state.matricula)
rng = random.Random(seed_val)

QUESTOES_BASE = [
    {
        "id": "q1",
        "pergunta": "Qual é a diferença fundamental entre Machine Learning Tradicional (Discriminativo) e IA Generativa?",
        "correta": "Discriminativos classificam e preveem rótulos; Generativos criam novos conteúdos autorregressivamente (texto, imagem, código).",
        "incorretas": [
            "Discriminativos criam textos sintéticos; Generativos apenas organizam tabelas e bancos de dados relacionais.",
            "Discriminativos não requerem dados de treino; Generativos funcionam exclusivamente através de regras manuais 'if/else'."
        ]
    },
    {
        "id": "q2",
        "pergunta": "No estudo de caso do RH em que a IA passou a excluir candidatos acima de 50 anos e de bairros periféricos, qual foi a causa raiz do viés?",
        "correta": "Fine-Tuning com dados históricos viciados da própria empresa que refletiam contratações passadas excludentes.",
        "incorretas": [
            "Pre-training básico da internet que deliberadamente bloqueou candidatos de certas regiões geográficas.",
            "Falha mecânica nos chips de processamento da nuvem que alterou aleatoriamente os resultados dos testes."
        ]
    },
    {
        "id": "q3",
        "pergunta": "Qual é a abordagem metodológica recomendada para incorporação de ética e responsabilidade no ciclo de vida de IAs no serviço público?",
        "correta": "Ethics by Design (incorporar regras éticas, transparência e segurança em todas as fases do ciclo de vida da IA).",
        "incorretas": [
            "Ethics by Reactivity (aguardar incidentes públicos para criar regras retroativas sem testes prévios de segurança).",
            "Ethics by Delegation (transferir toda a responsabilidade de decisões administrativas para o algoritmo sem supervisão)."
        ]
    },
    {
        "id": "q4",
        "pergunta": "Como os parâmetros `Temperatura` e `Top-P` influenciam a geração de texto dos LLMs?",
        "correta": "Temperatura controla a aleatoriedade/criatividade; Top-P (Nucleus Sampling) filtra a probabilidade acumulada dos tokens.",
        "incorretas": [
            "Temperatura ajusta a velocidade do processador; Top-P limita a quantidade máxima de caracteres por palavra do texto.",
            "Temperatura zera o contexto da conversa; Top-P converte automaticamente a saída do modelo para outros idiomas."
        ]
    }
]

# Embaralhar ordem de opções e perguntas individualmente por matrícula
questoes_shuffled = []
for q in QUESTOES_BASE:
    opcoes = [q["correta"]] + list(q["incorretas"])
    rng.shuffle(opcoes)
    questoes_shuffled.append({
        "id": q["id"],
        "pergunta": q["pergunta"],
        "opcoes": opcoes
    })

rng.shuffle(questoes_shuffled)

respostas = {}
with st.form("quiz_fase0a"):
    for idx, item in enumerate(questoes_shuffled, start=1):
        st.markdown(f"#### Questão {idx}: {item['pergunta']}")
        respostas[item['id']] = st.radio(
            item['pergunta'],
            item['opcoes'],
            index=None,
            key=f"f0a_{item['id']}",
            label_visibility="collapsed"
        )
        st.write("")
    
    sub_quiz = st.form_submit_button("Validar Respostas do Quiz ⚙️", type="primary")

if sub_quiz:
    ans_q1 = respostas.get("q1")
    ans_q2 = respostas.get("q2")
    ans_q3 = respostas.get("q3")
    ans_q4 = respostas.get("q4")

    if ans_q1 is None or ans_q2 is None or ans_q3 is None or ans_q4 is None:
        st.warning("⚠️ Marque uma alternativa para cada uma das 4 questões antes de submeter!")
    else:
        sucesso, msg = utils.validar_quiz_fase0a(ans_q1, ans_q2, ans_q3, ans_q4)
        
        if sucesso:
            st.session_state.fase0a_concluida = True
            codigo_0a = utils.gerar_codigo_zero_a(st.session_state.matricula)
            st.session_state.codigo_0a = codigo_0a
            
            st.success(f"✨ {msg}")
            st.balloons()
            
            st.markdown(f"""
            <div class='code-banner'>
                <span style='color: #94A3B8; font-size: 0.9rem;'>🔑 SEU CÓDIGO NÍVEL-0A DE DESBLOQUEIO GERADO:</span>
                <div class='code-text'>{codigo_0a}</div>
                <p style='color: #E2E8F0; font-size: 0.85rem; margin-top: 5px;'>
                <b>Copie este código!</b> Insira-o na <b>Fase 0B: Prompting Estruturado</b> no menu lateral.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(msg)

if st.session_state.get("fase0a_concluida", False):
    st.success("✅ Fase 0A Concluída! Utilize seu CÓDIGO NÍVEL-0A para abrir a Fase 0B.")
    if st.button("🚀 Avançar para a Fase 0B: Prompting RTF ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/0B_✍️_Fase_0B_Prompting.py")
