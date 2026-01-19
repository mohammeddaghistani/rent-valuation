import streamlit as st

# 1. استيراد الموديولات الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل النظام: {e}")
    st.stop()

# 2. إعدادات التبويب والأيقونة
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العربي الصارم (Strict RTL & Luxury UI)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه من اليمين لليسار على كامل التطبيق */
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #fcfcfc !important;
    }

    /* إصلاح كافة حقول الإدخال والقوائم لتكون يمين-إلى-يسار */
    input, select, textarea, label, div[data-baseweb="select"], .stSelectbox, .stTextInput, .stNumberInput {
        direction: rtl !important;
        text-align: right !important;
    }

    /* تنسيق العناوين السيادية (بالخط الأميري الفخم) */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2.2rem, 5vw, 3.8rem) !important;
        text-align: center !important;
        margin: 0 !important;
        font-weight: 700 !important;
    }
    
    .brand-subtitle {
        color: #1e293b !important;
        font-size: clamp(1rem, 2vw, 1.4rem) !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin-top: -10px !important;
    }

    /* تطوير التبويبات (Tabs) بشكل احترافي عالمي */
    .stTabs [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row-reverse !important; /* لتبدأ التبويبات من اليمين */
        gap: 10px !important;
        background-color: #ffffff !important;
        padding: 8px !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f5f9 !important;
        border-radius: 8px !important;
        color: #64748b !important;
        font-weight: 700 !important;
        padding: 10px 20px !important;
        border: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        box-shadow: 0 4px 10px rgba(184, 134, 11, 0.3) !important;
    }

    /* الأزرار الذهبية (تأثير معدني فخم) */
    div.stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #8b6b06 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        border: none !important;
        height: 3.5rem !important;
        width: 100% !important;
    }

    /* إخفاء الزوائد التقنية لتعزيز الفخامة */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* تحسين شكل الجداول والبيانات */
    .stDataFrame {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # تهيئة قاعدة البيانات
    init_db()
    ensure_settings()

    # الهيدر المطور (محمد داغستاني للتقييم العقاري)
    st.markdown("""
        <div style="text-align:center; padding:30px 0;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p class="brand-subtitle">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div style="width:70px; height:3px; background:#B8860B; margin: 15px auto; border-radius:10px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # نظام تسجيل الدخول المحمي
    user = login_required()
    
    if user:
        # لوحة التحكم - ميزة الساتلايت مدمجة في موديول الخريطة
        render_dashboard(user)

if __name__ == "__main__":
    main()
