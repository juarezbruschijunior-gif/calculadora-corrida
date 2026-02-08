import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO PROFISSIONAL DA PÁGINA
st.set_page_config(page_title="Calculadora de Pace Pro", page_icon="🏃")

# 2. INJEÇÃO DO CÓDIGO DO ADSENSE (Para o rastreador encontrar sua conta)
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
    """,
    height=0,
)

# 3. MENU LATERAL (Aumenta a chance de aprovação no AdSense)
st.sidebar.title("Informações")
aba = st.sidebar.radio("Navegar:", ["Calculadora", "Política de Privacidade", "Contato"])

if aba == "Calculadora":
    st.title("🏃 Calculadora de Pace e Tiros Pro")
    st.subheader("Precisão total para seus treinos de corrida.")

    # ENTRADA DE DADOS
    st.write("---")
    distancia = st.selectbox("Escolha a distância da prova (km):", [5, 10, 21, 42])

    st.write("**Tempo total que você pretende fazer na prova:**")
    col_min, col_seg = st.columns(2)
    with col_min:
        t_min = st.number_input("Minutos:", min_value=0, value=25, step=1)
    with col_seg:
        t_seg = st.number_input("Segundos:", min_value=0, max_value=59, value=0, step=1)

    tempo_total_segundos = (t_min * 60) + t_seg

    if st.button("Calcular Ritmo e Tiros"):
        # CÁLCULO DO PACE
        pace_por_km_segundos = tempo_total_segundos / distancia
        minutos_pace = int(pace_por_km_segundos // 60)
        segundos_pace = int(pace_por_km_segundos % 60)
        
        st.success(f"🎯 Seu ritmo médio (Pace) deve ser de: **{minutos_pace}:{segundos_pace:02d} min/km**")

        # CÁLCULO DE TIROS (10% mais velozes)
        st.write("---")
        st.header("🎯 Sugestão de Treino de Tiros")
        
        pace_tiro_seg_por_km = pace_por_km_segundos * 0.9
        tiros_config = {
            "100m": 0.1, "400m": 0.4, "800m": 0.8, "1000m": 1.0
        }

        for dist_nome, fator in tiros_config.items():
            t_tiro_total_seg = pace_tiro_seg_por_km * fator
            m_tiro = int(t_tiro_total_seg // 60)
            s_tiro = int(t_tiro_total_seg % 60)
            st.write(f"⏱️ **{dist_nome}:** {m_tiro:02d}:{s_tiro:02d}")

elif aba == "Política de Privacidade":
    st.title("Política de Privacidade")
    st.write("""
    Esta calculadora não coleta nem armazena dados pessoais dos usuários. 
    Utilizamos o Google AdSense para exibir anúncios, que pode utilizar cookies para melhorar sua experiência.
    """)

elif aba == "Contato":
    st.title("Contato")
    st.write("Dúvidas ou sugestões sobre a calculadora?")
    st.write("📧 Responsável: Juarez Bruschi Junior")

# 4. RODAPÉ PROFISSIONAL (O toque final que você pediu)
st.write("---")
st.caption("Desenvolvido por **Juarez Bruschi Junior**")
st.caption("Ferramenta para cálculo de ritmo de corrida e performance. © 2026")
