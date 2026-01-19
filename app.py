import streamlit as st
import os

# 1. استيراد الموديولات الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل النظام: {e}")
    st.stop()

# 2. إعدادات الصفحة والشعار (أيقونة التبويب)
# تأكد من رفع ملف logo.png في GitHub ليظهر شعارك
logo_path = "logo.png"
page_icon = logo_path if os.path.exists(logo_path) else "⚜️"

st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العالمي (Slim & Professional RTL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Amiri:wght@700&display=swap');

    /* الاتجاه والخلفية البيضاء */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }

    /* تصغير الخانات وجعلها نحيفة وأنيقة (Slim Style) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"], .stTextArea textarea {
        height: 38px !important; /* حجم نحيف واحترافي */
        padding: 5px 12px !important;
        font-size: 0.95rem !important;
        border-radius: 6px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
        direction: rtl !important;
    }

    /* عناوين الخانات (Labels) - تصغير الخط ليعطي هيبة */
    label {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #B8860B !important;
        margin-bottom: 2px !important;
    }

    /* التبويبات (Tabs) - نحيفة ومنظمة من اليمين */
    .stTabs [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 5px !important;
        background-color: transparent !important;
        border-bottom: 2px solid #f1f5f9 !important;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px !important;
        font-size: 0.9rem !important;
        padding: 0 15px !important;
        border: none !important;
        background-color: transparent !important;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #B8860B !important;
        color: #B8860B !important;
        font-weight: 700 !important;
    }

    /* الأزرار - أنيقة وغير ضخمة */
    div.stButton > button {
        height: 40px !important;
        width: auto !important;
        min-width: 150px !important;
        background: #1a1a1a !important; /* أسود ملكي */
        color: #B8860B !important; /* كتابة ذهبية */
        border: 1px solid #B8860B !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        margin-top: 10px !important;
    }
    div.stButton > button:hover {
        background: #B8860B !important;
        color: #ffffff !important;
    }

    /* الخريطة (ساتلايت افتراضي) */
    .folium-map { border-radius: 10px !important; }

    /* إخفاء زوائد ستريمليت */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def main():
    init_db()
    ensure_settings()

    # الهيدر (رأس الصفحة)
    st.markdown("""
        <div style="text-align:center; padding:20px 0 10px 0;">
            <h1 style="font-family:'Amiri', serif; color:#B8860B; font-size:2.8rem; margin:0;">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-size:1rem; font-weight:600; margin-top:-5px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
        </div>
    """, unsafe_allow_html=True)

    user = login_required()
    if user:
        # استدعاء لوحة التحكم (التي ستظهر فيها الخريطة والتبويبات المحدثة)
        render_dashboard(user)

if __name__ == "__main__":
    main()
