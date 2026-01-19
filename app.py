import streamlit as st
# استيراد الوظائف الأساسية لضمان عمل النظام بالكامل
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("تنبيه: تأكد من وجود مجلد modules كاملاً في مستودع GitHub.")

# --- 1. الهوية البصرية المطابقة لموقع mdaghistani.com ---
st.set_page_config(
    page_title="M. DAGHISTANI | نظام التقدير العقاري",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* الألوان الأساسية للموقع */
    :root {
        --deep-blue: #0a192f;
        --gold-accent: #c2974d;
        --pure-white: #FFFFFF;
    }

    /* الخلفية بتدرج دائري ملكي */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, var(--deep-blue) 100%) !important;
    }

    /* تحسين الخطوط ووضوح النصوص */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
        color: var(--pure-white) !important;
    }

    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: var(--gold-accent) !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        text-align: center;
    }

    /* تأثير البطاقات الزجاجية (Glassmorphism) من موقعك */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(194, 151, 77, 0.2);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        transition: 0.5s ease;
    }
    .glass-card:hover {
        border-color: var(--gold-accent);
        transform: translateY(-8px);
    }

    /* تحسين وضوح حقول الإدخال لتكون بيضاء وواضحة */
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        color: var(--pure-white) !important;
        background-color: rgba(10, 25, 47, 0.8) !important;
        border: 1px dotted var(--gold-accent) !important;
        border-radius: 12px !important;
        font-weight: 700;
        height: 50px;
    }
    
    label { 
        color: var(--gold-accent) !important; 
        font-weight: 900 !important; 
        font-size: 1.1rem !important;
    }

    /* تصميم الأزرار الذهبية التفاعلية */
    div.stButton > button {
        background: var(--gold-accent) !important;
        color: var(--deep-blue) !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px !important;
        width: 100%;
        transition: 0.4s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background: #e0ac52 !important;
        box-shadow: 0 0 40px rgba(194, 151, 77, 0.5) !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. منطق تشغيل النظام الأصلي ---
def main():
    # تهيئة قاعدة البيانات (دوال من موديولاتك الأصلية)
    try:
        init_db()
        ensure_settings()
    except Exception as e:
        st.error(f"حدث خطأ في قاعدة البيانات: {e}")

    # ترويسة الموقع (الهيدر) بنفس أسلوب mdaghistani.com
    st.markdown("""
        <div style="text-align: center; padding: 50px 0;">
            <h1 style="font-size: 4.5rem; margin-bottom: 0;">م. داغستاني</h1>
            <div style="color: var(--gold-accent); font-size: 1.8rem; font-weight: 900; margin-top: -15px;">
                من مكة المكرمة.. نصلكم بالعالم
            </div>
            <div style="width: 120px; height: 3px; background: var(--gold-accent); margin: 25px auto; border-radius: 10px;"></div>
        </div>
        """, unsafe_allow_html=True)

    # تشغيل نظام تسجيل الدخول المحمي (من موديولاتك)
    user = login_required()
    
    if user:
        # تغليف لوحة التحكم داخل التصميم الزجاجي الجديد
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        render_dashboard(user)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
