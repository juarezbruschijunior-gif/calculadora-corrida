import streamlit as st

# 1. INJEÇÃO DA METATAG PARA O GOOGLE ADSENSE (ESSENCIAL PARA VERIFICAÇÃO)
st.html('<meta name="google-adsense-account" content="ca-pub-3241373482970085">')

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Calculadora de Pace e Tiros", page_icon="🏃")

st.title("🏃 Calculadora de Pace e Performance")
st.subheader("Organize seus treinos e calcule seu ritmo para 5km, 10km e Maratonas.")

# 3. CALCULADORA DE PACE
st.write("---")
col_input1, col_input2 = st.columns(2)

with col_input1:
    distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21, 42])

with col_input2:
    tempo_total = st.number_input("Tempo total desejado (minutos):", min_value=1, value=25)

if st.button("Calcular Ritmo"):
    pace_decimal = tempo_total / distancia
    minutos = int(pace_decimal)
    segundos = int((pace_decimal - minutos) * 60)
    st.success(f"Seu ritmo médio (Pace) deve ser de: **{minutos}:{segundos:02d} min/km**")

# 4. CALCULADORA DE TIROS (SUGESTÕES DE TREINO)
st.write("---")
st.header("🎯 Sugestão de Treino de Tiros")
st.write("Estes tempos são calculados para serem 10% mais rápidos que seu pace de prova:")

# Cálculo do pace de tiro (10% mais rápido que o pace nominal)
pace_tiro_segundos = (tempo_total / distancia) * 0.9 * 60

tiros_config = {
    "100m": {"fator": 0.1, "qtd": "10 a 12", "pausa": "45 seg"},
    "400m": {"fator": 0.4, "qtd": "8 a 10", "pausa": "1 min 30 seg"},
    "800m": {"fator": 0.8, "qtd": "5 a 6", "pausa": "2 min"},
    "1000m": {"fator": 1.0, "qtd": "4 a 5", "pausa": "2 min 30 seg"}
}

for dist, info in tiros_config.items():
    tempo_tiro = pace_tiro_segundos * info["fator"]
    m_tiro = int(tempo_tiro // 60)
    s_tiro = int(tempo_tiro % 60)
    
    with st.expander(f"Tiros de {dist}"):
        st.write(f"⏱️ **Tempo do tiro:** {m_tiro:02d}:{s_tiro:02d}")
        st.write(f"🔢 **Quantidade sugerida:** {info['qtd']} repetições")
        st.write(f"⏳ **Pausa entre tiros:** {info['pausa']}")

st.write("---")
st.info("Dica: Realize um aquecimento de 10 a 15 minutos antes de iniciar os tiros.")
