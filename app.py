import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="StuDUBuddy AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# CUSTOM CSS
# ==============================
st.markdown("""
<style>

    /* ---------- MAIN BACKGROUND ---------- */
    .stApp {
        background: linear-gradient(135deg, #f8f9ff 0%, #eef2ff 100%);
    }

    /* ---------- SIDEBAR ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #1e293b 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* ---------- HEADER ---------- */
    .main-header {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        padding: 25px 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.25);
    }

    .main-header h1 {
        font-size: 38px;
        margin: 0;
        font-weight: 800;
    }

    .main-header p {
        font-size: 17px;
        margin-top: 8px;
        opacity: 0.9;
    }

    /* ---------- WELCOME CARD ---------- */
    .welcome-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        margin-bottom: 25px;
    }

    .welcome-card h2 {
        color: #4f46e5;
        margin-bottom: 10px;
    }

    .welcome-card p {
        color: #64748b;
        font-size: 16px;
    }

    /* ---------- FEATURE CARDS ---------- */
    .feature-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 18px rgba(0,0,0,0.05);
        height: 150px;
        transition: 0.3s;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.10);
    }

    .feature-icon {
        font-size: 30px;
    }

    .feature-title {
        font-size: 18px;
        font-weight: 700;
        color: #1e293b;
        margin-top: 8px;
    }

    .feature-text {
        font-size: 14px;
        color: #64748b;
    }

    /* ---------- CHAT MESSAGES ---------- */
    [data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* ---------- CHAT INPUT ---------- */
    [data-testid="stChatInput"] {
        border-radius: 15px;
    }

    /* ---------- BUTTONS ---------- */
    .stButton > button {
        border-radius: 12px;
        border: none;
        background: #6366f1;
        color: white;
        font-weight: 600;
        padding: 10px 20px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #4f46e5;
        transform: translateY(-2px);
    }

    /* ---------- SIDEBAR LOGO ---------- */
    .sidebar-logo {
        text-align: center;
        padding: 15px 5px 25px 5px;
    }

    .sidebar-logo .logo {
        font-size: 45px;
    }

    .sidebar-logo h2 {
        margin: 5px 0;
        font-size: 24px;
    }

    .sidebar-logo p {
        font-size: 13px;
        opacity: 0.7;
    }

    /* ---------- FOOTER ---------- */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        padding: 25px;
    }

</style>
""", unsafe_allow_html=True)


# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo">🎓</div>
        <h2>StuDUBuddy AI</h2>
        <p>Your AI-powered student companion</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 💡 What can I help with?")

    st.markdown("""
    - 📚 Study & academics
    - 💻 Coding problems
    - 📝 Assignments
    - 🎯 Career guidance
    - 🧠 Problem solving
    - 📅 Study planning
    """)

    st.markdown("---")

    st.markdown("### 🚀 About")

    st.write(
        "StuDUBuddy AI helps students solve problems, "
        "understand concepts and make better academic decisions."
    )


# ==============================
# MAIN HEADER
# ==============================
st.markdown("""
<div class="main-header">

    <h1>🎓 StuDUBuddy AI</h1>

    <p>
        Your smart AI companion for solving student problems.
        Ask anything, learn anything.
    </p>

</div>
""", unsafe_allow_html=True)


# ==============================
# WELCOME SECTION
# ==============================
st.markdown("""
<div class="welcome-card">

    <h2>👋 Hey Student!</h2>

    <p>
        I'm StuDUBuddy AI — here to help you with studies,
        coding, assignments, career questions and more.
    </p>

</div>
""", unsafe_allow_html=True)


# ==============================
# FEATURE CARDS
# ==============================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Study Help</div>
        <div class="feature-text">
            Understand difficult concepts easily.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💻</div>
        <div class="feature-title">Coding Support</div>
        <div class="feature-text">
            Get help with programming and debugging.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Career Guidance</div>
        <div class="feature-text">
            Explore skills, careers and opportunities.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ==============================
# CHATBOT
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input(
    "💬 Ask StuDUBuddy anything..."
)


if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)


    # ------------------------------------------------
    # PUT YOUR AI/API RESPONSE CODE HERE
    # ------------------------------------------------

    response = "I'm StuDUBuddy AI! 🤖 I'm here to help you solve your problem."

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# ==============================
# FOOTER
# ==============================
st.markdown("""
<div class="footer">
    🎓 StuDUBuddy AI &nbsp; • &nbsp;
    Built to make student life easier
</div>
""", unsafe_allow_html=True)