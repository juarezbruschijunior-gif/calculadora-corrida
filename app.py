import streamlit as st

st.set_page_config(page_title="Calculadora de Pace - Pro")

st.title("🏃 Calculadora de Pace e Performance")
st.markdown("Calcule seu ritmo médio para treinos de 5km, 10km ou Maratona.")

# Parte da Calculadora
distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21.1, 42.2])
tempo_total_min = st.number_input("Tempo total (em minutos):", min_value=1, value=25)

pace_decimal = tempo_total_min / distancia
pace_minutos = int(pace_decimal)
pace_segundos = int((pace_decimal - pace_minutos) * 60)

if st.button("Calcular meu Ritmo"):
    st.success(f"Seu Pace médio é de **{pace_minutos}:{pace_segundos:02d} min/km**")

# Conteúdo para o Google AdSense (SEO)
st.divider()
st.header("O que é Pace na corrida?")
st.write("O pace é o tempo que você leva para percorrer um quilômetro. É a medida principal para corredores de rua, pois ajuda a controlar o esforço durante provas de 5km ou maratonas.")

st.subheader("Dicas para baixar seu Pace nos 5km")
st.write("1. Treine intervalos: Corra tiros de 400m em velocidade alta.")
st.write("2. Fortalecimento: Pernas fortes garantem uma passada mais eficiente.")
st.write("3. Constância: Tente manter o mesmo ritmo do início ao fim da prova.")
