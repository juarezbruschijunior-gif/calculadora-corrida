import streamlit as st

# Configuração da página para SEO
st.set_page_config(page_title="Calculadora de Ritmo - Performance 5km", page_icon="🏃‍♂️")

# Estilo para melhorar o visual
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Menu Lateral (Essencial para o AdSense aceitar a navegação)
st.sidebar.title("🏃‍♂️ Menu de Treino")
pagina = st.sidebar.radio("Navegar por:", ["Calculadora de Tiros", "Dicas de Performance", "Sobre o Especialista", "Privacidade"])

if pagina == "Calculadora de Tiros":
    st.title("🏃‍♂️ Calculadora de Ritmo para Tiros de 5km")
    st.write("Otimize seus treinos de velocidade com base no seu tempo objetivo.")
    
    col1, col2 = st.columns(2)
    with col1:
        distancia = st.selectbox("Distância do Tiro (metros):", [200, 400, 800, 1000])
    with col2:
        tempo_objetivo_min = st.number_input("Tempo alvo nos 5km (minutos):", min_value=15, max_value=60, value=25)

    if st.button("Calcular Ritmo"):
        # Cálculo simples de ritmo por tiro
        ritmo_por_metro = (tempo_objetivo_min * 60) / 5000
        tempo_tiro = ritmo_por_metro * distancia
        minutos = int(tempo_tiro // 60)
        segundos = int(tempo_tiro % 60)
        
        st.success(f"Para um 5km em {tempo_objetivo_min}min, seu tiro de {distancia}m deve ser de: **{minutos:02d}:{segundos:02d}**")
        st.info("Dica: Descanse o dobro do tempo do tiro entre as repetições.")

elif pagina == "Dicas de Performance":
    st.header("📚 Como melhorar seu tempo nos 5km")
    st.write("""
    1. **Treino de Intervalos (Tiros):** Melhora o VO2 máximo e a tolerância ao lactato.
    2. **Rodagens Leves:** Fortalecem a base aeróbica.
    3. **Fortalecimento:** Previne lesões e melhora a economia de corrida.
    """)

elif pagina == "Sobre o Especialista":
    st.header("👨‍🏫 Juarez Bruschi Junior")
    st.write("Professor e entusiasta da corrida de rua, focado em ajudar corredores a alcançarem seus primeiros 5km com saúde e técnica.")

elif pagina == "Privacidade":
    st.header("🔒 Política de Privacidade")
    st.write("Este site não coleta dados pessoais dos usuários. Os cálculos são processados localmente no seu navegador.")

# Assinatura Profissional (Ajuda na autoridade do site)
st.markdown("---")
st.markdown("<p style='text-align: center;'>Criado por Juarez Bruschi Junior - Especialista em Treino de Performance</p>", unsafe_allow_html=True)
