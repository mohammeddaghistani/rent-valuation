import streamlit as st

# 1. تهيئة النظام واستدعاء الموديولات
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"خطأ في تحميل المكونات: {e}")
    st.stop()

# 2. إعدادات الصفحة المتقدمة للهواتف (Mobile-First)
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العالمي (UI/UX Mobile Optimization)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

    /* تحسين الواجهة للجوال والاتجاه العربي */
    .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff;
    }

    /* تطوير التبويبات (Tabs) لتكون سهلة اللمس على الآيفون */
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        overflow-x: auto; /* السماح بالتمرير الأفقي في الجوال */
        background-color: #f1f5f9;
        padding: 5px;
        border-radius: 12px;
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        flex: 1;
        min-width: 100px;
        height: 45px;
        background-color: white;
        border-radius: 8px;
        color: #1e293b;
        font-weight: 700;
        border: 1px solid #e2e8f0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        border: none !important;
    }

    /* تحسين شكل الجداول والبيانات المالية (Luxury Grid) */
    .stDataFrame, div[data-testid="stTable"] {
        border-radius: 12px !important;
        border: 1px solid #B8860B !important;
    }
    
    /* تنسيق خريطة الساتلايت */
    .folium-map { border-radius: 15px !important; }

    /* إخفاء الزوائد لمنع التشتت */
    #MainMenu, footer, header {visibility: hidden;}

    /* ضبط الهوامش للجوال */
    @media (max-width: 768px) {
        .block-container { padding: 1rem !important; }
        h1 { font-size: 1.8rem !important; }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # تهيئة قاعدة البيانات
    init_db()
    ensure_settings()

    # شعار الصفحة المطور (Responsive Header)
    st.markdown("""
    <div style="text-align:center; padding:15px 0;">
        <h1 style="margin:0; font-size: 2.5rem; color:#B8860B;">محمد داغستاني للتقييم العقاري</h1>
        <p style="color:#B8860B; font-size:1.1rem; font-weight:700; margin-top:5px;">
            نظام إدارة العلاقات والتقدير الإيجاري الاستثماري
        </p>
        <div style="width:60px; height:2px; background:#1e293b; margin:10px auto; border-radius:5px;"></div>
    </div>
    """, unsafe_allow_html=True)

    # التحقق من تسجيل الدخول
    user = login_required()
    
    if user:
        # ملاحظة برمجية: ميزة الساتلايت تمت برمجتها داخل موديول الخريطة 
        # لتعمل تلقائياً عند عرض لوحة التحكم.
        render_dashboard(user)

if __name__ == "__main__":
    main()
