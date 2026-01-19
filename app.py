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

# --- إعداد الشعار (Logo) كأيقونة للتبويب ---
# سنحاول البحث عن ملف الشعار في مجلداتك
logo_path = "logo.png" # تأكد من مطابقة اسم الملف المرفوع في GitHub
if not os.path.exists(logo_path):
    # إذا لم يجد الملف، سيستخدم الرمز الملكي مؤقتاً
    page_icon = "⚜️"
else:
    page_icon = logo_path

# 2. إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق "الفخامة البيضاء والذهبية" (Strict RTL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه من اليمين لليسار والخلفية البيضاء الصافية */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
        color: #1e293b !important;
    }

    /* تنسيق الخانات (Inputs) لتكون متناسقة واحترافية (بدون كحلي) */
    input, select, textarea, .stSelectbox, .stTextInput, .stNumberInput {
        direction: rtl !important;
        text-align: right !important;
        background-color: #fcfcfc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        height: 50px !important;
        font-size: 1rem !important;
    }

    /* العناوين الملكية */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2rem, 5vw, 3.5rem) !important;
        text-align: center !important;
        margin-bottom: 5px !important;
    }

    /* التبويبات المطورة (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row-reverse !important;
        background-color: #f8fafc !important;
        padding: 10px !important;
        border-radius: 12px !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 8px 20px !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
    }

    /* الأزرار الذهبية الفخمة */
    div.stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #8b6b06 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: 900 !important;
        border: none !important;
        height: 3.2rem !important;
        width: 100% !important;
    }

    /* إخفاء الزوائد */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def main():
    init_db()
    ensure_settings()

    # الهيدر الرسمي
    st.markdown("""
        <div style="text-align:center; padding:30px 0;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-weight:700;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
        </div>
    """, unsafe_allow_html=True)

    user = login_required()
    if user:
        render_dashboard(user)

if __name__ == "__main__":
    main()
