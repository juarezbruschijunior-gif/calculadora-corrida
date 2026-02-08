import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Pace Pro - Fisiologia e Performance", page_icon="🏃‍♂️", layout="wide")

# CSS Customizado para Visual "Alto Nível"
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #1E1E1E;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .metric-box {
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border-left: 5px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🏃‍♂️ Pace Pro: Engenharia da Performance")
st.markdown("### Transforme seus dados em resultados com ciência do esporte.")

# Imagem de Hero (Corredor Real)
st.image("https://images.unsplash.com/photo-1452626038306-9aae5e071dd3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", 
         caption="A alta performance começa na precisão dos dados.")

# --- CALCULADORA EM COLUNAS ---
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Calculadora de Ritmo")
    distancia = st.selectbox("Distância da prova (km):", [5, 10, 21, 42], index=0)
    
    c1, c2 = st.columns(2)
    with c1:
        minutos = st.number_input("Minutos totais:", min_value=0, value=25)
    with c2:
        segundos = st.number_input("Segundos totais:", min_value=0, max_value=59, value=0)

    if st.button("Calcular Estratégia"):
        tempo_total_seg = (minutos * 60) + segundos
        ritmo_decimal = (tempo_total_seg / distancia) / 60
        ritmo_min = int(ritmo_decimal)
        ritmo_seg = int((ritmo_decimal - ritmo_min) * 60)
        
        st.markdown(f"""
            <div class="metric-box">
                <p style="margin:0;">Ritmo Médio Necessário:</p>
                <h2 style="margin:0; color:#28a745;">{ritmo_min}:{ritmo_seg:02d} min/km</h2>
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("⏱️ Sugestão de Tiros (Intervalados)")
    st.info("Treinos calculados com 10% de intensidade acima do pace de prova.")
    # Cálculo lógico simplificado para os tiros
    if 'ritmo_decimal' in locals():
        tiro_400 = (ritmo_decimal * 0.9) * 0.4 * 60
        st.write(f"**Tiro de 400m:** {int(tiro_400 // 60):02d}:{int(tiro_400 % 60):02d}")
        st.write(f"**Tiro de 800m:** {int((tiro_400*2) // 60):02d}:{int((tiro_400*2) % 60):02d}")
    else:
        st.write("Insira os dados e clique em calcular para ver os tiros.")

st.markdown('</div>', unsafe_allow_html=True)

# --- ARTIGO TÉCNICO (O que o Google AdSense ama) ---
st.divider()
st.header("🧬 A Fisiologia por trás do Treino de Tiros")

col_text, col_img = st.columns([2, 1])

with col_text:
    st.markdown("""
    Os treinos intervalados, popularmente conhecidos como **treinos de tiro**, são o pilar central para corredores que buscam quebrar recordes pessoais. 
    Mas o que acontece dentro do seu corpo durante esses esforços?
    
    #### 1. VO2 Máximo e Eficiência Cardíaca
    Ao correr em intensidades superiores ao seu limiar aeróbico, você força o seu coração a bombear mais sangue por batimento (volume sistólico). 
    Com o tempo, isso aumenta a sua capacidade máxima de consumo de oxigênio ($VO_2$ máx), permitindo que você corra mais rápido com menos esforço.

    #### 2. Limiar de Lactato
    O "tiro" ensina o seu corpo a lidar com o ácido lático. Em intensidades altas, o corpo produz lactato mais rápido do que consegue remover. 
    O treinamento intervalado melhora a eficiência das suas mitocôndrias em oxidar esse lactato e reutilizá-lo como energia, retardando a fadiga extrema.
    
    #### 3. Recrutamento de Fibras Tipo II
    Diferente da rodagem leve, o tiro recruta as **fibras musculares de contração rápida** (Tipo II). Elas são essenciais para o "sprint" final de uma prova e para melhorar a economia de corrida.
    """)

with col_img:
    st.image("https://images.unsplash.com/photo-1530143311094-34d807799e8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80")

st.markdown("""
> **Nota do Especialista:** Não realize treinos de tiro em dias consecutivos. O processo de supercompensação exige pelo menos 48 horas de recuperação para que as adaptações fisiológicas ocorram sem risco de lesão.
""")

# Rodapé
st.divider()
st.center = st.markdown("© 2026 Pace Pro - Ciência e Performance Humana")
