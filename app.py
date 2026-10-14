import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="Emala Game Engine Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS EPIC GAMES / UNREAL ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0e0e10; color: #efeff1; }
    .project-card {
        background-color: #1f1f23;
        border: 1px solid #2f2f35;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .social-panel {
        background-color: #18181b;
        border: 1px solid #27272a;
        border-radius: 10px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION SUPÉRIEURE ---
t1, t2, t3, t4, t5 = st.columns([1, 1, 1, 1, 4])
with t1:
    st.markdown("### 🛒 Boutique")
with t2:
    st.markdown("### 📚 Bibliothèque")
with t3:
    st.markdown("### ⚙️ **Moteur Studio**")
with t4:
    st.markdown("### 🌐 Communauté")
with t5:
    st.caption("Emala Engine v4.1 • Studio Pro Actif")

st.divider()

# --- LAYOUT PRINCIPAL ---
col_workspace, col_social = st.columns([3, 1])

with col_workspace:
    st.markdown("## 🔬 Laboratoire de Physique & Trajectoire 3D")
    st.markdown("Simulateur de moteur physique en temps réel (Calculs vectoriels et cinématiques).")
    
    st.divider()

    # Contrôles du moteur physique
    c1, c2, c3 = st.columns(3)
    vitesse_initiale = c1.slider("Vitesse Initiale (m/s)", 10, 100, 50)
    angle_tir = c2.slider("Angle de Tir (Degrés)", 10, 80, 45)
    gravite = c3.slider("Gravité (m/s²)", 1.0, 20.0, 9.81)

    # Calculs mathématiques de la trajectoire balistique avec NumPy
    g = gravite
    theta = np.radians(angle_tir)
    v0 = vitesse_initiale

    t_vol = (2 * v0 * np.sin(theta)) / g
    t = np.linspace(0, t_vol, num=100)

    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * (t ** 2)
    y = np.maximum(y, 0)

    portee_max = x[-1] if len(x) > 0 else 0
    hauteur_max = (v0**2 * (np.sin(theta)**2)) / (2 * g)

    m1, m2, m3 = st.columns(3)
    m1.metric("Portée Maximale", f"{round(portee_max, 2)} m")
    m2.metric("Hauteur Atteinte", f"{round(hauteur_max, 2)} m")
    m3.metric("Temps de Vol", f"{round(t_vol, 2)} s")

    # Graphique natif Streamlit ultra fluide (zéro dépendance externe)
    df_chart = pd.DataFrame({
        "Distance (m)": x,
        "Altitude (m)": y
    }).set_index("Distance (m)")

    st.line_chart(df_chart, height=400)

    if st.button("🚀 Compiler et Exécuter la Scène 3D", type="primary"):
        with st.status("Compilation des shaders et des scripts C#...", expanded=True) as status:
            st.write("Optimisation des matrices de collision...")
            time.sleep(0.4)
            st.write("Chargement des textures dans la VRAM...")
            time.sleep(0.4)
            status.update(label="Scène compilée et active avec succès !", state="complete", expanded=False)
        st.success("Le moteur physique s'exécute à 240 FPS constants.")

with col_social:
    st.markdown("""
    <div class="social-panel">
        <h3 style="margin-top: 0; font-size: 1.1rem;">👥 Panneau social</h3>
        <p style="font-size: 0.75rem; color: #a1a1aa;">Groupe : Session Studio 🔒</p>
        <hr style="border-color: #27272a;">
        🟢 <b>Emala!</b> (Développeur Principal)<br><br>
        <b style="font-size: 0.85rem; color: #0078f2;">Membres du Studio :</b><br>
        🟢 <b>Alex_Dev</b><br>
        <span style="font-size: 0.75rem; color: #3fb950;">Édition de shaders</span><br><br>
        🟢 <b>NvidiaEng</b><br>
        <span style="font-size: 0.75rem; color: #3fb950;">Optimisation CUDA</span>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("💬 Ouvrir le Chat Studio", use_container_width=True):
        st.toast("Canal de discussion du studio ouvert.")
