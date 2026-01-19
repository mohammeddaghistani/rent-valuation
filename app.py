import streamlit as st

# 1. استيراد الموديولات الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل النظام: {e}")
    st.stop()

# 2. إعدادات الصفحة (تبويب الصفحة والشعار)
st.set_page_config(
    page_title="محمد داغستاني ",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العالمي الفاخر (RTL & Luxury White Design)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه من اليمين لليسار والخلفية البيضاء */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important; /* خلفية بيضاء صافية */
        color: #1e293b !important;
    }

    /* تنسيق العناوين السيادية (ذهبي ملكي) */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2.2rem, 5vw, 3.8rem) !important;
        text-align: center !important;
        margin: 0 !important;
        font-weight: 700 !important;
    }
    
    .brand-subtitle {
        color: #64748b !important;
        font-size: clamp(1rem, 2vw, 1.4rem) !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin-top: -10px !important;
    }

    /* ضبط تناسق وأحجام الخانات (Inputs) لتبدو احترافية */
    input, select, textarea, div[data-baseweb="select"], .stSelectbox, .stTextInput, .stNumberInput {
        direction: rtl !important;
        text-align: right !important;
        background-color: #f8fafc !important; /* رمادي فاتح جداً للخانات */
        color: #1e293b !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        height: 55px !important; /* حجم موحد ومريح للمس في الجوال */
        font-size: 1.1rem !important;
    }
    
    /* ضبط تسمية الخانات (Labels) */
    label {
        color: #B8860B !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
        font-size: 1rem !important;
    }

    /* تطوير التبويبات (Tabs) بشكل عصري وعالمي */
    .stTabs [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 12px !important;
        background-color: #f1f5f9 !important;
        padding: 8px !important;
        border-radius: 15px !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white !important;
        border-radius: 10px !important;
        color: #64748b !important;
        font-weight: 700 !important;
        padding: 12px 25px !important;
        border: 1px solid #e2e8f0 !important;
        min-width: 120px !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(184, 134, 11, 0.3) !important;
    }

    /* الأزرار الذهبية (تصميم فخم) */
    div.stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #8b6b06 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        border: none !important;
        height: 3.5rem !important;
        width: 100% !important;
        font-size: 1.2rem !important;
        transition: 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(184, 134, 11, 0.4) !important;
    }

    /* إخفاء الزوائد التقنية لرفع الفخامة */
    #MainMenu, footer, header {visibility: hidden;}

    /* ضبط الجداول لتكون نظيفة جداً */
    .stDataFrame {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # تهيئة النظام
    init_db()
    ensure_settings()

    # الهيدر الرسمي الاحترافي (محمد داغستاني )
    st.markdown("""
        <div style="text-align:center; padding:40px 0;">
            <h1 class="brand-title">محمد داغستاني </h1>
            <p class="brand-subtitle">التقدير الإيجاري الاستثماري</p>
            <div style="width:80px; height:3px; background:#B8860B; margin: 15px auto; border-radius:10px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # نظام تسجيل الدخول المحمي
    user = login_required()
    
    if user:
        # تشغيل لوحة التحكم الأصلية
        # ميزة الساتلايت تعمل تلقائياً عبر التحكم في موديول الخريطة
        render_dashboard(user)

if __name__ == "__main__":
    main()
