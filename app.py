import streamlit as st

st.set_page_config(page_title="Pace Pro - Treinamento Avançado", page_icon="🏃‍♂️", layout="wide")

# Estilização Premium
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stNumberInput, .stSelectbox { border-radius: 10px; }
    .card {
        padding: 25px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border-top: 5px solid #007BFF;
    }
    .result-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        text-align: center;
    }
    .highlight { color: #007BFF; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏃‍♂️ Planejador de Performance Pace Pro")
st.markdown("---")

# --- ÁREA DA CALCULADORA ---
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1.5, 2, 2])

with col1:
    st.subheader("📋 Parâmetros da Prova")
    distancia = st.selectbox("Objetivo de Prova (km):", [5, 10, 21, 42], index=0)
    minutos = st.number_input("Minutos pretendidos:", min_value=1, value=25)
    segundos = st.number_input("Segundos pretendidos:", min_value=0, max_value=59, value=0)
    
    tempo_total_seg = (minutos * 60) + segundos
    ritmo_base = tempo_total_seg / distancia # seg/km

with col2:
    st.subheader("⏱️ Guia de Ritmos (Paces)")
    
    # Lógica de Fisiologia para Paces
    pace_tiro = ritmo_base * 0.92  # 8% mais rápido
    pace_tempo = ritmo_base * 1.10 # 10% mais lento
    pace_rodagem = ritmo_base * 1.25 # 25% mais lento

    def format_pace(seg):
        m, s = divmod(int(seg), 60)
        return f"{m}:{s:02d}"

    st.write(f"🚀 **Tiros (V02 Máx):** {format_pace(pace_tiro)} min/km")
    st.write(f"⚡ **Tempo Run (Limiar):** {format_pace(pace_tempo)} min/km")
    st.write(f"🐢 **Rodagem (Base):** {format_pace(pace_rodagem)} min/km")

with col3:
    st.subheader("🎯 Prescrição de Tiros")
    
    # Definindo volume e pausa por distância
    if distancia == 5:
        qtd, dist_tiro, pausa = 10, "400m", "90 seg"
        tempo_tiro = pace_tiro * 0.4
    elif distancia == 10:
        qtd, dist_tiro, pausa = 6, "800m", "2 min"
        tempo_tiro = pace_tiro * 0.8
    elif distancia == 21:
        qtd, dist_tiro, pausa = 5, "1000m", "2:30 min"
        tempo_tiro = pace_tiro
    else: # 42k
        qtd, dist_tiro, pausa = 8, "1000m", "2 min"
        tempo_tiro = pace_tiro

    st.markdown(f"""
    <div class="result-box">
        <p>Sugerido para seu nível:</p>
        <h2 style="color:#007BFF;">{qtd}x {dist_tiro}</h2>
        <p>Tempo por tiro: <b>{format_pace(tempo_tiro)}</b></p>
        <p>Descanso entre tiros: <span class="highlight">{pausa}</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- CONTEÚDO TÉCNICO ---
st.header("🧬 A Ciência da Recuperação e Intensidade")

tab1, tab2 = st.tabs(["Fisiologia das Pausas", "Tipos de Treino"])

with tab1:
    st.markdown("""
    ### Por que a pausa é tão importante quanto o tiro?
    A pausa no treino intervalado não serve apenas para "descansar". Ela controla o sistema energético utilizado:
    * **Pausa Incompleta:** Mantém a frequência cardíaca elevada, forçando o corpo a trabalhar sob acúmulo de lactato.
    * **Relação Esforço/Pausa:** Para ganhos de velocidade, usamos frequentemente a proporção 1:1 ou 1:0.5. Se você corre por 2 minutos, descansa 1 ou 2 minutos.
    """)
    

with tab2:
    st.markdown("""
    ### Entendendo a Pirâmide de Treinamento
    1.  **Rodagem (80% do seu volume):** Constrói a base mitocondrial e fortalece tendões.
    2.  **Tempo Run:** O "confortavelmente difícil". Treina o corpo a remover o lactato enquanto você corre rápido.
    3.  **Tiros:** Aumentam a potência do motor (Coração e Pulmão).
    """)

st.info("💡 **Dica para o AdSense:** Este conteúdo técnico aumenta o tempo de permanência no site, sinalizando ao Google que sua página é valiosa.")
