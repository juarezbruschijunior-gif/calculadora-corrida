import streamlit as st

# 1. Configurações de SEO e Título Profissional
st.set_page_config(page_title="Portal do Corredor - Performance 5km", page_icon="🏃‍♂️")

# 2. Estilo Visual (Clean e Profissional)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { background-color: #1a73e8; color: white; border-radius: 5px; }
    h1 { color: #1a73e8; }
    </style>
    """, unsafe_allow_html=True)

# 3. Menu de Navegação (Essencial para o AdSense)
st.sidebar.title("🧭 Navegação")
menu = st.sidebar.radio("Ir para:", ["Calculadora de Ritmo", "Artigos de Treino", "Sobre o Autor", "Privacidade"])

if menu == "Calculadora de Ritmo":
    st.title("🏃‍♂️ Calculadora de Ritmo para Provas de 5km")
    st.write("Utilize nossa ferramenta para planejar seus tiros de treino com precisão científica.")
    
    col1, col2 = st.columns(2)
    with col1:
        dist = st.selectbox("Distância do Tiro (metros):", [200, 400, 800, 1000])
    with col2:
        tempo_alvo = st.number_input("Tempo alvo nos 5km (minutos):", min_value=15, value=25)

    if st.button("Calcular Tempo do Tiro"):
        ritmo_total_seg = tempo_alvo * 60
        tempo_tiro = (ritmo_total_seg / 5000) * dist
        minutos = int(tempo_tiro // 60)
        segundos = int(tempo_tiro % 60)
        st.success(f"Seu tempo para o tiro de {dist}m deve ser: **{minutos:02d}:{segundos:02d}**")

elif menu == "Artigos de Treino":
    st.title("📚 Dicas e Conteúdo Educativo")
    st.subheader("Como melhorar seu ritmo nos 5km")
    st.write("""
    Para o Google AdSense aprovar seu site, ele precisa de texto informativo. 
    Aqui estão 3 pilares para baixar seu tempo:
    1. **Treino Intervalado:** Fazer tiros curtos aumenta sua capacidade cardiovascular.
    2. **Recuperação Ativa:** Dias de descanso são tão importantes quanto os dias de treino.
    3. **Volume Semanal:** Aumente sua quilometragem gradualmente (regra dos 10%).
    """)

elif menu == "Sobre o Autor":
    st.title("👨‍🏫 Sobre o Especialista")
    st.write("Juarez Bruschi Junior é professor e entusiasta da corrida, focado em democratizar o acesso a planilhas de performance.")

elif menu == "Privacidade":
    st.title("🔒 Política de Privacidade")
    st.write("Este site utiliza ferramentas de análise e exibe anúncios via Google AdSense. Não coletamos dados sensíveis dos usuários.")

# 4. Rodapé com Copyright e Assinatura
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Portal do Corredor - Juarez Bruschi Junior. Todos os direitos reservados.</p>", unsafe_allow_html=True)
