import streamlit as st

# 1. INJEÇÃO DA METATAG PARA O GOOGLE ADSENSE (MANTIDA NO TOPO)
st.html('<meta name="google-adsense-account" content="ca-pub-3241373482970085">')

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Calculadora de Pace Pro", page_icon="🏃")

st.title("🏃 Calculadora de Pace e Tiros Pro")
st.subheader("Precisão total com minutos e segundos para seus treinos.")

# 3. ENTRADA DE DADOS: DISTÂNCIA E TEMPO (MINUTOS + SEGUNDOS)
st.write("---")
distancia = st.selectbox("Escolha a distância da prova (km):", [5, 10, 21, 42])

st.write("**Tempo total que você pretende fazer na prova:**")
col_min, col_seg = st.columns(2)
with col_min:
    t_min = st.number_input("Minutos:", min_value=0, value=25, step=1)
with col_seg:
    t_seg = st.number_input("Segundos:", min_value=0, max_value=59, value=0, step=1)

# Cálculo do tempo total em segundos para garantir a precisão
tempo_total_segundos = (t_min * 60) + t_seg

if st.button("Calcular Ritmo e Tiros"):
    # 4. CÁLCULO DO PACE (RITMO POR KM)
    pace_por_km_segundos = tempo_total_segundos / distancia
    minutos_pace = int(pace_por_km_segundos // 60)
    segundos_pace = int(pace_por_km_segundos % 60)
    
    st.success(f"🎯 Seu ritmo médio (Pace) deve ser de: **{minutos_pace}:{segundos_pace:02d} min/km**")

    # 5. CÁLCULO DE TIROS (INTENSIDADE 10% SUPERIOR AO PACE DE PROVA)
    st.write("---")
    st.header("🎯 Sugestão de Treino de Tiros")
    st.write("Estes tempos são calculados para serem 10% mais velozes que seu pace de prova:")
    
    # Pace de tiro é 10% mais rápido (fator 0.9)
    pace_tiro_seg_por_km = pace_por_km_segundos * 0.9

    tiros_config = {
        "100 metros": {"fator": 0.1, "qtd": "10 a 12", "pausa": "45 seg"},
        "400 metros": {"fator": 0.4, "qtd": "8 a 10", "pausa": "1 min 30 seg"},
        "800 metros": {"fator": 0.8, "qtd": "5 a 6", "pausa": "2 min"},
        "1000 metros": {"fator": 1.0, "qtd": "4 a 5", "pausa": "2 min 30 seg"}
    }

    for dist, info in tiros_config.items():
        # Calcula o tempo exato de cada tiro em segundos
        t_tiro_total_seg = pace_tiro_seg_por_km * info["fator"]
        m_tiro = int(t_tiro_total_seg // 60)
        s_tiro = int(t_tiro_total_seg % 60)
        
        with st.expander(f"Ver Detalhes: Tiros de {dist}"):
            st.write(f"⏱️ **Tempo do tiro:** {m_tiro:02d}:{s_tiro:02d}")
            st.write(f"🔢 **Quantidade:** {info['qtd']} repetições")
            st.write(f"⏳ **Pausa:** {info['pausa']}")

st.write("---")
st.info("💡 Com essa precisão, seu site agora oferece um cálculo de nível profissional para atletas.")
