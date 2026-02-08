import streamlit as st
from core.explainer import explain

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Explain Like Anime 🤍",
    page_icon="🍥",
    layout="centered"
)

# ---------------------------
# Custom Anime CSS
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #fde2ff, #e0f7fa);
}

/* Title */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3em;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 2em;
}

/* Cards */
.anime-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-top: 20px;
}

/* Button */
.stButton>button {
    border-radius: 999px;
    font-weight: 600;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    color: white;
    border: none;
    padding: 0.6em 1.5em;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(120,115,245,0.4);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff1eb, #ace0f9);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown('<div class="main-title">🍥 Explain Like Anime</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Learn any concept explained by your favorite anime characters ✨</div>',
    unsafe_allow_html=True
)

# ---------------------------
# Sidebar controls
# ---------------------------
st.sidebar.header("🎌 Anime Settings")

anime = st.sidebar.selectbox(
    "Choose Anime",
    ["Naruto", "My Hero Academia", "Hunter x Hunter"]
)

character_map = {
    "Naruto": ["Naruto", "Kakashi"],
    "My Hero Academia": ["Deku", "All Might"],
    "Hunter x Hunter": ["Gon", "Killua"]
}

character = st.sidebar.selectbox(
    "Choose Character",
    character_map[anime]
)

level = st.sidebar.selectbox(
    "Explanation Level",
    ["beginner", "intermediate", "advanced"]
)

# ---------------------------
# Main input card
# ---------------------------
# st.markdown('<div class="anime-card">', unsafe_allow_html=True)

topic = st.text_input(
    "📘 What do you want to learn today?",
    placeholder="Neural Networks, Recursion, Confidence, Sorting Algorithms..."
)

if st.button("✨ Explain it!", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic 🌸")
    else:
        with st.spinner(f"{character} is thinking hard... 🧠✨"):
            explanation = explain(
                topic=topic,
                anime=anime,
                level=level,
                character=character
            )

        st.markdown("### 📖 Explanation")
        st.write(explanation)
        st.success("Done! Try another anime or character 🌟")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("<br>", unsafe_allow_html=True)
