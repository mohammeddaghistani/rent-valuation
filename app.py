import streamlit as st

try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.exception(e)
    st.stop()

st.set_page_config(
    page_title="M. DAGHISTANI CRM",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Professional UI Engine ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

:root { --gold: #c2974d; }

html, body, .stApp {
    font-family: 'Cairo', sans-serif !important;
    direction: rtl;
    background: radial-gradient(circle at 50% 50%, #0a192f 0%, #050a14 100%) !important;
    color: white !important;
}

h1,h2,h3 {
    font-family: 'Amiri', serif !important;
    color: var(--gold) !important;
}

.stDataFrame, div[data-testid="stDataFrame"], div[data-testid="stTable"] {
    border: 1px solid rgba(194,151,77,.3);
    border-radius: 12px;
    overflow-x: auto;
    backdrop-filter: blur(6px);
}

div.stButton > button {
    background: linear-gradient(135deg, #c2974d 0%, #a67c37 100%);
    color: #050a14;
    font-weight: 900;
    border-radius: 10px;
    padding: 10px 20px;
}

input, select {
    background-color: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(194,151,77,.4) !important;
    color: white !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)


def main():
    init_db()
    ensure_settings()

    st.markdown("""
    <div style="text-align:center;padding:30px;">
        <h1>م. داغستاني CRM</h1>
        <div style="color:#c2974d;font-size:1.2rem;">من مكة المكرمة.. نصلكم بالعالم</div>
    </div>
    """, unsafe_allow_html=True)

    user = login_required()
    if user:
        render_dashboard(user)


if __name__ == "__main__":
    main()
