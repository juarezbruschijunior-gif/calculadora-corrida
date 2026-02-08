import streamlit as st

# --- FUNÇÃO PARA O GOOGLE ADSENSE ENXERGAR O ADS.TXT ---
# Se o Google tentar acessar /ads.txt, ele verá o seu código
query_params = st.query_params
if "ads.txt" in str(query_params):
    st.write("google.com, pub-3241373482970085, DIRECT, f08c47fec0942fa0")
    st.stop()
# -------------------------------------------------------

st.set_page_config(page_title="Calculadora de Pace Pro", page_icon="🏃")

st.title("🏃 Calculadora de Pace e Performance")
st.write("Calcule seu ritmo de corrida e planeje seus treinos para 5km, 10km ou Maratona.")

# Campos da calculadora
distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21.1, 42.2])
tempo_total_min = st.number_input("Tempo total (minutos):", min_value=1, value=25)

if st.button("Calcular Ritmo"):
    pace_decimal = tempo_total_min / distancia
    minutos = int(pace_decimal)
    segundos = int((pace_decimal - minutos) * 60)
    st.success(f"Seu ritmo é de **{minutos}:{segundos:02d} min/km**")

st.divider()
st.header("O que é Pace?")
st.write("O pace é o tempo médio que você leva para percorrer 1km. É essencial para o controle de intensidade nos treinos.")
