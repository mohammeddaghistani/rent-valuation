import streamlit as st

# استيراد الوظائف الأساسية لضمان عمل النظام
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.exception(e)
    st.stop()

# إعدادات الصفحة
st.set_page_config(
    page_title="M. DAGHISTANI CRM",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- محرك التصميم العصري الاحترافي (Modern Clean UI) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

/* 1. الخلفية: أبيض ناصع مع تدرج رمادي خفيف جداً للفخامة */
html, body, .stApp {
    background: #FFFFFF !important; /* خلفية بيضاء نظيفة */
    color: #1A1A1A !important; /* نصوص سوداء فحمي لسهولة القراءة */
    font-family: 'Cairo', sans-serif !important;
    direction: rtl;
}

/* 2. العناوين: ذهبي نحاسي فخم */
h1, h2, h3 {
    font-family: 'Amiri', serif !important;
    color: #B8860B !important; /* Dark Goldenrod */
    text-align: center;
}

/* 3. الجداول: تصميم نظيف (Clean Data Grid) */
.stDataFrame, div[data-testid="stTable"] {
    background-color: white !important;
    border: 1px solid #E0E0E0 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

/* عناوين الجداول: أسود ملكي مع خط ذهبي */
thead tr th {
    background-color: #1A1A1A !important;
    color: #B8860B !important;
    font-weight: 700 !important;
}

/* خلايا الجداول: بيضاء واضحة جداً */
tbody tr td {
    background-color: #FFFFFF !important;
    color: #333333 !important;
    border-bottom: 1px solid #F0F0F0 !important;
}

/* 4. حقول الإدخال: تصميم Apple (Clean Inputs) */
input, select, textarea {
    background-color: #F9F9F9 !important;
    border: 1px solid #D1D1D1 !important;
    color: #1A1A1A !important;
    border-radius: 10px !important;
    padding: 12px !important;
}

input:focus {
    border: 2px solid #B8860B !important;
    background-color: #FFFFFF !important;
}

/* 5. الأزرار: ذهبي مطفي (Satin Gold) */
div.stButton > button {
    background: #B8860B !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    width: 100%;
    height: 45px;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    background: #1A1A1A !important; /* يتحول للأسود عند المرور عليه */
    box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3);
}

/* 6. تنسيق الجوال */
@media (max-width: 768px) {
    .main-title { font-size: 2rem !important; }
}
</style>
""", unsafe_allow_html=True)

def main():
    init_db()
    ensure_settings()

    # الهيدر (الشعار الرسمي)
    st.markdown("""
    <div style="text-align:center; padding:20px 0;">
        <h1 class="main-title" style="margin:0; font-size:3.5rem;">محمد داغستاني</h1>
        <div style="color:#B8860B; font-weight:700; font-size:1.2rem; letter-spacing:2px;">
            CRM & INVESTMENT VALUATION
        </div>
        <div style="width:50px; height:3px; background:#1A1A1A; margin:15px auto;"></div>
    </div>
    """, unsafe_allow_html=True)

    # تشغيل نظام الدخول
    user = login_required()
    if user:
        # تغليف لوحة التحكم في حاوية بيضاء نظيفة
        st.markdown('<div style="background:#FFFFFF; padding:20px; border-radius:15px;">', unsafe_allow_html=True)
        render_dashboard(user)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
