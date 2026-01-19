import streamlit as st

# 1. تهيئة النظام واستدعاء الموديولات الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"خطأ في تحميل المكونات: {e}")
    st.stop()

# 2. إعدادات التبويب والأيقونة (أعلى المتصفح)
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق العالمي (Global Luxury UI)
# يعتمد على التباين العالي، الخطوط الانسيابية، وتجربة Mobile-First
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&family=Amiri:wght@700&display=swap');

    /* التصميم العام والاتجاه العربي */
    html, body, [data-testid="stAppViewContainer"] {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background: #f8fafc !important; /* خلفية هادئة تبرز العناصر الذهبية */
    }

    /* تنسيق العناوين (نظام سيادي) */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important; /* ذهبي ملكي مطفي */
        font-size: clamp(2rem, 5vw, 3.5rem) !important;
        margin-bottom: 0px !important;
        text-align: center;
    }
    
    .brand-subtitle {
        color: #1e293b !important;
        font-size: clamp(1rem, 2vw, 1.4rem) !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
    }

    /* تطوير التبويبات (Tabs) لتكون أزرار تفاعلية فخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #ffffff;
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f1f5f9;
        border-radius: 10px;
        color: #64748b;
        font-weight: 700;
        border: none;
        transition: 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3);
    }

    /* تنسيق الجداول (الخلايا) لتكون واضحة واحترافية */
    .stDataFrame, div[data-testid="stTable"] {
        border-radius: 15px !important;
        border: 1px solid #e2e8f0 !important;
        overflow: hidden;
    }
    
    /* الأزرار الذهبية التفاعلية */
    div.stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #8b6b06 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 900 !important;
        height: 3.5rem;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(184, 134, 11, 0.4) !important;
    }

    /* إخفاء الزوائد التقنية */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* الخريطة (الساتلايت مدمج برمجياً) */
    .folium-map { border-radius: 20px !important; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

def main():
    # 1. تهيئة قاعدة البيانات
    init_db()
    ensure_settings()

    # 2. الهيدر الرسمي الاحترافي
    st.markdown("""
        <div style="text-align:center; padding:20px 0;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p class="brand-subtitle">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div style="width:60px; height:4px; background:#B8860B; margin: 0 auto 40px auto; border-radius:10px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # 3. نظام الدخول المحمي
    user = login_required()
    
    if user:
        # تشغيل لوحة التحكم (Dashboard)
        # ميزة "خريطة الساتلايت" تعمل تلقائياً داخل موديول الخريطة
        render_dashboard(user)

if __name__ == "__main__":
    main()
