import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import math

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="محمد داغستاني للتقييم العقاري", page_icon="⚜️", layout="wide")

# --- 2. محرك التنسيق (Strict RTL & Slim UI) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Amiri:wght@700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        direction: rtl !important; text-align: right !important; font-family: 'Cairo', sans-serif !important;
    }
    /* تصغير الخانات وضبط اتجاه الكتابة بداخلها */
    input, select, textarea {
        direction: rtl !important; text-align: right !important;
        height: 32px !important; font-size: 0.85rem !important; border-radius: 4px !important;
    }
    .stTabs [data-baseweb="tab-list"] { flex-direction: row-reverse !important; justify-content: flex-end !important; }
    label { font-size: 0.8rem !important; color: #B8860B !important; text-align: right !important; display: block !important; }
    div.stButton > button { height: 35px !important; background: #1a1a1a !important; color: #B8860B !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. المعادلات والعمليات (المنطق البرمجي) ---
def calculate_valuation(area, unit_price, floor_factor, location_score):
    """معادلة التقدير الإيجاري الاستثماري"""
    base_value = area * unit_price
    adjusted_value = base_value * (floor_factor) * (1 + (location_score / 100))
    return adjusted_value

def calculate_confidence_score(num_deals, proximity_km):
    """معادلة درجة الثقة في التقييم"""
    # كلما زادت الصفقات وقربت المسافة زادت الثقة
    score = (num_deals * 10) + (100 / (proximity_km + 1))
    return min(99, round(score, 1))

# --- 4. واجهة العمليات (التطبيق الفعلي) ---
def main():
    st.markdown("<h1 style='text-align:center; color:#B8860B; font-family:Amiri;'>محمد داغستاني للتقييم العقاري</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📝 عملية تقييم جديدة", "🌍 خريطة الساتلايت", "📊 سجل الصفقات"])

    with tab1:
        st.markdown("<p style='text-align:right; font-weight:bold;'>إدخال بيانات التقدير الإيجاري</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            name = st.text_input("اسم العقار/العميل")
            area = st.number_input("المساحة (م2)", min_value=1.0, value=100.0)
        with col2:
            base_price = st.number_input("سعر المتر التقديري", value=500.0)
            floor = st.selectbox("الدور", options=[1.0, 1.2, 0.9], format_func=lambda x: "أرضي" if x==1.2 else "متكرر")
        with col3:
            loc_score = st.slider("درجة الموقع (0-20)", 0, 20, 10)

        if st.button("تشغيل معادلة التقييم"):
            res = calculate_valuation(area, base_price, floor, loc_score)
            conf = calculate_confidence_score(5, 0.5) # قيم افتراضية كمثال
            
            st.success(f"التقدير الإيجاري السنوي: {res:,.2f} ريال سعودي")
            st.info(f"درجة الثقة في التقييم: {conf}%")

    with tab2:
        st.markdown("<p style='text-align:right;'>المعاينة الجيومكانية (Satellite)</p>", unsafe_allow_html=True)
        m = folium.Map(location=[21.4225, 39.8262], zoom_start=15)
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri Satellite', name='Satellite'
        ).add_to(m)
        st_folium(m, width="100%", height=400)

    with tab3:
        # هنا تظهر الصفقات التي كانت في ملف db
        st.write("سجل الصفقات المرجعية (Database)")
        df_sample = pd.DataFrame({
            "التاريخ": ["2024-01-01", "2024-01-10"],
            "العقار": ["مبنى أ", "محل ب"],
            "القيمة الإيجارية": [50000, 120000]
        })
        st.table(df_sample)

if __name__ == "__main__":
    main()
