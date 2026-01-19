import streamlit as st

# 1. استيراد الموديولات الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل النظام: {e}")
    st.stop()

# 2. إعدادات الصفحة (أيقونة الشعار والتبويب)
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon="⚜️", # يمكنك استبدالها برابط شعارك المباشر لاحقاً
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق النهائي (RTL + التبويبات المطورة)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    /* ضبط اتجاه الواجهة RTL */
    .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff;
    }

    /* تطوير شكل التبويبات (Tabs) لتكون فخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: #f8fafc;
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre;
        background-color: white;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        color: #64748b;
        font-weight: 700;
        transition: 0.3s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.2);
    }

    /* تنسيق العناوين السيادية */
    h1, h2, h3 {
        color: #B8860B !important;
        text-align: center !important;
        font-weight: 900 !important;
    }

    /* إخفاء عناصر Streamlit لمنع التكرار */
    #MainMenu, footer, header {visibility: hidden;}

    /* ضبط الحقول لتناسب الجوال */
    input, select, .stSelectbox {
        direction: rtl !important;
        text-align: right !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # تهيئة قاعدة البيانات
    init_db()
    ensure_settings()

    # الهيدر المعتمد (محمد داغستاني للتقييم العقاري)
    st.markdown("""
    <div style="text-align:center; padding:20px 0;">
        <h1 style="margin:0; font-size: 3.2rem;">محمد داغستاني للتقييم العقاري</h1>
        <p style="color:#B8860B; font-size:1.4rem; font-weight:700; margin-top:5px;">
            نظام إدارة العلاقات والتقدير الإيجاري الاستثماري
        </p>
        <div style="width:120px; height:3px; background:#1a1a1a; margin:15px auto; border-radius:5px;"></div>
    </div>
    """, unsafe_allow_html=True)

    # التحقق من الدخول
    user = login_required()
    
    if user:
        # عرض لوحة التحكم الأصلية (التبويبات ستأخذ التنسيق الجديد تلقائياً)
        render_dashboard(user)

if __name__ == "__main__":
    main()
