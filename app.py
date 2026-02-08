import streamlit as st

# --- TRUQUE PARA O GOOGLE ENXERGAR O ADS.TXT ---
# Se o robô do Google perguntar pelo ads.txt, o site responde direto
query_params = st.query_params
if "ads.txt" in str(query_params) or "ads" in str(query_params):
    st.write("google.com, pub-3241373482970085, DIRECT, f08c47fec0942fa0")
    st.stop()
# ----------------------------------------------

st.set_page_config(page_title="Calculadora de Pace Pro", page_icon="🏃")

# Cabeçalho do Site
st.title("🏃 Calculadora de Pace e Performance")
st.write("Organize seus treinos e calcule seu ritmo para 5km, 10km e Maratonas.")

# Calculadora
distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21.1, 42.2])
tempo_total_min = st.number_input("Tempo total (minutos):", min_value=1, value=25)

if st.button("Calcular Ritmo"):
    pace_decimal = tempo_total_min / distancia
    minutos = int(pace_decimal)
    segundos = int((pace_decimal - minutos) * 60)
    st.success(f"Seu ritmo médio é de **{minutos}:{segundos:02d} min/km**")

# Conteúdo Extra (Isso ajuda o Google a aprovar o site)
st.divider()
st.header("Dicas para melhorar seu Pace")
st.write("1. Mantenha a constância nos treinos semanais.")
st.write("2. Faça exercícios de fortalecimento para evitar lesões.")
st.write("3. Use esta calculadora para planejar sua velocidade em provas.")
