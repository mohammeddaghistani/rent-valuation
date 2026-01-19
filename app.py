import streamlit as st
# استيراد الوظائف الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("خطأ تقني: تأكد من وجود مجلد modules كاملاً.")

# --- 1. إعدادات الهوية البصرية الموحدة (تصميم mdaghistani.com) ---
st.set_page_config(page_title="M. DAGHISTANI | التقدير العقاري", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* الألوان الرسمية */
    :root {
        --deep-blue: #0a192f;
        --gold-accent: #c2974d;
        --pure-white: #FFFFFF;
        --glass-bg: rgba(255, 255, 255, 0.03);
    }

    /* تهيئة الخلفية العامة */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, var(--deep-blue) 100%) !important;
        color: var(--pure-white) !important;
    }

    /* توحيد الخطوط وتعديل الاتجاه */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* تحسين العناوين الذهبية */
    h1, h2, h3, .stHeader {
        font-family: 'Amiri', serif !important;
        color: var(--gold-accent) !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* حل مشكلة ألوان حقول الإدخال غير المتناسقة */
    .stTextInput input, .stNumberInput input, .stSelectbox div, .stTextArea textarea {
        color: var(--pure-white) !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid var(--gold-accent) !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }

    /* تعديل لون "الليبل" (عناوين الحقول) */
    label {
        color: var(--gold-accent) !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }

    /* تنسيق الأزرار الذهبية بشكل احترافي */
    div.stButton > button {
        background: linear-gradient(135deg, #c2974d, #e0ac52) !important;
        color: var(--deep-blue) !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        width: 100%;
        transition: 0.4s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(194, 151, 77, 0.4) !important;
    }

    /* تحسين شكل البطاقات (Cards) لتكون زجاجية متناسقة */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: var(--glass-bg) !important;
        border: 1px solid rgba(194, 151, 77, 0.2) !important;
        border-radius: 10px 10px 0 0 !important;
        color: var(--pure-white) !important;
        padding: 10px 30px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--gold-accent) !important;
        color: var(--deep-blue) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الهيكل البرمجي (دون تغيير في الوظائف) ---
def main():
    # 1. تهيئة النظام
    init_db()
    ensure_settings()
    
    # 2. الهيدر (الشعار)
    st.markdown("""
        <div style="text-align: center; padding: 30px 0;">
            <h1 style="font-size: 3.8rem; margin: 0;">م. داغستاني</h1>
            <p style="color: #c2974d; font-size: 1.4rem; font-weight: 700; margin-top: -10px;">
                من مكة المكرمة.. نصلكم بالعالم
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 3. تشغيل الدخول واللوحة
    user = login_required()
    if user:
        # هنا يتم عرض لوحة التحكم (render_dashboard)
        # سيتم تطبيق التنسيقات أعلاه تلقائياً على كل عناصرها
        render_dashboard(user)

if __name__ == "__main__":
    main()
