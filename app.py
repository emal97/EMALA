import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="Emala Launcher Pro",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS EPIC GAMES / DARK MODE ---
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
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "playing" not in st.session_state:
    st.session_state.playing = None

# --- NAVIGATION SUPÉRIEURE ---
t1, t2, t3, t4 = st.columns([1, 1, 1, 5])
with t1:
    st.markdown("### 🛒 Boutique")
with t2:
    st.markdown("### 📚 Bibliothèque")
with t3:
    st.markdown("### 🚀 **Développer**")
with t4:
    st.caption("Emala Launcher v3.1 • Mode Jeu Actif")

st.divider()

if st.session_state.playing:
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅ Quitter le jeu"):
            st.session_state.playing = None
            st.rerun()
    with col_title:
        st.markdown(f"## 🎮 En cours de partie : {st.session_state.playing}")
    
    st.divider()

    # --- CODE DU JEU ROBUSTE AVEC FOCUS ACTIF ---
    arcade_game_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: #05070b;
                color: #00ffcc;
                text-align: center;
                font-family: 'Inter', sans-serif;
                margin: 0;
                overflow: hidden;
            }
            canvas {
                background: #0b0e14;
                border: 2px solid #00ffcc;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,255,204,0.3);
                cursor: pointer;
            }
            #info {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 8px;
                color: #ffffff;
            }
        </style>
    </head>
    <body>
        <div id="info">Score : <span id="points">0</span> | <span id="status" style="color: #00ffcc;">Cliquez sur l'écran pour activer le jeu !</span></div>
        <canvas id="gameCanvas" width="700" height="380"></canvas>
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");

            let player = { x: 325, y: 320, width: 50, height: 20, color: "#00ffcc", speed: 8 };
            let obstacles = [];
            let score = 0;
            let gameOver = false;
            let gameStarted = false;
            let keys = {};

            // Activation au clic de l'utilisateur pour contourner le blocage iframe
            canvas.addEventListener("click", () => {
                if (!gameStarted) {
                    gameStarted = true;
                    document.getElementById("status").innerText = "Utilisez les flèches GAUCHE / DROITE pour esquiver !";
                    loop();
                }
            });

            window.addEventListener("keydown", (e) => {
                if(["ArrowLeft","ArrowRight"," "].includes(e.key)) e.preventDefault();
                keys[e.key] = true;
            });
            window.addEventListener("keyup", (e) => keys[e.key] = false);

            function spawnObstacle() {
                if (Math.random() < 0.04) {
                    obstacles.push({
                        x: Math.random() * (canvas.width - 40),
                        y: -40,
                        width: 40,
                        height: 40,
                        speed: 4 + Math.random() * 4,
                        color: "#ff0055"
                    });
                }
            }

            function update() {
                if (gameOver || !gameStarted) return;

                if (keys["ArrowLeft"] && player.x > 0) player.x -= player.speed;
                if (keys["ArrowRight"] && player.x < canvas.width - player.width) player.x += player.speed;

                spawnObstacle();

                for (let i = obstacles.length - 1; i >= 0; i--) {
                    obstacles[i].y += obstacles[i].speed;

                    if (
                        player.x < obstacles[i].x + obstacles[i].width &&
                        player.x + player.width > obstacles[i].x &&
                        player.y < obstacles[i].y + obstacles[i].height &&
                        player.y + player.height > obstacles[i].y
                    ) {
                        gameOver = true;
                    }

                    if (obstacles[i].y > canvas.height) {
                        obstacles.splice(i, 1);
                        score += 10;
                        document.getElementById("points").innerText = score;
                    }
                }
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // Dessin Joueur
                ctx.fillStyle = player.color;
                ctx.fillRect(player.x, player.y, player.width, player.height);

                // Dessin Obstacles
                for (let obs of obstacles) {
                    ctx.fillStyle = obs.color;
                    ctx.fillRect(obs.x, obs.y, obs.width, obs.height);
                }

                if (!gameStarted) {
                    ctx.fillStyle = "rgba(0, 0, 0, 0.75)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = "#00ffcc";
                    ctx.font = "20px Inter";
                    ctx.textAlign = "center";
                    ctx.fillText("▶ CLIQUEZ ICI POUR LANCER LA PARTIE", canvas.width / 2, canvas.height / 2);
                }

                if (gameOver) {
                    ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = "#ff0055";
                    ctx.font = "30px Inter";
                    ctx.textAlign = "center";
                    ctx.fillText("GAME OVER", canvas.width / 2, canvas.height / 2 - 15);
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "15px Inter";
                    ctx.fillText("Cliquez sur 'Quitter le jeu' puis relancez pour rejouer", canvas.width / 2, canvas.height / 2 + 25);
                }
            }

            // Affichage initial de l'écran d'accueil
            draw();

            function loop() {
                update();
                draw();
                if (!gameOver) requestAnimationFrame(loop);
            }
        </script>
        </body>
        </html>
        """
        components.html(arcade_game_html, height=450)

else:
    col_workspace, col_social = st.columns([3, 1])

    with col_workspace:
        sub_tab = st.radio("Navigation", ["Bibliothèque", "Outils", "Projets"], horizontal=True, label_visibility="collapsed")
        
        if sub_tab == "Bibliothèque":
            st.markdown("## 📚 Votre Bibliothèque de Jeux")
            st.markdown("""
            <div class="project-card">
                <h3 style="margin: 0; color: #ffffff;">🚀 Cyber-Runner 2077</h3>
                <p style="color: #a1a1aa; font-size: 0.9rem;">Moteur : Emala Engine 5.4 | Statut : Prêt à jouer</p>
                <p style="color: #00ffcc; font-size: 0.85rem;">Esquivez les blocs rouges dans ce jeu d'arcade intégré !</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("▶ LANCER LE JEU", type="primary"):
                st.session_state.playing = "Cyber-Runner 2077"
                st.rerun()

        elif sub_tab == "Outils":
            st.markdown("## ⚙️ Compilateur & SDK")
            st.success("🟢 Compilateur C++ et CUDA virtuels prêts.")

        elif sub_tab == "Projets":
            st.markdown("## 💻 Espace Développement")
            st.info("Aucun projet en cours de compilation.")

    with col_social:
        st.markdown("""
        <div style="background-color: #18181b; border: 1px solid #27272a; border-radius: 10px; padding: 15px;">
            <h3 style="margin-top: 0; font-size: 1.1rem;">👥 Panneau social</h3>
            <p style="font-size: 0.75rem; color: #a1a1aa;">Groupe : Public 🔓</p>
            <hr style="border-color: #27272a;">
            🟢 <b>Emala!</b> (En ligne)<br><br>
            <b style="font-size: 0.85rem;">Amis en jeu :</b><br>
            🟢 <b>Alex_Dev</b><br>
            <span style="font-size: 0.75rem; color: #3fb950;">Joue à Cyber-Runner</span>
        </div>
        """, unsafe_allow_html=True)
