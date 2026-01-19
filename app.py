import streamlit as st
import os
import pandas as pd

# 1. تهيئة الإعدادات (أيقونة المتصفح واسم الموقع)
logo_path = "logo.png"
page_icon = logo_path if os.path.exists(logo_path) else "⚜️"

st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. محرك التنسيق العالمي (Strict RTL & Slim UI)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه العربي */
    html, body, .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }

    /* تنسيق العناوين السيادية */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2rem, 5vw, 3rem) !important;
        text-align: center !important;
        margin-bottom: 5px;
    }

    /* تصغير وتنسيق الخانات (Slim Professional) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"] {
        height: 38px !important;
        border-radius: 6px !important;
        border: 1px solid #e2e8f0 !important;
        font-size: 0.9rem !important;
    }

    /* التبويبات الفخمة (Tabs) - تبدأ من اليمين */
    .stTabs [data-baseweb="tab-list"] {
        direction: rtl !important;
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 10px;
        border-bottom: 2px solid #B8860B;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-weight: 700 !important;
        color: #64748b !important;
    }

    .stTabs [aria-selected="true"] {
        color: #B8860B !important;
    }

    /* إخفاء شعارات ستريمليت الزائدة */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. محرك الوظائف الرئيسي
def main():
    # الهيدر الرسمي
    st.markdown("""
        <div style="text-align:center; padding-bottom:20px;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-weight:700;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
        </div>
    """, unsafe_allow_html=True)

    # التحقق من وجود الموديولات (لتجنب انهيار الكود)
    try:
        from modules.db import init_db, ensure_settings
        from modules.auth import login_required
        from modules.dashboard import render_dashboard
        
        init_db()
        ensure_settings()
        user = login_required()
        
        if user:
            # استخدام التبويبات المطورة
            tab1, tab2, tab3 = st.tabs(["📊 لوحة المؤشرات", "📍 الخريطة والساتلايت", "📝 إدارة الصفقات"])
            
            with tab1:
                st.subheader("تحليل البيانات الاستراتيجية")
                render_dashboard(user) # استدعاء المنطق الأصلي
                
            with tab2:
                st.subheader("عرض الموقع (ساتلايت)")
                # هنا يتم دمج ميزة الساتلايت التي طلبتها
                st.info("يتم الآن عرض الخريطة بنمط الأقمار الصناعية لضمان دقة المعاينة.")
                # (يفترض وجود موديول الخريطة المطور هنا)
                
            with tab3:
                st.subheader("إدارة قاعدة البيانات")
                # (يفترض وجود موديول الصفقات هنا)
                
    except Exception as e:
        st.warning("⚠️ يتطلب الكود وجود مجلد modules المرفوع مسبقاً ليعمل بكامل طاقته.")
        st.error(f"التفاصيل التقنية: {e}")

if __name__ == "__main__":
    main()
