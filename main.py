# main.py (VERSION CORRIGÉE - Contenu bien À L'INTÉRIEUR des cartes glassmorphism)

import streamlit as st
import os

# ---------------------------------------
# CONFIGURATION PAGE
# ---------------------------------------
st.set_page_config(
    page_title="GT Tools – Espace RH",
    page_icon="image.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------
# STYLE CSS
# ---------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #D8BFD8 0%, #CBC3E3 30%, #B19CD9 70%, #9370DB 100%);
    }

    .main-title {
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #6A3297, #F26522);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 2rem 0 0.5rem 0;
        letter-spacing: -2px;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.5rem;
        margin-bottom: 4rem;
    }

    .welcome-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #6A3297;
        margin-bottom: 4rem;
    }

    /* Carte glassmorphism */
    .glass-card {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 32px;
        padding: 3rem 2rem;
        text-align: center;
        box-shadow: 0 15px 35px rgba(106, 50, 151, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(106, 50, 151, 0.2);
        transition: all 0.4s ease;
        height: 420px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .glass-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 25px 50px rgba(106, 50, 151, 0.3);
        background: rgba(255, 255, 255, 0.4);
    }

    .card-icon {
        font-size: 6rem;
        margin-bottom: 2rem;
        color: #6A3297;
    }

    .card-title {
        font-size: 2rem;
        font-weight: 700;
        color: #4A2C6D;
        margin: 1rem 0;
    }

    .card-desc {
        color: #555;
        font-size: 1.1rem;
        line-height: 1.6;
        max-width: 80%;
    }

    /* Bouton circulaire en dessous */
    div.stButton > button {
        background: linear-gradient(135deg, #8B5CF6, #6A3297);
        color: white;
        border: none;
        width: 240px;
        height: 240px;
        border-radius: 50%;
        font-weight: 700;
        font-size: 1.3rem;
        box-shadow: 0 15px 35px rgba(106, 50, 151, 0.5);
        transition: all 0.4s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin: 3rem auto 0 auto;
        padding: 0;
        line-height: 1.4;
    }

    div.stButton > button:hover {
        transform: scale(1.08) translateY(-8px);
        box-shadow: 0 25px 50px rgba(106, 50, 151, 0.7);
        background: linear-gradient(135deg, #A855F7, #55277A);
    }

    .footer {
        text-align: center;
        color: #777;
        font-size: 1rem;
        margin-top: 6rem;
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# EN-TÊTE
# ---------------------------------------
logo_path = "logo GTT nEw.png"
if os.path.exists(logo_path):
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(logo_path, width=160)
    with col2:
        st.markdown("<h1 class='main-title'>GT TOOLS</h1>", unsafe_allow_html=True)
else:
    st.markdown("<h1 class='main-title'>GT TOOLS</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Choisissez votre outil RH</p>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "menu"

# ---------------------------------------
# MENU PRINCIPAL - Tout À L'INTÉRIEUR de la carte
# ---------------------------------------
if st.session_state.page == "menu":
    st.markdown("<h2 class='welcome-title'>Bienvenue sur votre Espace Applications</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        # TOUT le contenu de la carte en UN SEUL markdown → bien à l'intérieur
        st.markdown("""
        <div class='glass-card'>
            <div class='card-icon'>🏦</div>
            <h3 class='card-title'>Format Banque Mondiale</h3>
            <p class='card-desc'>Gérez et formatez votre base de CVs selon les standards GT</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("➡️\nAccéder\nà la Banque\nde CV", key="btn_banque"):
            st.session_state.page = "banque"
            st.rerun()

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <div class='card-icon'>📊</div>
            <h3 class='card-title'>Générateur PowerPoint GT</h3>
            <p class='card-desc'>Créez des présentations professionnelles au format GT</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("➡️\nAccéder\nau\nPowerPoint", key="btn_ppt"):
            st.session_state.page = "powerpoint"
            st.rerun()

    with col3:
        st.markdown("""
        <div class='glass-card'>
            <div class='card-icon'>📝</div>
            <h3 class='card-title'>CV Détailler</h3>
            <p class='card-desc'>CV détailler du personnel clé de l'offre</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("➡️\nAccéder\nà l'outil\nOffres", key="btn_app2"):
            st.session_state.page = "app2"
            st.rerun()

# ---------------------------------------
# PAGES DES APPLICATIONS
# ---------------------------------------
else:
    if st.button("← Retour au menu principal", type="secondary"):
        st.session_state.page = "menu"
        st.rerun()

    if st.session_state.page == "banque":
        import app_banque
        app_banque.main()

    elif st.session_state.page == "powerpoint":
        import app_powerpoint
        app_powerpoint.main()

    elif st.session_state.page == "app2":
        import app2
        app2.main()

# ---------------------------------------
# PIED DE PAGE
# ---------------------------------------
st.markdown("""
<div class='footer'>
    © 2025 Grant Thornton Technologies – Tous droits réservés<br>
    Tous les outils RH centralisés pour une meilleure productivité
</div>
""", unsafe_allow_html=True)