import streamlit as st
import os
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. إعدادات الهوية والشعار
logo_url = "https://mdaghistani.com/wp-content/uploads/2023/05/logo-gold.png" # رابط شعارك من موقعك
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=logo_url,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. محرك التنسيق العالمي (Luxury Slim RTL - White Edition)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه العربي والخلفية البيضاء */
    html, body, .stApp {{
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }}

    /* الخانات النحيفة والأنيقة (Slim UI) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"], .stTextArea textarea {{
        height: 35px !important;
        min-height: 35px !important;
        padding: 2px 10px !important;
        font-size: 0.9rem !important;
        border-radius: 4px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: #fcfcfc !important;
    }}

    /* تصغير العناوين الفرعية للهيبة */
    label {{
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        color: #B8860B !important;
        margin-bottom: 2px !important;
    }}

    /* التبويبات الفخمة بنظام الخط السفلي */
    .stTabs [data-baseweb="tab-list"] {{
        direction: rtl !important;
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 20px;
        border-bottom: 1px solid #f1f5f9;
    }}
    .stTabs [data-baseweb="tab"] {{
        height: 40px !important;
        font-weight: 700 !important;
        background-color: transparent !important;
        border: none !important;
        color: #64748b !important;
    }}
    .stTabs [aria-selected="true"] {{
        border-bottom: 3px solid #B8860B !important;
        color: #B8860B !important;
    }}

    /* الأزرار الملكية النحيفة */
    div.stButton > button {{
        height: 38px !important;
        background: #1a1a1a !important;
        color: #B8860B !important;
        border: 1px solid #B8860B !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
    }}

    /* إخفاء الزوائد */
    #MainMenu, footer, header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# 3. دالة الخريطة المطورة (ساتلايت)
def render_professional_map():
    # إحداثيات افتراضية (مكة المكرمة)
    m = folium.Map(location=[21.4225, 39.8262], zoom_start=15)
    
    # إضافة خريطة الساتلايت من Esri
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='صور الأقمار الصناعية (Satellite)',
        overlay=False,
        control=True
    ).add_to(m)
    
    # إضافة التحكم في الطبقات
    folium.LayerControl(position='topleft').add_to(m)
    
    st_folium(m, width="100%", height=400)

# 4. محرك النظام الرئيسي
def main():
    # الهيدر الفخم
    st.markdown(f"""
        <div style="text-align:center; padding:10px 0;">
            <img src="{logo_url}" width="80" style="margin-bottom:10px;">
            <h1 style="font-family:'Amiri', serif; color:#B8860B; font-size:2.5rem; margin:0;">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#64748b; font-size:1rem; font-weight:700; margin-top:-5px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div style="width:40px; height:2px; background:#B8860B; margin: 5px auto;"></div>
        </div>
    """, unsafe_allow_html=True)

    # التحقق من الدخول (استدعاء الموديول الأصلي لضمان الأمان)
    try:
        from modules.auth import login_required
        user = login_required()
    except:
        st.warning("يرجى التأكد من إعداد Secrets الدخول.")
        return

    if user:
        # التبويبات المطورة للهواتف
        tab1, tab2, tab3 = st.tabs(["📊 التحليل الاستراتيجي", "🌍 معاينة الساتلايت", "💼 إدارة الصفقات"])
        
        with tab1:
            st.markdown("<h4 style='color:#B8860B;'>مؤشرات السوق الحالية</h4>", unsafe_allow_html=True)
            # هنا يمكنك وضع محتوى لوحة التحكم
            c1, c2, c3 = st.columns(3)
            c1.metric("إجمالي الصفقات", "1,240", "+5%")
            c2.metric("متوسط الإيجار", "45,000 ر.س", "-2%")
            c3.metric("درجة الثقة", "92%", "ممتاز")
            
        with tab2:
            st.markdown("<h4 style='color:#B8860B;'>المعاينة الميدانية (الأقمار الصناعية)</h4>", unsafe_allow_html=True)
            render_professional_map()
            
        with tab3:
            st.markdown("<h4 style='color:#B8860B;'>بيانات الصفقات العقارية</h4>", unsafe_allow_html=True)
            # مثال لجدول نحيف وأنيق
            data = pd.DataFrame({
                "العقار": ["برج مكة", "مبنى استثماري", "فيلا سكنية"],
                "القيمة": ["5M", "2.1M", "1.8M"],
                "المنطقة": ["العزيزية", "الشوقية", "بطحاء قريش"]
            })
            st.table(data)

if __name__ == "__main__":
    main()
