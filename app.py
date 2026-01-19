import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# --- 1. إعدادات الهوية واللوجو ---
logo_url = "https://mdaghistani.com/wp-content/uploads/2023/05/logo-gold.png"
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=logo_url,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. محرك التنسيق العالمي الصارم (Strict RTL & Slim UI) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Amiri:wght@700&display=swap');

    /* ضبط اتجاه التطبيق بالكامل ليقرأ من اليمين لليسار */
    html, body, .stApp, [data-testid="stAppViewContainer"] {{
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }}

    /* تصغير الخانات (Slim) وجعل النص بداخلها يبدأ من اليمين */
    input, select, textarea, [data-baseweb="select"] {{
        direction: rtl !important;
        text-align: right !important;
        height: 35px !important;
        font-size: 0.9rem !important;
        border-radius: 4px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
    }}

    /* ضبط اتجاه حقول النصوص الخاصة بـ Streamlit */
    .stTextInput div, .stNumberInput div, .stSelectbox div {{
        direction: rtl !important;
    }}

    /* تسميات الخانات (Labels) - صغيرة وأنيقة للهيبة */
    label {{
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        color: #B8860B !important;
        margin-bottom: 2px !important;
        display: block !important;
        width: 100% !important;
        text-align: right !important;
    }}

    /* التبويبات (Tabs) - تبدأ من اليمين بشكل حقيقي */
    .stTabs [data-baseweb="tab-list"] {{
        flex-direction: row-reverse !important;
        justify-content: flex-end !important;
        gap: 15px !important;
        border-bottom: 2px solid #f1f5f9 !important;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        height: 40px !important;
        padding: 0 15px !important;
        font-weight: 700 !important;
        color: #64748b !important;
    }}

    .stTabs [aria-selected="true"] {{
        color: #B8860B !important;
        border-bottom-color: #B8860B !important;
    }}

    /* الأزرار الملكية - رشاقة وهيبة */
    div.stButton > button {{
        height: 36px !important;
        background: #1a1a1a !important;
        color: #B8860B !important;
        border: 1px solid #B8860B !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        width: 100% !important;
    }}

    /* إخفاء الزوائد */
    #MainMenu, footer, header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# --- 3. وظائف النظام (Logic) ---
def render_satellite_map():
    # إحداثيات افتراضية (مكة المكرمة)
    m = folium.Map(location=[21.4225, 39.8262], zoom_start=16)
    # إضافة طبقة الساتلايت العالمية
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Satellite',
        name='الأقمار الصناعية'
    ).add_to(m)
    st_folium(m, width="100%", height=400)

# --- 4. الصفحة الرئيسية ---
def main():
    # الهيدر الاحترافي
    st.markdown(f"""
        <div style="text-align:center; padding-bottom:15px;">
            <img src="{logo_url}" width="70">
            <h1 style="font-family:'Amiri', serif; color:#B8860B; font-size:2.4rem; margin:0;">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-size:0.95rem; font-weight:700; margin-top:-5px;">نظام التقدير الإيجاري الاستثماري الذكي</p>
        </div>
    """, unsafe_allow_html=True)

    # محاكاة الدخول لضمان عدم فقدان الخصائص (يمكن ربطها بملف auth الأصلي)
    is_logged_in = True 
    
    if is_logged_in:
        # التبويبات تبدأ من اليمين
        tab1, tab2, tab3, tab4 = st.tabs(["📊 المؤشرات", "📍 المعاينة", "📝 العمليات", "⚙️ الإعدادات"])
        
        with tab1:
            st.markdown("<p style='color:#B8860B; font-weight:700;'>لوحة تحليل البيانات</p>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("إجمالي التقييمات", "452", "+12")
            with col2:
                st.metric("متوسط سعر المتر", "3,200 ر.س", "ثابت")
            with col3:
                st.metric("نسبة النمو", "8.4%", "+1.2%")

        with tab2:
            st.markdown("<p style='color:#B8860B; font-weight:700;'>خريطة المعاينة (ساتلايت)</p>", unsafe_allow_html=True)
            render_satellite_map()

        with tab3:
            st.markdown("<p style='color:#B8860B; font-weight:700;'>إدخال بيانات صفقة جديدة</p>", unsafe_allow_html=True)
            # نموذج إدخال نحيف وأنيق (Slim UI)
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("اسم العقار / العميل")
                st.number_input("مساحة العقار (م2)", min_value=0)
            with c2:
                st.selectbox("نوع العقار", ["سكني", "تجاري", "إداري", "صناعي"])
                st.date_input("تاريخ المعاينة")
            
            st.button("حفظ الصفقة وتوليد التقييم")

        with tab4:
            st.info("إعدادات النظام والتحكم في المستخدمين.")

if __name__ == "__main__":
    main()
