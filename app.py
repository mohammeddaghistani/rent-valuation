import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# --- 1. إعدادات الهوية والشعار بناءً على ملفك المرفق ---
LOGO_URL = "https://mdaghistani.com/wp-content/uploads/2023/05/logo-gold.png" # رابط شعارك الرسمي

st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=LOGO_URL,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. محرك التنسيق "الهيبة والرشاقة" (Elite Slim RTL) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* الإعدادات العامة والاتجاه */
    html, body, .stApp {{
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }}

    /* الرشاقة القصوى للخانات (Slim Design) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"], .stTextArea textarea {{
        height: 32px !important; /* حجم نحيف جداً واحترافي */
        padding: 0px 10px !important;
        font-size: 0.85rem !important;
        border-radius: 4px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
        direction: rtl !important;
    }}

    /* عناوين الخانات (Labels) - صغيرة وأنيقة */
    label {{
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        color: #b45309 !important; /* لون ذهبي الشعار */
        margin-bottom: 2px !important;
    }}

    /* التبويبات (Tabs) - تبدأ من اليمين بنمط Apple */
    .stTabs [data-baseweb="tab-list"] {{
        direction: rtl !important;
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 12px;
        background-color: #f8fafc;
        padding: 5px;
        border-radius: 8px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: transparent !important;
        color: #64748b !important;
        font-weight: 600 !important;
        height: 35px !important;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: white !important;
        color: #065f46 !important; /* أخضر الشعار */
        border-radius: 6px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}

    /* الأزرار الملكية النحيفة */
    div.stButton > button {{
        height: 35px !important;
        background: #1e293b !important; /* أسود ملكي */
        color: #b45309 !important; /* كتابة ذهبية */
        border: 1px solid #b45309 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
    }}

    /* إخفاء الزوائد التقنية */
    #MainMenu, footer, header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# --- 3. محرك العمليات (Logic) ---
def render_satellite_map():
    # إحداثيات مكة المكرمة
    m = folium.Map(location=[21.4225, 39.8262], zoom_start=16)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}',
        attr='Esri Satellite', name='ساتلايت'
    ).add_to(m)
    st_folium(m, width="100%", height=400)

# --- 4. الهيكل الرئيسي للتطبيق ---
def main():
    # الهيدر الفخم المستوحى من ملف HTML الخاص بك
    st.markdown(f"""
        <div style="text-align:center; padding-bottom:15px;">
            <img src="{LOGO_URL}" width="65" style="margin-bottom:10px;">
            <h1 style="font-family:'Amiri', serif; color:#b45309; font-size:2.4rem; margin:0;">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#065f46; font-size:0.95rem; font-weight:700; margin-top:-5px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div style="width:50px; height:2px; background:linear-gradient(to left, #b45309, #065f46); margin:10px auto;"></div>
        </div>
    """, unsafe_allow_html=True)

    # التحقق من الدخول (باستخدام نظامك الأصلي)
    try:
        from modules.auth import login_required
        user = login_required()
    except:
        st.warning("⚠️ يرجى التأكد من رفع موديول auth وضبط Secrets الدخول.")
        return

    if user:
        # التبويبات بنظام RTL الحقيقي
        tab1, tab2, tab3 = st.tabs(["📊 البيانات والعمليات", "📍 المعاينة الجيو-مكانية", "💼 الأرشيف والإدارة"])

        with tab1:
            st.markdown("<p style='color:#b45309; font-weight:bold;'>عملية تقدير جديدة</p>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text_input("اسم العقار / العميل")
            with col2:
                st.number_input("المساحة الإجمالية", value=0.0)
            with col3:
                st.selectbox("نوع النشاط", ["تجاري", "سكني", "إداري"])
            
            st.button("حفظ البيانات وتوليد التقرير")

        with tab2:
            st.markdown("<p style='color:#b45309; font-weight:bold;'>معاينة الأقمار الصناعية (Satellite)</p>", unsafe_allow_html=True)
            render_satellite_map()

        with tab3:
            st.info("سجل العمليات والتقارير المؤرشفة.")

if __name__ == "__main__":
    main()
