import streamlit as st
import streamlit.components.v1 as components

# Inserindo o código de verificação do Google AdSense
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

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

# Conteúdo para o Google (Essencial para aprovação do AdSense)
st.divider()
st.header("O que é o Pace na corrida?")
st.write("O pace é o tempo que você leva para percorrer um quilômetro. Ele é fundamental para corredores que buscam manter a constância e melhorar a performance em provas de rua.")

st.subheader("Dicas para baixar seu tempo")
st.write("Para melhorar seu ritmo, é importante intercalar treinos de rodagem leve com treinos de tiro e fortalecimento muscular.")

