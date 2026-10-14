import streamlit as st
import pandas as pd
import time

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="Emala Launcher Pro",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS EPIC GAMES / UNREAL ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0e0e10; color: #efeff1; }
    
    /* Style des cartes de projets */
    .project-card {
        background-color: #1f1f23;
        border: 1px solid #2f2f35;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        transition: border-color 0.2s ease;
    }
    .project-card:hover {
        border-color: #0078f2;
    }
    
    /* Panneau Social latéral */
    .social-panel {
        background-color: #18181b;
        border: 1px solid #27272a;
        border-radius: 10px;
        padding: 15px;
    }
    
    /* Header supérieur */
    .top-nav {
        background-color: #18181b;
        padding: 12px 20px;
        border-bottom: 1px solid #27272a;
        border-radius: 8px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- GESTION DES PROJETS EN SESSION ---
if "projets_list" not in st.session_state:
    st.session_state.projets_list = [
        {"nom": "Cyber-Nvidia Core 2077", "moteur": "Emala Engine 5.4", "statut": "Prêt"},
        {"nom": "Simulation Quantique GPU", "moteur": "DeepTech SDK", "statut": "Compilé"}
    ]

# --- NAVIGATION SUPÉRIEURE (STYLE EPIC) ---
t1, t2, t3, t4 = st.columns([1, 1, 1, 5])
with t1:
    st.markdown("### 🛒 Boutique")
with t2:
    st.markdown("### 📚 Bibliothèque")
with t3:
    st.markdown("### 🚀 **Développer**")
with t4:
    st.caption("Emala Launcher v2.6.0 • Connecté en mode Administrateur")

st.divider()

# --- LAYOUT PRINCIPAL : ESPACE PROJET (GAUCHE) & PANNEAU SOCIAL (DROITE) ---
col_workspace, col_social = st.columns([3, 1])

with col_workspace:
    # Sous-onglets de la section Développer (Outils, Projets, Fab, Apprendre)
    sub_tab = st.radio("Navigation Développeur", ["Outils", "Projets", "Fab", "Apprendre"], horizontal=True, label_visibility="collapsed")
    
    if sub_tab == "Projets":
        st.markdown("## Projets Emala Engine")
        
        # Barre de recherche et filtres
        c_search, c_filter = st.columns([3, 1])
        with c_search:
            recherche = st.text_input("Recherche", placeholder="Chercher dans les projets...", label_visibility="collapsed")
        with c_filter:
            st.button("⚙️ Filtrer et trier", use_container_width=True)
            
        st.write("")
        
        # Formulaire de création de nouveau projet
        with st.expander("➕ Créer un nouveau projet Deep-Tech"):
            nouveau_nom = st.text_input("Nom du nouveau projet", value="MonMoteurGraphique")
            if st.button("Initialiser le workspace"):
                st.session_state.projets_list.append({"nom": nouveau_nom, "moteur": "Emala Engine 5.4", "statut": "Nouveau"})
                st.success(f"Projet {nouveau_nom} initialisé avec succès !")
                st.rerun()

        st.divider()
        
        # Affichage de la liste des projets
        projets_trouves = False
        for proj in st.session_state.projets_list:
            if recherche.lower() in proj['nom'].lower() or not recherche:
                projets_trouves = True
                st.markdown(f"""
                <div class="project-card">
                    <h3 style="margin: 0; color: #ffffff;">💻 {proj['nom']}</h3>
                    <p style="color: #a1a1aa; font-size: 0.85rem; margin-top: 5px;">Moteur : {proj['moteur']} | Statut : <span style="color: #3fb950;">{proj['statut']}</span></p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Lancer l'éditeur pour {proj['nom']}", key=f"launch_{proj['nom']}"):
                    with st.status(f"Lancement de l'environnement pour {proj['nom']}...", expanded=True) as status:
                        st.write("Chargement des bibliothèques d'algèbre linéaire...")
                        time.sleep(0.8)
                        st.write("Allocation des registres CUDA virtuels...")
                        time.sleep(0.8)
                        status.update(label=f"🚀 {proj['nom']} est prêt !", state="complete", expanded=False)
                    st.balloons()
                    st.success("Session de développement active.")
        
        if not projets_trouves:
            st.info("Aucun projet trouvé sur cet appareil correspondant à votre recherche.")

    elif sub_tab == "Outils":
        st.markdown("## Outils de Compilation")
        st.write("Gérez vos kits de développement C++, Python et vos compilateurs CUDA.")
        st.success("🟢 Compilateur Emala GCC v14.2 prêt.")

    elif sub_tab == "Fab":
        st.markdown("## Fab — Place de marché 3D & Shaders")
        st.write("Téléchargez des textures haute résolution et des modèles de réseaux de neurones pré-entraînés.")

    elif sub_tab == "Apprendre":
        st.markdown("## Apprendre — Tutoriels Deep-Tech")
        st.info("Découvrez comment coder des moteurs graphiques et optimiser le calcul matriciel.")

with col_social:
    # Panneau Social latéral (exactement comme sur ton image Epic Games)
    st.markdown("""
    <div class="social-panel">
        <h3 style="margin-top: 0; font-size: 1.1rem;">👥 Panneau social</h3>
        <p style="font-size: 0.75rem; color: #a1a1aa;">Groupe : Sur invitation 🔒<br>Signalement activé</p>
        <hr style="border-color: #27272a;">
        <b style="font-size: 0.85rem; color: #0078f2;">Mon profil :</b><br>
        🟢 <b>Emala!</b> (En ligne)<br><br>
        <hr style="border-color: #27272a;">
        <b style="font-size: 0.85rem;">Conversations rejoignables :</b><br>
        🟢 <b>Alex_Dev</b><br>
        <span style="font-size: 0.75rem; color: #3fb950;">Rejoignable • Benchmark GPU</span><br><br>
        🟢 <b>NvidiaFan99</b><br>
        <span style="font-size: 0.75rem; color: #3fb950;">Rejoignable • Simulation Python</span><br><br>
        <hr style="border-color: #27272a;">
        <b style="font-size: 0.85rem;">Invitations (1) :</b><br>
        <span style="font-size: 0.8rem; color: #e11d48;"><b>P1XUL.era</b> vous invite à rejoindre son groupe !</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("💬 Ouvrir les Chats", use_container_width=True):
        st.toast("Canal de discussion chiffré ouvert.")

# --- BARRE DE BAS DE PAGE ---
st.divider()
st.caption("🟢 Statut du système : Connecté au Cloud Global Emala | Téléchargements : 0 ko/s | Version Launcher 2.6.0")
