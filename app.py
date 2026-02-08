import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="BioScience Run - Calculadora de Performance", page_icon="🏃")

# 2. ADSENSE
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3241373482970085"
     crossorigin="anonymous"></script>
    """,
    height=0,
)

# 3. MENU LATERAL
st.sidebar.title("🔬 BioScience Menu")
aba = st.sidebar.radio("Navegar:", ["Calculadora de Tiros (5km)", "Artigos e Fisiologia", "Privacidade", "Contato"])

if aba == "Calculadora de Tiros (5km)":
    st.title("🏃 Calculadora de Tiros para 5 km")
    st.write("Insira seu tempo pretendido nos 5 km para gerar sua planilha de tiros.")
    
    # Imagem de cabeçalho
    st.image("https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?q=80&w=1000&auto=format&fit=crop", caption="Alta Performance e Ciência")

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        t_min = st.number_input("Minutos nos 5km:", min_value=10, value=25, step=1)
    with col2:
        t_seg = st.number_input("Segundos nos 5km:", min_value=0, max_value=59, value=0, step=1)

    tempo_total_seg = (t_min * 60) + t_seg
    pace_prova_seg = tempo_total_seg / 5
    # Ritmo de tiro 10% mais rápido que o pace de prova
    pace_tiro_seg = pace_prova_seg * 0.9

    if st.button("Gerar Planilha de Treino"):
        st.subheader("🎯 Sua Planilha de Tiros Customizada")
        st.info(f"Seu Pace de Prova: {int(pace_prova_seg//60)}:{int(pace_prova_seg%60):02d} min/km")

        # Configuração dos Tiros
        tiros = {
            "100 metros": {"fator": 0.1, "qtd": "12 a 15", "pausa": "45 seg"},
            "400 metros": {"fator": 0.4, "qtd": "10 a 12", "pausa": "1 min 30 seg"},
            "800 metros": {"fator": 0.8, "qtd": "6 a 8", "pausa": "2 min"},
            "1000 metros": {"fator": 1.0, "qtd": "5 a 6", "pausa": "2 min 30 seg"}
        }

        for dist, info in tiros.items():
            t_tiro_total = pace_tiro_seg * info["fator"]
            m_tiro = int(t_tiro_total // 60)
            s_tiro = int(t_tiro_total % 60)
            
            with st.expander(f"Tiros de {dist}"):
                st.write(f"⏱️ **Tempo do tiro:** {m_tiro:02d}:{s_tiro:02d}")
                st.write(f"🔢 **Quantidade:** {info['qtd']} repetições")
                st.write(f"⏳ **Descanso:** {info['pausa']}")

elif aba == "Artigos e Fisiologia":
    st.title("🔬 Ciência da Performance")
    
    st.image("https://images.unsplash.com/photo-1552674605-db6ffd4facb5?q=80&w=1000&auto=format&fit=crop", caption="Biometria e Fisiologia do Exercício")
    
    st.header("1. Treino Intervalado (Tiros)")
    st.write("""
    Como Biomédico, destaco que o treino de tiros induz a **biogênese mitocondrial**. Ao submeter o corpo a esforços acima do 
    limiar aeróbico, forçamos o organismo a melhorar o tamponamento do lactato e a eficiência na ressíntese de ATP.
    """)

    st.header("2. O Papel do Descanso")
    st.write("""
    A pausa entre os tiros é fundamental para a recuperação parcial dos estoques de fosfocreatina. Sem o descanso correto, 
    o treino deixa de ser de velocidade e torna-se apenas exaustivo, aumentando o risco de lesões por estresse oxidativo.
    """)

    st.header("3. Rodagem e Capilarização")
    st.write("""
    Treinos leves aumentam a densidade capilar nos músculos, facilitando o transporte de oxigênio. É a base necessária 
    para suportar os treinos intensos.
    """)

elif aba == "Privacidade":
    st.title("Política de Privacidade")
    st.write("Este site utiliza cookies do Google para anúncios. Não coletamos dados de saúde dos usuários.")

elif aba == "Contato":
    st.title("Contato")
    st.write("📧 Responsável Técnico: **Juarez Bruschi Junior - Biomédico**")

# 4. RODAPÉ PROFISSIONAL
st.write("---")
st.caption("Desenvolvido por **Juarez Bruschi Junior | Biomédico**")
st.caption("BioScience Run Performance © 2026")
