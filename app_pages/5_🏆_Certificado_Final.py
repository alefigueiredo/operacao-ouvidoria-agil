import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Conclusão & Certificado Final - Ouvidoria Ágil", page_icon="🏆", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #F59E0B; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
    .cert-box {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border: 4px solid #F59E0B;
        border-radius: 16px;
        padding: 35px 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        text-align: center;
        margin-top: 20px;
    }
    .cert-title-text {
        font-size: 2.1rem;
        font-weight: 800;
        color: #F59E0B;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    .cert-sub-text {
        font-size: 1.1rem;
        color: #94A3B8;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 25px;
    }
    .cert-name-text {
        font-size: 2.4rem;
        font-weight: 800;
        color: #38BDF8;
        margin: 15px 0;
    }
    .cert-body-text {
        font-size: 1.1rem;
        color: #E2E8F0;
        line-height: 1.7;
        max-width: 750px;
        margin: 0 auto 25px auto;
    }
    .cert-hash-text {
        font-family: monospace;
        font-size: 0.9rem;
        color: #4ADE80;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação na página inicial (Login).")
    st.stop()

# Trava da Fase Final por conclusão da Fase 4
if not st.session_state.get("fase4_concluida", False):
    st.markdown("<div class='main-title'>🏆 CONCLUSÃO & CERTIFICADO OFICIAL</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA ETAPA FINAL ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para desbloquear a Emissão do Certificado Oficial de Conclusão, conclua primeiro o Relatório Executivo da <b>Fase 4</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

# --- CONTEÚDO DA TELA FINAL DE CONCLUSÃO ---
st.markdown("<div class='main-title'>🎓🏆 PARABÉNS! CONCLUSÃO DA TRILHA & CURSO</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>Participante: <b>{st.session_state.nome}</b> (ID / Matrícula: {st.session_state.matricula})</div>", unsafe_allow_html=True)

# Mapa Mario Final - Robozinho no Troféu 🏆
st.markdown(utils.render_mario_map("5", st.session_state), unsafe_allow_html=True)

# Mensagem do Mascote Ágil-Bot
st.markdown(utils.render_mascote_dica(
    f"Sensacional, {st.session_state.nome}! Você venceu todos os desafios, salvou a cidade de Nova Esperança e dominou a Engenharia de Prompts, Triagem em Python, Simulador n8n e Red Teaming!",
    "Seu Certificado Oficial de Conclusão foi gerado abaixo com Autenticação Digital SHA-256. Você pode imprimi-lo ou baixá-lo em HTML!"
), unsafe_allow_html=True)

# Placar de Pontuação Final
with st.container(border=True):
    st.subheader("⭐ Placar Final de Desempenho")
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("Pontuação de XP", "1000 / 1000 XP", "100% Concluído")
    col_s2.metric("Missões Concluídas", "10 de 10 Fases", "Nota Máxima")
    col_s3.metric("Status da Capacitação", "EXCELÊNCIA", "Aprovado")
    st.progress(1.0)

# Gerar Hash SHA-256 do Certificado
semente_cert = f"{st.session_state.nome}_{st.session_state.matricula}_EXCELENCIA_OUVIDORIA_AGIL_2026"
hash_cert = utils.gerar_hash_sha256(semente_cert)[:16].upper()

# Exibição Visual do Certificado Oficial na Tela
st.markdown(f'''<div class='cert-box'>
<div style='display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #334155; padding-bottom: 15px; margin-bottom: 20px;'>
<span style='font-size: 1.5rem; font-weight: bold; color: #38BDF8;'>🌧️ OPERAÇÃO OUVIDORIA ÁGIL</span>
<span style='font-size: 1.5rem;'>🤖</span>
</div>

<div class='cert-title-text'>🏆 CERTIFICADO DE EXCELÊNCIA EM GESTÃO DE CRISES</div>
<div class='cert-sub-text'>Operação Ouvidoria Ágil</div>

<div style='color: #CBD5E1; font-size: 1.1rem;'>Certificamos que</div>

<div class='cert-name-text'>{st.session_state.nome}</div>

<div class='cert-body-text'>
Concluiu com êxito a Trilha Integrada com <b>carga horária de 8 horas (8h)</b>, englobando todas as missões de engenharia de prompt de dados, triagem de matriz de risco com 20 casos e pegadinhas, segurança de IA contra 10 vetores de ataque hacker (Red Teaming) e síntese executiva de crises.
</div>

<div style='font-size: 0.95rem; font-weight: 700; color: #F59E0B; margin: 15px 0 20px 0;'>
⏱️ Carga Horária Total: 8 horas (8h)
</div>

<div class='cert-hash-text'>
Autenticação Digital SHA-256: <b>{hash_cert}</b>
</div>
</div>''', unsafe_allow_html=True)

st.write("")

# Botões de Exportação e Impressão Alinhados (Flexbox)
html_cert_completo = utils.gerar_certificado_oficial_html(st.session_state.nome, st.session_state.matricula, hash_cert)
nome_arquivo_cert = f"Certificado_Ouvidoria_Agil_{st.session_state.nome.replace(' ', '_')}.html"

st.components.v1.html(
    f"""
    <div style="display: flex; gap: 16px; width: 100%; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        <button onclick="baixarCertificado()" style="
            flex: 1;
            background: linear-gradient(135deg, #0EA5E9, #0284C7);
            color: white;
            border: none;
            padding: 13px 20px;
            font-size: 0.95rem;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            transition: opacity 0.2s;
        " onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">📥 Baixar Certificado Oficial (.html)</button>
        
        <button onclick="imprimirCertificado()" style="
            flex: 1;
            background: linear-gradient(135deg, #2563EB, #1D4ED8);
            color: white;
            border: none;
            padding: 13px 20px;
            font-size: 0.95rem;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            transition: opacity 0.2s;
        " onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">🖨️ Abrir Janela de Impressão / Exportar PDF</button>
    </div>

    <script>
    var certHtml = {repr(html_cert_completo)};

    function baixarCertificado() {{
        var blob = new Blob([certHtml], {{ type: "text/html;charset=utf-8" }});
        var link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = {repr(nome_arquivo_cert)};
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }}

    function imprimirCertificado() {{
        var win = window.open("", "_blank");
        win.document.write(certHtml);
        win.document.close();
        setTimeout(function() {{
            win.print();
        }}, 500);
    }}
    </script>
    """,
    height=65
)

st.write("")
st.markdown("---")
if st.button("🏁 Finalizar Capacitação & Encerrar Sessão 🚪", type="secondary", use_container_width=True):
    st.session_state.clear()
    st.rerun()
