import streamlit as st

# 1. استيراد الموديولات الأساسية (مع معالجة الأخطاء)
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل ملفات النظام الأساسية: {e}")
    st.stop()

# 2. إعدادات الصفحة (التوافق مع الأجهزة المحمولة)
st.set_page_config(
    page_title="م. داغستاني | نظام التقدير العقاري",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التصميم الموحد (RTL & Professional Style)
# تم ضبط الاتجاه RTL ومنع تكرار أي عناصر
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    /* ضبط اتجاه الواجهة بالكامل من اليمين لليسار */
    .stApp, div[data-testid="stAppViewContainer"] {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff; /* خلفية بيضاء نظيفة للاحترافية */
    }

    /* إصلاح اتجاه حقول الإدخال والقوائم */
    input, select, textarea, label, .stSelectbox, div[role="listbox"] {
        direction: rtl !important;
        text-align: right !important;
    }

    /* تنسيق العناوين السيادية */
    h1, h2, h3 {
        color: #B8860B !important; /* ذهبي ملكي */
        text-align: center !important;
        font-weight: 900 !important;
    }

    /* تنسيق الجداول (الخلايا) لتكون واضحة واحترافية */
    .stDataFrame, table {
        direction: rtl !important;
        border: 1px solid #f0f0f0 !important;
    }
    
    /* الأزرار الذهبية الموحدة */
    div.stButton > button {
        width: 100%;
        background-color: #B8860B !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        border: none !important;
        height: 3.2rem;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1a1a1a !important; /* يتحول للأسود الفخم عند التمرير */
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* إخفاء عناصر Streamlit الزائدة لمنع التشتت */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* تحسين ظهور العناصر على الآيفون والجوال */
    @media (max-width: 768px) {
        .block-container { padding: 1rem !important; }
        h1 { font-size: 1.8rem !important; }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # تشغيل قاعدة البيانات (مرة واحدة فقط)
    init_db()
    ensure_settings()

    # الهيدر الاحترافي (صياغة مصلحة)
    st.markdown("""
    <div style="text-align:center; padding:30px 0;">
        <h1 style="margin:0; font-size: 3rem;">محمد داغستاني</h1>
        <p style="color:#B8860B; font-size:1.3rem; font-weight:700; margin-top:5px;">
            نظام التقدير الإيجاري الذكي للعقارات الاستثمارية
        </p>
        <p style="color:#64748b; font-size:0.9rem; margin-top:-10px;">
            من مكة المكرمة.. نصلكم بالعالم
        </p>
        <div style="width:80px; height:3px; background:#1a1a1a; margin:15px auto; border-radius:5px;"></div>
    </div>
    """, unsafe_allow_html=True)

    # التحقق من تسجيل الدخول (استدعاء موديول الأمان الأصلي)
    user = login_required()
    
    if user:
        # تشغيل لوحة التحكم الرئيسية (بدون فقدان أي ميزة)
        render_dashboard(user)

if __name__ == "__main__":
    main()
