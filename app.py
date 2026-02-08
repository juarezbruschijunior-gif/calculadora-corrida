import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DO SITE
st.set_page_config(page_title="Calculadora de Pace Pro", page_icon="🏃")

# 2. ADSENSE (Código para o rastreador validar sua conta)
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
    """,
    height=0,
)

# 3. MENU LATERAL PROFISSIONAL (Item essencial para aprovação no AdSense)
st.sidebar.title("Calculadora Pro")
aba = st.sidebar.radio("Selecione:", ["Calculadora", "Política de Privacidade", "Contato"])

if aba == "Calculadora":
    st.title("🏃 Calculadora de Pace e Tiros Pro")
    st.write("Calcule seu ritmo de prova com precisão de minutos e segundos.")

    st.write("---")
    distancia = st.selectbox("Distância da prova (km):", [5, 10, 21, 42])

    st.write("**Tempo total pretendido:**")
    col_min, col_seg = st.columns(2)
    with col_min:
        t_min = st.number_input("Minutos:", min_value=0, value=25, step=1)
    with col_seg:
        t_seg = st.number_input("Segundos:", min_value=0, max_value=59, value=0, step=1)

    tempo_total_segundos = (t_min * 60) + t_seg

    if st.button("Calcular Agora"):
        # CÁLCULO DO PACE
        pace_por_km_segundos = tempo_total_segundos / distancia
        minutos_pace = int(pace_por_km_segundos // 60)
        segundos_pace = int(pace_por_km_segundos % 60)
        
        st.success(f"🎯 Ritmo médio necessário: **{minutos_pace}:{segundos_pace:02d} min/km**")

        # TREINO DE TIROS
        st.write("---")
        st.header("🎯 Sugestão de Treino de Tiros")
        st.write("Intensidade 10% superior ao seu ritmo de prova:")
        
        pace_tiro_seg_por_km = pace_por_km_segundos * 0.9
        tiros = {"100m": 0.1, "400m": 0.4, "800m": 0.8, "1000m": 1.0}

        for dist, fator in tiros.items():
            t_tiro_seg = pace_tiro_seg_por_km * fator
            st.write(f"⏱️ **Tiro de {dist}:** {int(t_tiro_seg//60):02d}:{int(t_tiro_seg%60):02d}")

elif aba == "Política de Privacidade":
    st.title("Política de Privacidade")
    st.write("""
    Respeitamos sua privacidade. Esta ferramenta não armazena dados pessoais. 
    Anúncios são exibidos via Google AdSense para manter o serviço gratuito.
    """)

elif aba == "Contato":
    st.title("Contato")
    st.write("📧 Desenvolvedor: Juarez Bruschi Junior")
    st.write("Para sugestões sobre a calculadora, entre em contato.")

# 4. RODAPÉ DE AUTORIA (Confirmação de propriedade para o Google)
st.write("---")
st.caption("Desenvolvido por **Juarez Bruschi Junior**")
st.caption("Calculadora de Performance © 2026")
