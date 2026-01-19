import streamlit as st
import os

# 1. استيراد الموديولات الأساسية لضمان عمل كافة الوظائف
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل ملفات النظام: {e}")
    st.stop()

# 2. إعدادات الصفحة وأيقونة التبويب (شعارك)
# تأكد من رفع ملف logo.png في المجلد الرئيسي على GitHub ليظهر تلقائياً
logo_path = "logo.png"
page_icon = logo_path if os.path.exists(logo_path) else "⚜️"

st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العالمي (Luxury Slim RTL UI)
# تصميم بدون كحلي، يعتمد على الأبيض الصافي والذهبي الملكي
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه من اليمين لليسار والخلفية البيضاء */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }

    /* إصلاح العناوين لتكون سيادية وغير مكررة */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2rem, 5vw, 3rem) !important;
        text-align: center !important;
        margin-bottom: 5px !important;
        font-weight: 700 !important;
    }

    /* تصغير الخانات لتصبح نحيفة ومرتبة (Professional Slim) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"], .stTextArea textarea {
        height: 38px !important; /* حجم رشيق واحترافي */
        padding: 5px 12px !important;
        font-size: 0.95rem !important;
        border-radius: 8px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
        direction: rtl !important;
        color: #1a1a1a !important;
    }

    /* عناوين الخانات (Labels) - صغيرة وأنيقة */
    label {
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        color: #B8860B !important;
        margin-bottom: 2px !important;
    }

    /* تطوير التبويبات (Tabs) لتكون موجهة للجوال وتبدأ من اليمين */
    .stTabs [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row-reverse !important; /* تبدأ من اليمين */
        gap: 5px !important;
        background-color: #f8fafc !important;
        padding: 5px !important;
        border-radius: 10px !important;
        overflow-x: auto !important; /* السماح بالتمرير في الجوال */
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 6px !important;
        height: 40px !important;
        font-size: 0.9rem !important;
        min-width: 100px !important;
        color: #64748b !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        border: none !important;
    }

    /* الأزرار الذهبية (تصميم نحيف فخم) */
    div.stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #8b6b06 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        height: 42px !important;
        font-size: 1rem !important;
        border: none !important;
        width: 100% !important;
    }

    /* إخفاء الزوائد التقنية لتعزيز الهيبة */
    #MainMenu, footer, header {visibility: hidden;}

    /* تنسيق الجداول لتكون نظيفة وواضحة جداً */
    .stDataFrame { border: 1px solid #e2e8f0 !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

def main():
    # تهيئة قاعدة البيانات والإعدادات
    init_db()
    ensure_settings()

    # شعار "محمد داغستاني للتقييم العقاري" الرسمي
    st.markdown("""
        <div style="text-align:center; padding:20px 0;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-weight:700; font-size:1.1rem; margin-top:-5px;">
                نظام إدارة العلاقات والتقدير الإيجاري الاستثماري
            </p>
            <div style="width:60px; height:2px; background:#B8860B; margin: 10px auto;"></div>
        </div>
    """, unsafe_allow_html=True)

    # التحقق من تسجيل الدخول وتشغيل لوحة التحكم
    user = login_required()
    if user:
        # لوحة التحكم تحتوي الآن على ميزة الخريطة "ساتلايت" والتبويبات المحدثة
        render_dashboard(user)

if __name__ == "__main__":
    main()
