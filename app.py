import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DO SITE
st.set_page_config(page_title="Calculadora de Pace Pro - BioScience", page_icon="🏃")

# 2. ADSENSE (Código para o rastreador validar sua conta)
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
    """,
    height=0,
)

# 3. MENU LATERAL PROFISSIONAL
st.sidebar.title("🏃 BioScience Run")
aba = st.sidebar.radio("Navegar por:", ["Calculadora de Performance", "Artigos Científicos", "Privacidade", "Contato"])

if aba == "Calculadora de Performance":
    st.title("🏃 Calculadora de Pace e Tiros Pro")
    st.write("Ferramenta de precisão para atletas e treinadores.")

    st.write("---")
    distancia = st.selectbox("Distância da prova (km):", [5, 10, 21, 42])

    st.write("**Tempo total pretendido:**")
    col_min, col_seg = st.columns(2)
    with col_min:
        t_min = st.number_input("Minutos:", min_value=0, value=25, step=1)
    with col_seg:
        t_seg = st.number_input("Segundos:", min_value=0, max_value=59, value=0, step=1)

    tempo_total_segundos = (t_min * 60) + t_seg

    if st.button("Calcular Planilha de Ritmo"):
        pace_por_km_segundos = tempo_total_segundos / distancia
        minutos_pace = int(pace_por_km_segundos // 60)
        segundos_pace = int(pace_por_km_segundos % 60)
        
        st.success(f"🎯 Pace de Prova: **{minutos_pace}:{segundos_pace:02d} min/km**")

        st.write("---")
        st.header("🎯 Sugestão de Treino de Tiros (Intervalado)")
        st.write("Tempos calculados para estímulo de limiar anaeróbico (10% mais veloz):")
        
        pace_tiro_seg_por_km = pace_por_km_segundos * 0.9
        tiros = {"100m": 0.1, "400m": 0.4, "800m": 0.8, "1000m": 1.0}

        for dist, fator in tiros.items():
            t_tiro_seg = pace_tiro_seg_por_km * fator
            st.write(f"⏱️ **Tiro de {dist}:** {int(t_tiro_seg//60):02d}:{int(t_tiro_seg%60):02d}")

elif aba == "Artigos Científicos":
    st.title("🔬 Fisiologia da Corrida")
    
    st.subheader("1. Treino de Tiros e o Limiar de Lactato")
    st.write("""
    Fisiologicamente, o treino de tiros (intervalado de alta intensidade) visa aumentar o seu **V02 Máximo** e a eficiência mitocondrial. 
    Ao correr acima do seu pace de prova, você recruta fibras musculares do tipo II (contração rápida) e treina seu organismo para remover o lactato 
    mais rapidamente do fluxo sanguíneo, adiando a fadiga muscular periférica.
    """)
    
    st.subheader("2. A Importância Biológica do Descanso")
    st.write("""
    O ganho de performance ocorre durante o descanso, não durante o treino. Este processo é conhecido como **Supercompensação**. 
    Após o estresse mecânico e oxidativo do exercício, o corpo inicia uma cascata hormonal e proteica para reparar as microlesões musculares. 
    Sem o descanso adequado, ocorre o aumento do cortisol basal, podendo levar ao *overtraining* e à queda do sistema imune.
    """)
    
    st.subheader("3. Rodagem Leve e Biogênese Mitocondrial")
    st.write("""
    Treinos de baixa intensidade (Zonas 1 e 2) promovem a capilarização muscular, aumentando a oferta de oxigênio para os tecidos 
    e otimizando a oxidação de lipídeos como fonte energética primária.
    """)

elif aba == "Privacidade":
    st.title("Política de Privacidade")
    st.write("""
    Esta ferramenta é de uso público e gratuito. Não armazenamos informações de saúde ou dados sensíveis. 
    Cookies podem ser utilizados pelo Google AdSense para personalização de anúncios.
    """)

elif aba == "Contato":
    st.title("Contato Técnico")
    st.write("Para consultorias ou suporte técnico sobre a ferramenta:")
    st.write("📧 Responsável: **Juarez Bruschi Junior - Biomédico**")

# 4. RODAPÉ DE AUTORIDADE
st.write("---")
st.caption("Desenvolvido por **Juarez Bruschi Junior** | Biomédico")
st.caption("BioScience Performance & Tecnologia © 2026")
