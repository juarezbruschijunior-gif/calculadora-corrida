import streamlit as st

# 1. INJEÇÃO DA METATAG PARA O GOOGLE ADSENSE (OBRIGATÓRIO PARA VERIFICAÇÃO)
st.html('<meta name="google-adsense-account" content="ca-pub-3241373482970085">')

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Calculadora de Pace e Tiros", page_icon="🏃")

st.title("🏃 Calculadora de Pace e Performance")
st.subheader("Organize seus treinos com precisão de minutos e segundos.")

# 3. CALCULADORA DE PACE (COM SEGUNDOS)
st.write("---")
col_input1, col_input2 = st.columns(2)

with col_input1:
    distancia = st.selectbox("Escolha a distância da prova (km):", [5, 10, 21, 42])

with col_input2:
    tempo_total = st.number_input("Tempo total desejado (minutos):", min_value=1, value=25)

if st.button("Calcular Ritmo"):
    # Cálculo preciso do Pace em segundos por km
    pace_total_segundos = (tempo_total * 60) / distancia
    minutos_pace = int(pace_total_segundos // 60)
    segundos_pace = int(pace_total_segundos % 60)
    
    st.success(f"Seu ritmo médio (Pace) deve ser de: **{minutos_pace}:{segundos_pace:02d} min/km**")

# 4. CALCULADORA DE TIROS (COM MINUTOS E SEGUNDOS)
st.write("---")
st.header("🎯 Sugestão de Treino de Tiros")
st.write("Calculado com intensidade de 10% acima do seu pace de prova:")

# Pace de tiro é 10% mais rápido (fator 0.9)
pace_tiro_segundos_por_km = ((tempo_total * 60) / distancia) * 0.9

tiros_config = {
    "100 metros": {"fator": 0.1, "qtd": "10 a 12", "pausa": "45 seg"},
    "400 metros": {"fator": 0.4, "qtd": "8 a 10", "pausa": "1 min 30 seg"},
    "800 metros": {"fator": 0.8, "qtd": "5 a 6", "pausa": "2 min"},
    "1000 metros": {"fator": 1.0, "qtd": "4 a 5", "pausa": "2 min 30 seg"}
}

for dist, info in tiros_config.items():
    # Calcula o tempo do tiro em segundos
    tempo_tiro_total_seg = pace_tiro_segundos_por_km * info["fator"]
    m_tiro = int(tempo_tiro_total_seg // 60)
    s_tiro = int(tempo_tiro_total_seg % 60)
    
    with st.expander(f"Ver detalhes: Tiros de {dist}"):
        st.write(f"⏱️ **Tempo do tiro:** {m_tiro:02d}:{s_tiro:02d}")
        st.write(f"🔢 **Quantidade:** {info['qtd']} repetições")
        st.write(f"⏳ **Pausa:** {info['pausa']}")

st.write("---")
st.info("Dica: Os segundos são fundamentais para ajustar seu esforço nos treinos de tiro.")
