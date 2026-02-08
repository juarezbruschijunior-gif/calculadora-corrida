import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA E METATAG DO ADSENSE
st.set_page_config(page_title="Calculadora de Pace e Tiros", page_icon="🏃")

# Injeção da Metatag para o Google AdSense (O que você copiou)
st.markdown(
    f'<head><meta name="google-adsense-account" content="ca-pub-3241373482970085"></head>',
    unsafe_allow_html=True
)

st.title("🏃 Calculadora de Pace e Performance")
st.subheader("Organize seus treinos e calcule seu ritmo.")

# 2. CALCULADORA DE PACE TRADICIONAL
st.write("---")
distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21, 42])
tempo_total = st.number_input("Tempo total desejado (minutos):", min_value=1, value=25)

if st.button("Calcular Ritmo"):
    pace = tempo_total / distancia
    st.success(f"Seu ritmo médio (Pace) deve ser de: **{pace:.2f} min/km**")

# 3. CALCULADORA DE TIROS (NOVIDADE)
st.write("---")
st.header("🎯 Calculadora de Treino de Tiros")
st.write("Baseado no seu tempo total desejado acima, aqui estão as sugestões de tiros:")

# Lógica simples de cálculo para os tiros (estimativa de intensidade)
pace_tiro = (tempo_total / distancia) * 0.9  # Tiros costumam ser 10% mais rápidos que o pace de prova

tiros = {
    "100m": {"dist": 0.1, "qtd": "10 a 12", "pausa": "45 seg"},
    "400m": {"dist": 0.4, "qtd": "8 a 10", "pausa": "1 min 30 seg"},
    "800m": {"dist": 0.8, "qtd": "5 a 6", "pausa": "2 min"},
    "1000m": {"dist": 1.0, "qtd": "4 a 5", "pausa": "2 min 30 seg"}
}

col1, col2 = st.columns(2)

for dist_nome, info in tiros.items():
    tempo_tiro_seg = pace_tiro * info["dist"] * 60
    minutos = int(tempo_tiro_seg // 60)
    segundos = int(tempo_tiro_seg % 60)
    
    with st.expander(f"Tiros de {dist_nome}"):
        st.write(f"**Tempo do tiro:** {minutos:02d}:{segundos:02d}")
        st.write(f"**Quantidade:** {info['qtd']} vezes")
        st.write(f"**Pausa:** {info['pausa']} (descanso ativo/parado)")

st.write("---")
st.write("💡 *Dica: Use os tiros para ganhar velocidade e explosão nos seus treinos.*")
