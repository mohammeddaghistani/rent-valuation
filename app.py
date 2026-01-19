import streamlit as st

# استيراد الوظائف الأساسية - معالجة الخطأ لضمان استمرارية التطبيق
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"خطأ في تحميل الملفات البرمجية: {e}")
    st.stop()

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="M. DAGHISTANI CRM",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. محرك التنسيق العربي الموحد (RTL Engine)
# هذا الجزء يضمن عدم التكرار وضبط الاتجاه من اليمين لليسار
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    /* ضبط اتجاه التطبيق بالكامل */
    .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif !important;
        background-color: #f8fafc; /* خلفية هادئة واحترافية */
    }

    /* إصلاح اتجاه النصوص في الحقول والقوائم */
    input, select, textarea, label {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* تنسيق العناوين (دون تكرار) */
    h1, h2, h3 {
        color: #B8860B !important; /* ذهبي ملكي */
        text-align: center !important;
        margin-bottom: 1rem !important;
    }

    /* تنسيق الجداول لتكون واضحة واحترافية */
    .stDataFrame, table {
        direction: rtl !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* تنسيق الأزرار (تصميم موحد وغير متكرر) */
    div.stButton > button {
        width: 100%;
        background-color: #B8860B !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: none !important;
        height: 3rem;
    }

    /* إخفاء أي عناصر تكرار ناتجة عن التنسيقات القديمة */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def main():
    # تشغيل قاعدة البيانات والإعدادات مرة واحدة فقط
    init_db()
    ensure_settings()

    # الهيدر الاحترافي (إصلاح العبارات)
    st.markdown("""
    <div style="text-align:center; padding:20px 0;">
        <h1 style="margin:0;">محمد داغستاني للتقييم العقاري</h1>
        <p style="color:#64748b; font-size:1.1rem; margin-top:5px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
        <div style="width:100px; height:2px; background:#B8860B; margin:10px auto;"></div>
    </div>
    """, unsafe_allow_html=True)

    # التحقق من الدخول وتشغيل لوحة التحكم
    user = login_required()
    if user:
        # استدعاء لوحة التحكم الأصلية دون تعديل وظائفها
        render_dashboard(user)

if __name__ == "__main__":
    main()
