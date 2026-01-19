import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="M. DAGHISTANI | نظام التقدير العقاري",
    page_icon="🏢",
    layout="wide"
)

# 2. حقن CSS المطور (الهوية البصرية + التحسينات الوظيفية)
st.markdown("""
    <style>
    /* استيراد الخطوط الفخمة */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* الخلفية العامة بتدرج ملكي */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, #0a192f 100%);
        color: #e6f1ff;
    }

    /* الشريط الجانبي */
    [data-testid="stSidebar"] {
        background-color: #0a192f !important;
        border-right: 1px solid rgba(194, 151, 77, 0.3);
    }

    /* الخطوط والتنظيم */
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* العناوين الملكية */
    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
    }

    /* الصناديق الزجاجية المطورة */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(194, 151, 77, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* تحسين حقول الإدخال مع تأثير التركيز (Focus) */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: rgba(10, 25, 47, 0.8) !important;
        color: #e6f1ff !important;
        border: 1px solid rgba(194, 151, 77, 0.3) !important;
        border-radius: 12px !important;
        padding: 12px !important;
        transition: 0.3s !important;
    }
    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: #c2974d !important;
        box-shadow: 0 0 15px rgba(194, 151, 77, 0.4) !important;
    }

    /* الأزرار الذهبية التفاعلية */
    div.stButton > button {
        background: linear-gradient(45deg, #c2974d, #e0ac52) !important;
        color: #0a192f !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px !important;
        width: 100%;
        font-size: 1.1rem !important;
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(194, 151, 77, 0.5) !important;
    }

    /* بطاقة عرض النتائج (Metric Box) */
    .metric-box {
        text-align: center;
        background: rgba(194, 151, 77, 0.1);
        border: 2px solid #c2974d;
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: inset 0 0 20px rgba(194, 151, 77, 0.1);
    }
    .metric-value {
        font-size: 3.2rem;
        font-weight: 900;
        color: #c2974d;
        margin-top: 10px;
        text-shadow: 0 0 10px rgba(194, 151, 77, 0.3);
    }

    /* تنسيق الجداول (Zebra Stripes) */
    .stDataFrame {
        border: 1px solid rgba(194, 151, 77, 0.2) !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ترويسة التطبيق (الهيدر)
st.markdown("""
    <div style="text-align: center; padding: 10px 0 40px 0;">
        <h1 style="font-size: 4rem; margin-bottom: 0;">م. داغستاني</h1>
        <div style="color: #c2974d; font-size: 1.6rem; font-weight: 700; margin-top: -10px; letter-spacing: 2px;">
            من مكة المكرمة.. نصلكم بالعالم
        </div>
        <p style="color: #8892b0; font-size: 1.1rem; margin-top: 15px;">نظام التقدير الإيجاري الذكي للعقارات الاستثمارية</p>
        <div style="width: 100px; height: 3px; background: #c2974d; margin: 20px auto; border-radius: 5px;"></div>
    </div>
    """, unsafe_allow_html=True)

# 4. منطق العمل الأساسي (الكود الوظيفي الخاص بك)
# -------------------------------------------------------------------
# ملاحظة: ضع هنا جميع الدوال الحسابية الخاصة بك (functions) 
# التي تقوم بحساب تقدير القيمة الإيجارية.

def main():
    # استخدام الصندوق الزجاجي لتنظيم المدخلات
    st.markdown('<div class="glass-card"><h3>بيانات العقار المراد تقديره</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        building_name = st.text_input("اسم المبنى / المشروع", placeholder="مثال: برج مكة الاستثماري")
        property_type = st.selectbox("نوع النشاط الاستثماري", ["تجاري", "سكني", "فندقي", "إداري"])
    
    with col2:
        location = st.text_input("الحي / المنطقة", placeholder="مثال: العزيزية")
        total_area = st.number_input("إجمالي المساحة القابلة للتأجير (م²)", min_value=1.0, step=1.0)
    
    # زر الحساب
    calculate = st.button("حساب القيمة التقديرية")
    st.markdown('</div>', unsafe_allow_html=True)

    if calculate:
        # هنا يتم وضع منطق الحساب البرمجي الخاص بك
        # سنضع مثالاً افتراضياً:
        estimated_value = total_area * 1250 # مثال افتراضي للسعر للمتر
        
        # 5. عرض النتائج بالهوية الجديدة
        st.markdown(f"""
            <div class="metric-box">
                <div style="color: #e6f1ff; font-size: 1.3rem; font-weight: 700;">إجمالي القيمة الإيجارية السنوية التقديرية</div>
                <div class="metric-value">{estimated_value:,.0f} ريال</div>
            </div>
            """, unsafe_allow_html=True)
        
        # عرض جدول البيانات المرجعية بتنسيق نظيف
        st.write("### تفاصيل التقدير المرجعية")
        data = {
            "المعيار": ["سعر المتر المرجعي", "معدل الإشغال المتوقع", "تكاليف الإدارة"],
            "القيمة": ["1,250 ريال", "95%", "5%"]
        }
        st.table(pd.DataFrame(data))

# تشغيل التطبيق
if __name__ == "__main__":
    main()

# 6. التذييل (فوتر)
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid rgba(194, 151, 77, 0.1);">
        <p style="color: #8892b0; font-size: 0.9rem;">© 2025 M. DAGHISTANI | جميع الحقوق محفوظة</p>
        <p style="color: #c2974d; font-size: 0.8rem;">نظام تقدير القيم الإيجارية - النسخة الاحترافية 1.0</p>
    </div>
    """, unsafe_allow_html=True)
