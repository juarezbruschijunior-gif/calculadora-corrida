import streamlit as st

# 1. Configurações de SEO e Identidade Visual Profissional
st.set_page_config(page_title="Portal de Performance 5km - Juarez Bruschi", page_icon="🏃‍♂️")

# Estilo para melhorar a leitura e o visual (Padrão AdSense)
st.markdown("""
    <style>
    .main { background-color: #ffffff; color: #333; }
    .stButton>button { background-color: #007bff; color: white; border-radius: 8px; font-weight: bold; }
    h1, h2 { color: #0056b3; }
    .content-box { background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Menu de Navegação Estruturado
st.sidebar.title("🧭 Guia de Navegação")
menu = st.sidebar.radio("Escolha uma seção:", 
                        ["Calculadora de Performance", "Guia: Como Começar nos 5km", 
                         "Técnicas de Respiração", "Sobre o Autor", "Privacidade"])

if menu == "Calculadora de Performance":
    st.title("🏃‍♂️ Planejador de Ritmo para Treinos de Tiro")
    st.write("Esta ferramenta ajuda você a calcular o tempo exato para seus intervalos de velocidade (tiros), essencial para baixar seu tempo nos 5km.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            dist = st.selectbox("Selecione a Distância (metros):", [200, 400, 800, 1000, 1200])
        with col2:
            tempo_alvo = st.number_input("Sua Meta para 5km (minutos):", min_value=15, value=25)

        if st.button("Gerar Plano de Velocidade"):
            ritmo_total_seg = tempo_alvo * 60
            tempo_tiro = (ritmo_total_seg / 5000) * dist
            minutos = int(tempo_tiro // 60)
            segundos = int(tempo_tiro % 60)
            st.success(f"Para fechar os 5km em {tempo_alvo}min, seu tempo no tiro de {dist}m deve ser de: **{minutos:02d}:{segundos:02d}**")
            st.info("Recomendação: Execute de 6 a 10 repetições com descanso de 1:1 entre elas.")

elif menu == "Guia: Como Começar nos 5km":
    st.title("📚 Guia Completo: Do Zero aos 5km")
    st.markdown("""
    <div class='content-box'>
    <h3>O Volume é a Base</h3>
    Para correr 5km sem parar, você precisa construir uma base aeróbica sólida. Comece com o método <b>Corra e Caminhe</b>: alterne 2 minutos de corrida leve com 1 minuto de caminhada rápida. Repita isso por 20 a 30 minutos, três vezes por semana.
    
    <h3>A Regra dos 10%</h3>
    Nunca aumente sua distância semanal em mais de 10% de uma vez. Se você correu 10km no total da semana passada, corra no máximo 11km nesta semana. Isso evita lesões comuns como canelite e dores no joelho.
    
    <h3>A Importância do Aquecimento</h3>
    Nunca comece um tiro de velocidade com o corpo "frio". Faça pelo menos 10 minutos de trote bem lento e alguns exercícios educativos (como skipping) para preparar as articulações.
    </div>
    """, unsafe_allow_html=True)

elif menu == "Técnicas de Respiração":
    st.title("🫁 Dominando a Respiração na Corrida")
    st.write("""
    Muitos corredores iniciantes sentem a famosa 'dor de lado'. Isso geralmente é falta de oxigenação adequada. 
    Siga estas dicas para melhorar seu fôlego:
    * **Respiração Abdominal:** Tente levar o ar para a barriga, não apenas para o peito.
    * **Ritmo 2:2:** Tente inspirar durante dois passos e expirar durante dois passos. Isso cria um ritmo constante que evita a fadiga precoce.
    * **Nariz e Boca:** Em alta intensidade, use ambos para captar o máximo de oxigênio possível.
    """)

elif menu == "Sobre o Autor":
    st.title("👨‍🏫 Juarez Bruschi Junior")
    st.write("Professor, desenvolvedor e entusiasta da corrida de rua. Este portal foi criado para compartilhar conhecimento técnico e ferramentas de cálculo para atletas amadores que buscam evolução constante.")

elif menu == "Privacidade":
    st.title("🔒 Compromisso com a Privacidade")
    st.write("Este site segue as diretrizes do Google AdSense. Não coletamos dados pessoais e utilizamos cookies apenas para melhorar a experiência do usuário e exibir anúncios relevantes.")

# 3. Rodapé de Autoridade (Crucial para o AdSense)
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Portal de Performance 5km | Juarez Bruschi Junior | Passo Fundo - RS</p>", unsafe_allow_html=True)
