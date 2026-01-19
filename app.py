import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# 1. إعدادات الهوية (أيقونة التبويب والشعار)
st.set_page_config(
    page_title="M. DAGHISTANI | التقدير العقاري",
    page_icon="🦅", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. محرك التنسيق "نيومورفيزم ذهبي وأخضر" (Luxury Tech RTL)
# تم إلغاء الكحلي واستخدام الأبيض الصافي مع لمسات من أخضر وذهبي الشعار
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* الاتجاه العربي والخلفية النظيفة */
    html, body, .stApp {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }

    /* الخانات النحيفة (Professional Slim) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"] {
        height: 35px !important;
        padding: 2px 10px !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
        direction: rtl !important;
    }

    /* العناوين بهوية الشعار (ذهبي وأخضر) */
    .brand-title {
        font-family: 'Amiri', serif !important;
        color: #B8860B !important;
        font-size: clamp(2rem, 5vw, 3rem) !important;
        text-align: center !important;
        margin: 0 !important;
    }
    
    .tech-line {
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #B8860B, #228B22); /* تدرج ذهبي أخضر مثل الشعار */
        margin: 10px auto 30px auto;
        border-radius: 10px;
    }

    /* التبويبات المطورة (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        direction: rtl !important;
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 10px;
        background-color: #f8fafc;
        padding: 8px;
        border-radius: 12px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #B8860B !important;
        color: white !important;
        border-radius: 8px;
    }

    /* الأزرار الملكية (Slim Black & Gold) */
    div.stButton > button {
        height: 38px !important;
        background: #1a1a1a !important;
        color: #B8860B !important;
        border: 1px solid #B8860B !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        width: 100% !important;
    }

    /* الجداول الاحترافية */
    .stDataFrame { border: 1px solid #e2e8f0 !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# 3. محرك العمليات والمعادلات (Logic Engine)
def calculate_valuation(area, price):
    # معادلة التقدير الأساسية
    return area * price

def render_satellite_map():
    # خريطة الأقمار الصناعية (Satellite)
    m = folium.Map(location=[21.4225, 39.8262], zoom_start=16)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Satellite', name='الساتلايت'
    ).add_to(m)
    st_folium(m, width="100%", height=400)

# 4. واجهة التطبيق الرئيسية
def main():
    # الهيدر (استدعاء شعارك المرفوع)
    st.markdown(f"""
        <div style="text-align:center; padding:20px;">
            <h1 class="brand-title">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#228B22; font-weight:700; margin-top:-10px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div class="tech-line"></div>
        </div>
    """, unsafe_allow_html=True)

    # التحقق من الدخول (باستخدام نظامك الأصلي)
    try:
        from modules.auth import login_required
        user = login_required()
    except:
        st.warning("⚠️ يرجى ضبط أسرار الدخول في Secrets.")
        return

    if user:
        # التبويبات بتنسيق اليمين لليسار (RTL)
        tab1, tab2, tab3 = st.tabs(["📊 لوحة العمليات", "📍 معاينة الساتلايت", "⚙️ الإدارة"])

        with tab1:
            st.markdown("<h4 style='color:#B8860B;'>إدخال بيانات التقدير</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("اسم العميل / العقار")
                area = st.number_input("المساحة الإجمالية (م2)", min_value=1.0)
            with col2:
                price = st.number_input("سعر المتر التقديري (ريال)", min_value=1.0)
                category = st.selectbox("نوع النشاط", ["تجاري", "سكني", "صناعي"])
            
            if st.button("تشغيل معادلة التقدير"):
                result = calculate_valuation(area, price)
                st.success(f"التقدير الإيجاري المقترح: {result:,.2f} ريال سعودي")

        with tab2:
            st.markdown("<h4 style='color:#B8860B;'>المعاينة الجيومكانية</h4>", unsafe_allow_html=True)
            render_satellite_map()

        with tab3:
            st.info("قسم إدارة الصفقات والأرشيف.")
            # مثال لجدول البيانات النحيف
            df = pd.DataFrame({"العقار": ["برج مكة", "مجمع تجاري"], "القيمة": ["5M", "12M"]})
            st.table(df)

if __name__ == "__main__":
    main()
