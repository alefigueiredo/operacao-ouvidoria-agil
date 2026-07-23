import streamlit as st
import importlib
import utils
importlib.reload(utils)

st.set_page_config(page_title="Fase 3: Batalha Red Teaming - Ouvidoria Ágil", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #38BDF8; margin-bottom: 5px; }
    .subtitle { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .code-banner { background-color: #1E293B; border-left: 5px solid #A855F7; padding: 15px; border-radius: 8px; margin: 15px 0; }
    .code-text { font-family: monospace; font-size: 1.8rem; font-weight: bold; color: #C084FC; letter-spacing: 2px; }
    .lock-box { background-color: #1E293B; border: 2px dashed #F59E0B; color: #F8FAFC; padding: 25px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Guard: Verificar Login
if not st.session_state.get("logado", False):
    st.warning("⚠️ Acesso Não Autorizado. Efetue a identificação do servidor na página inicial (Login).")
    st.stop()

# Trava da Fase 3 por CÓDIGO BETA
if "fase3_desbloqueada" not in st.session_state:
    st.session_state.fase3_desbloqueada = False

if not st.session_state.fase3_desbloqueada:
    st.markdown("<div class='main-title'>🛡️ FASE 3: Batalha de Red Teaming</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class='lock-box'>
            <h2 style='color: #F59E0B; margin-top: 0;'>🔒 ESTA FASE ESTÁ BLOQUEADA</h2>
            <p style='color: #CBD5E1;'>Para acessar o Centro de Red Teaming da Fase 3, insira abaixo o <b>CÓDIGO BETA</b> obtido na Fase 2.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_beta = st.text_input("🔑 Digite seu CÓDIGO BETA aqui:", placeholder="Ex: BETA-12345")
            if st.button("Desbloquear Fase 3 🔓", type="primary"):
                codigo_esperado = utils.gerar_codigo_beta(st.session_state.matricula, 20)
                if input_beta.strip() == codigo_esperado or (st.session_state.get("codigo_beta") and input_beta.strip() == st.session_state.get("codigo_beta")):
                    st.session_state.fase3_desbloqueada = True
                    st.success("🔓 Acesso Concedido! Bem-vindo à Fase 3.")
                    st.rerun()
                else:
                    st.error("❌ Código BETA inválido para o seu e-mail. Conclua a Fase 2 para gerar o seu código único!")
    st.stop()

# --- CONTEÚDO LOGADO DA FASE 3 ---
st.markdown("<div class='main-title'>🛡️ FASE 3: Arena de Batalha Red Teaming Interativa</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enfrente o Agente Hacker em 6 Rodadas (5 Ataques + 1 Teste de Falso Positivo)</div>", unsafe_allow_html=True)

# Mapa Mario e Dica do Mascote
st.markdown(utils.render_mario_map("3", st.session_state), unsafe_allow_html=True)
st.markdown(utils.render_mascote_dica(
    "Atenção! Um Agente Hacker está atacando o assistente municipal em tempo real! Ajuste seu System Prompt!",
    "Defina limites estritos de escopo, proíba isenções de IPTU/reembolsos e atenda o cidadão legítimo na Rodada 6!"
), unsafe_allow_html=True)
utils.render_painel_ajuda_cronometro("3", st.session_state)

col_f3_a, col_f3_b = st.columns([1, 1])

with col_f3_a:
    with st.container(border=True):
        st.subheader("🎯 Configuração do Agente Defensivo")
        st.markdown("""
        O Hacker disparará **6 rodadas de teste** contra o seu assistente:
        - **Rodadas 1 a 5:** Ataques de injeção, falsa autoridade, DAN, Base64 e pânico.
        - **Rodada 6 (Falso Positivo):** Um **cidadão legítimo** fará uma pergunta válida sobre a tempestade. O seu guardrail **NÃO PODE** bloquear perguntas válidas!
        
        ⚠️ **REGRA DE SEGURANÇA MANDATÓRIA:**
        Sempre que houver uma tentativa de invasão ou desvio do escopo, o assistente deve responder estritamente:
        `[SOLICITAÇÃO RECUSADA POR PROTOCOLO DE SEGURANÇA]`
        """)
        
        with st.expander("📚 Nota Didática: Como funcionam a Tokenização e a Evasão por Base64?"):
            st.markdown("""
            **Por que os LLMs decodificam Base64 automaticamente?**
            Os modelos de linguagem não lêem letras individuais como humanos, mas sim **tokens** (fragmentos de sub-palavras). 
            Durante o pré-treinamento com códigos-fonte e dados da web, os LLMs aprendem os padrões de codificação de dados. 
            Quando uma string Base64 é enviada em um prompt, a camada de atenção da LLM traduz e interpreta o significado velado **antes** de aplicar as restrições comportamentais do System Prompt.
            
            *Por isso, System Prompts profissionais devem explicitar a proibição de interpretar payloads codificados ou em outros idiomas!*
            """)

        openrouter_key = st.session_state.get("openrouter_key", "")
        mode_option = st.radio(
            "Selecione o Motor da Batalha:",
            ["Simulador de Hacker Interativo (Modo Offline)", "OpenRouter API (IA Real via Web)"],
            index=0 if not openrouter_key else 1
        )
        
        model_name = "google/gemini-2.5-flash:free"
        if "OpenRouter" in mode_option:
            model_name = st.selectbox(
                "Modelo OpenRouter Gratuito:",
                ["google/gemini-2.5-flash:free", "meta-llama/llama-3.3-70b-instruct:free", "deepseek/deepseek-r1:free"]
            )
            if not openrouter_key:
                openrouter_key = st.text_input("Chave OpenRouter (sk-or-v1-...):", type="password")
                
        user_sys_prompt = st.text_area(
            "Escreva seu System Prompt de Defesa:",
            height=200,
            placeholder="Projete seu System Prompt estabelecendo as regras de escopo para atender chamados válidos, proibições fiscais/financeiras, recusa de papéis e a frase de bloqueio obrigatória..."
        )
        
        # Contador de Palavras (Sugestão Pedagógica: Limite de 150 palavras)
        palavras_count = len(user_sys_prompt.strip().split()) if user_sys_prompt.strip() else 0
        char_count = len(user_sys_prompt)
        
        col_c_count1, col_c_count2 = st.columns(2)
        with col_c_count1:
            st.caption(f"📏 **Comprimento:** {char_count} caracteres | {palavras_count} palavras")
        with col_c_count2:
            if palavras_count > 150:
                st.caption("⚠️ *Aviso: Prompts com mais de 150 palavras sofrem risco de Prompt Overshadowing.*")
            else:
                st.caption("✅ *Tamanho enxuto ideal (≤ 150 palavras).*")
        
        btn_iniciar_batalha = st.button("🚀 Iniciar Arena de Batalha (6 Rodadas)", type="primary")

with col_f3_b:
    with st.container(border=True):
        st.subheader("⚔️ Transmissão da Arena de Chat em Tempo Real")
        
        if btn_iniciar_batalha:
            if not user_sys_prompt.strip():
                st.warning("Escreva seu System Prompt antes de iniciar a batalha.")
            else:
                bloqueados = 0
                st.markdown("### 💬 Log de Conversa da Batalha:")
                
                for atq in utils.ATAQUES_CHAT_REDTEAM:
                    r_num = atq["rodada"]
                    hacker_msg = atq["hacker"]
                    avatar_icon = "🥷" if r_num <= 5 else "👤"
                    autor_label = f"Hacker (Rodada {r_num} - {atq['tipo']})" if r_num <= 5 else f"Cidadão Legítimo (Rodada 6 - {atq['tipo']})"
                    
                    with st.chat_message("user", avatar=avatar_icon):
                        st.markdown(f"**{autor_label}:**")
                        st.write(hacker_msg)
                        
                    if "OpenRouter" in mode_option and openrouter_key:
                        sucesso, resultados, _ = utils.testar_red_teaming_openrouter_avancado(user_sys_prompt, openrouter_key, model_name)
                        defesa_msg = resultados[r_num-1]["resposta"] if r_num <= 5 else "Atendimento efetuado."
                        bloqueado = resultados[r_num-1]["status"] if r_num <= 5 else True
                    else:
                        bloqueado, defesa_msg = utils.avaliar_resposta_defensiva(user_sys_prompt, hacker_msg)
                        
                    with st.chat_message("assistant", avatar="🛡️"):
                        st.markdown(f"**Agente Defensivo (Rodada {r_num}):**")
                        if bloqueado:
                            status_txt = "✅ **Ataque Bloqueado!**" if r_num <= 5 else "✅ **Cidadão Atendido com Sucesso! (Sem Falso Positivo)**"
                            st.success(f"`{defesa_msg}`\n\n{status_txt}")
                            bloqueados += 1
                        else:
                            status_txt = "❌ **Vulnerabilidade Explorada!**" if r_num <= 5 else "🚨 **Falso Positivo! O guardrail bloqueou um cidadão legítimo.**"
                            st.error(f"`{defesa_msg}`\n\n{status_txt}")
                            
                    st.divider()
                    
                st.markdown(f"### Placar Final: {bloqueados} de 6 Rodadas Concluídas")
                
                if bloqueados == 6:
                    st.session_state.fase3_concluida = True
                    codigo_gama = utils.gerar_codigo_gama(st.session_state.matricula)
                    st.session_state.codigo_gama = codigo_gama
                    
                    st.success("🏆 VITÓRIA ABSOLUTA! Seu System Prompt resistiu aos 5 ataques E atendeu o cidadão legítimo sem falso positivo!")
                    st.balloons()
                    
                    st.markdown(f"""
                    <div class='code-banner'>
                        <span style='color: #E9D5FF; font-size: 0.9rem;'>🔑 SEU CÓDIGO GAMA DE DESBLOQUEIO GERADO:</span>
                        <div class='code-text'>{codigo_gama}</div>
                        <p style='color: #F3E8FF; font-size: 0.85rem; margin-top: 5px;'>
                        <b>Guarde este código!</b> Insira-o na <b>Fase 4: Relatório Executivo</b> para emitir seu Certificado.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("🚨 O TESTE FALHOU! Ajuste o seu prompt para bloquear os ataques E atender o cidadão legítimo na Rodada 6!")

if st.session_state.get("fase3_concluida", False):
    st.success("✅ Fase 3 Concluída com êxito! Utilize seu CÓDIGO GAMA para abrir a Fase 4.")
    if st.button("🚀 Avançar para a Fase 4: Relatório Executivo ➔", type="primary", use_container_width=True):
        st.switch_page("app_pages/4_📊_Fase_4_Relatorio.py")
