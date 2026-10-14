import streamlit as st
import pandas as pd
import time

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="Emala Games Store",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS GAMING (NÉON / DARK MODE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Inter:wght@400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    
    /* Titres style Gaming */
    h1, h2, h3 { font-family: 'Rajdhani', sans-serif; text-transform: uppercase; letter-spacing: 1px; }
    
    /* Cartes de jeux */
    .game-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .game-card:hover {
        transform: translateY(-5px);
        border-color: #58a6ff;
    }
    .game-title { font-family: 'Rajdhani', sans-serif; font-size: 1.3rem; font-weight: 700; color: #f0f6fc; margin-top: 10px; }
    .game-genre { color: #8b949e; font-size: 0.85rem; margin-bottom: 10px; }
    .game-price { color: #3fb950; font-weight: 700; font-size: 1.1rem; }
    
    [data-testid="stSidebar"] { background-color: #11141d; border-right: 1px solid #30363D; }
</style>
""", unsafe_allow_html=True)

# --- GESTION DE LA BIBLIOTHÈQUE EN SESSION ---
if "library" not in st.session_state:
    st.session_state.library = ["Cyber-Nvidia 2077"] # Un jeu gratuit de base dans la bibliothèque

if "wallet" not in st.session_state:
    st.session_state.wallet = 50.0  # 50€ offerts pour commencer

# --- CATALOGUE DE JEUX ---
CATALOGUE = {
    "Cyber-Nvidia 2077": {
        "genre": "RPG / Action Deep-Tech",
        "prix": 0.0,
        "desc": "Incarnez un ingénieur luttant pour optimiser des puces quantiques dans un monde cyberpunk futuriste.",
        "image": "🚀",
        "dev": "Emala Studios"
    },
    "Quantum Racer": {
        "genre": "Course / Simulation",
        "prix": 19.99,
        "desc": "Des courses de bolides volants propulsés par intelligence artificielle à des vitesses supraluminiques.",
        "image": "🏎️",
        "dev": "DeepTech Games"
    },
    "Algorithmia Tactics": {
        "genre": "Stratégie / Tactique",
        "prix": 14.99,
        "desc": "Programmez des lignes de code et des unités autonomes pour conquérir des serveurs interstellaires.",
        "image": "💻",
        "dev": "CodeCraft"
    },
    "Silicon Tycoon": {
        "genre": "Gestion / Simulation",
        "prix": 24.99,
        "desc": "Créez votre propre entreprise de semi-conducteurs et tentez de dépasser les plus grands géants mondiaux.",
        "image": "🏭",
        "dev": "Silicon Corp"
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.title("🎮 EMALA GAMES")
    st.caption("Plateforme de Jeux Décentralisée")
    
    st.divider()
    st.markdown(f"💰 **Portefeuille :** `{round(st.session_state.wallet, 2)} €`")
    
    st.divider()
    menu = st.radio(
        "NAVIGATION",
        ["Magasin (Store)", "Ma Bibliothèque", "Communauté"]
    )

# ==========================================
# 1. MAGASIN (STORE)
# ==========================================
if menu == "Magasin (Store)":
    st.title("🛒 Emala Store — Découvrez les nouveautés")
    st.markdown("Trouvez les meilleurs jeux indépendants et de simulation deep-tech.")
    
    st.divider()
    
    # Affichage des jeux en grille de 2 colonnes
    cols = st.columns(2)
    idx = 0
    for nom_jeu, info in CATALOGUE.items():
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="game-card">
                <div style="font-size: 3rem;">{info['image']}</div>
                <div class="game-title">{nom_jeu}</div>
                <div class="game-genre">{info['genre']} | Par {info['dev']}</div>
                <p style="color: #c9d1d9; font-size: 0.9rem; min-height: 40px;">{info['desc']}</p>
                <div class="game-price">{'Gratuit' if info['prix'] == 0 else f"{info['prix']} €"}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Bouton d'action
            possede = nom_jeu in st.session_state.library
            if possede:
                st.success("✅ Déjà dans votre bibliothèque")
            else:
                if st.button(f"Acheter / Obtenir {nom_jeu}", key=f"buy_{nom_jeu}"):
                    if st.session_state.wallet >= info['prix']:
                        st.session_state.wallet -= info['prix']
                        st.session_state.library.append(nom_jeu)
                        st.success(f"Félicitations ! {nom_jeu} a été ajouté à votre bibliothèque.")
                        st.rerun()
                    else:
                        st.error("Fonds insuffisants dans votre portefeuille !")
            st.write("") # Espacement
        idx += 1

# ==========================================
# 2. MA BIBLIOTHÈQUE
# ==========================================
elif menu == "Ma Bibliothèque":
    st.title("📚 Votre Bibliothèque de Jeux")
    st.markdown("Lancez vos jeux installés directement depuis le cloud.")
    
    st.divider()
    
    if not st.session_state.library:
        st.info("Votre bibliothèque est vide. Visitez le magasin pour obtenir des jeux !")
    else:
        for jeu in st.session_state.library:
            info = CATALOGUE.get(jeu, {"genre": "Jeu indépendant", "image": "🎮", "desc": "Jeu classique."})
            
            col_img, col_info, col_btn = st.columns([1, 4, 2])
            with col_img:
                st.markdown(f"<h1 style='text-align: center;'>{info['image']}</h1>", unsafe_allow_html=True)
            with col_info:
                st.subheader(jeu)
                st.caption(f"{info['genre']} • Installé sur le cloud Emala")
                st.write(info['desc'])
            with col_btn:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button(f"▶ JOUER", key=f"play_{jeu}", use_container_width=True):
                    with st.status(f"Lancement de {jeu}...", expanded=True) as status:
                        st.write("Connexion aux serveurs cloud sécurisés...")
                        time.sleep(1)
                        st.write("Chargement des shaders et des textures...")
                        time.sleep(1)
                        st.write("Synchronisation des données de profil...")
                        time.sleep(0.8)
                        status.update(label=f"🚀 {jeu} est lancé !", state="complete", expanded=False)
                    st.balloons()
                    st.success(f"Bonne partie sur {jeu} ! (Simulation de session active)")
            st.divider()

# ==========================================
# 3. COMMUNAUTÉ
# ==========================================
elif menu == "Communauté":
    st.title("🌐 Hub de la Communauté Emala")
    st.markdown("Discutez avec les autres joueurs et développeurs de la plateforme.")
    
    st.divider()
    
    # Espace de discussion simple simulant un chat communautaire
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"user": "Alex_Dev", "text": "Quelqu'un a testé Silicon Tycoon ? Le marché des puces est ultra dur à maîtriser !"},
            {"user": "Emala_Admin", "text": "Bienvenue sur la plateforme les codeurs ! D'autres jeux arrivent bientôt."}
        ]
        
    for m in st.session_state.messages:
        st.markdown(f"**💬 {m['user']}** : {m['text']}")
        
    st.divider()
    nouveau_msg = st.text_input("Écrire un message à la communauté :")
    if st.button("Publier"):
        if nouveau_msg.strip():
            st.session_state.messages.append({"user": "Vous (Pro)", "text": nouveau_msg})
            st.rerun()
