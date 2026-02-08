import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Calculadora de Pace - Pro")

# --- INJEÇÃO DO CÓDIGO ADSENSE ---
# Usamos um componente de HTML para forçar o Google a ler o script na página
adsense_script = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
"""
components.html(adsense_script, height=0)
# ---------------------------------

st.title("🏃 Calculadora de Pace e Performance")
st.markdown("Calcule seu ritmo médio para treinos de 5km, 10km ou Maratona.")

# Parte da Calculadora
distancia = st.selectbox("Escolha a distância (km):", [5, 10, 21.1, 42.2])
tempo_total_min = st.number_input("Tempo total (em minutos):", min_value=1, value=25)

if st.button("Calcular meu Ritmo"):
    pace_decimal = tempo_total_min / distancia
    pace_minutos = int(pace_decimal)
    pace_segundos = int((pace_decimal - pace_minutos) * 60)
    st.success(f"Seu Pace médio é de **{pace_minutos}:{pace_segundos:02d} min/km**")

# Conteúdo obrigatório para o Google aprovar (SEO)
st.divider()
st.header("O que é o Pace na corrida?")
st.write("O pace é o indicador que mostra quantos minutos você leva para completar cada quilômetro.")
st.write("Controlar o seu pace é a melhor forma de evoluir na corrida sem se lesionar.")


