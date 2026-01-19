import streamlit as st
from modules.db import init_db, ensure_settings
from modules.auth import login_required
from modules.dashboard import render_dashboard

# --- إعدادات الهوية البصرية وتحسين وضوح الخط ---
st.set_page_config(page_title="M. DAGHISTANI | التقدير العقاري", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* تحسين وضوح النصوص والقراءة */
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
        color: #e6f1ff !important; /* لون نص فاتح وواضح */
    }

    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, #0a192f 100%);
    }

    /* العناوين الذهبية */
    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* تحسين وضوح حقول الإدخال */
    .stTextInput input, .stSelectbox div {
        color: white !important;
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid #c2974d !important;
    }
    
    label { color: #c2974d !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    # استعادة الوظائف المفقودة
    init_db()
    ensure_settings()
    
    # إضافة ترويسة الهوية
    st.markdown('<h1 style="text-align:center;">م. داغستاني</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#c2974d;">من مكة المكرمة.. نصلكم بالعالم</p>', unsafe_allow_html=True)
    
    user = login_required()
    if user:
        render_dashboard(user)

if __name__ == "__main__":
    main()
