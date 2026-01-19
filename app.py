import streamlit as st
# استيراد الوظائف الأصلية لبرنامجك لضمان عدم فقدان أي ميزة
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("خطأ: لم يتم العثور على مجلد modules. تأكد من رفعه كاملاً على GitHub.")

# --- 1. الهوية البصرية المستوحاة من mdaghistani.com ---
st.set_page_config(page_title="M. DAGHISTANI | التقدير العقاري", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* تحسين الألوان لتطابق الموقع تماماً */
    :root {
        --primary: #0a192f;
        --accent: #c2974d;
        --text: #e6f1ff;
    }

    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, #0a192f 100%) !important;
    }

    /* تحسين وضوح الخطوط (الأبيض الناصع) */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
        color: var(--text) !important;
    }

    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: var(--accent) !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* تأثير البطاقات الزجاجية من الموقع */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(194, 151, 77, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        transition: 0.4s;
    }
    .glass-card:hover {
        border-color: var(--accent);
        background: rgba(194, 151, 77, 0.05);
        transform: translateY(-5px);
    }

    /* تحسين وضوح حقول الإدخال */
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        color: #FFFFFF !important;
        background-color: rgba(10, 25, 47, 0.8) !important;
        border: 1px solid rgba(194, 151, 77, 0.3) !important;
        border-radius: 12px !important;
        font-weight: bold;
    }

    /* الأزرار الذهبية المستوحاة من زر "إرسال الطلب" */
    div.stButton > button {
        background: var(--accent) !important;
        color: var(--primary) !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px !important;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #e0ac52 !important;
        box-shadow: 0 0 30px rgba(194, 151, 77, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الهيكل التنظيمي للبرنامج ---
def main():
    # تشغيل قاعدة البيانات الأصلية
    try:
        init_db()
        ensure_settings()
    except Exception as e:
        st.error(f"فشل في الاتصال بقاعدة البيانات: {e}")

    # الهيدر المتوافق مع الموقع
    st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="font-size: 4rem; margin-bottom: 0;">م. داغستاني</h1>
            <p style="color: #c2974d; font-size: 1.6rem; font-weight: bold; margin-top: -10px;">
                من مكة المكرمة.. نصلكم بالعالم
            </p>
            <div style="width: 80px; height: 4px; background: #c2974d; margin: 20px auto; border-radius: 10px;"></div>
        </div>
        """, unsafe_allow_html=True)

    # تشغيل نظام الدخول ولوحة التحكم الأصلية
    # هذا السطر يضمن عدم فقدان أي وظيفة من موديولاتك
    user = login_required()
    if user:
        # تغليف لوحة التحكم داخل بطاقة زجاجية لتحسين المظهر
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        render_dashboard(user)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
