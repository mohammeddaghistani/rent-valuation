import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="M. DAGHISTANI | نظام التقدير العقاري",
    page_icon="🏢",
    layout="wide"
)

# 2. حقن CSS مخصص لتطبيق الهوية البصرية (Deep Marine & Gold)
st.markdown("""
    <style>
    /* استيراد الخطوط */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* الخلفية العامة */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle, #1a2a44 0%, #0a192f 100%);
        color: #e6f1ff;
    }

    /* الخطوط العربية */
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
    }

    /* الصناديق الزجاجية (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(194, 151, 77, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* الأزرار الذهبية */
    div.stButton > button {
        background: linear-gradient(45deg, #c2974d, #e0ac52) !important;
        color: #0a192f !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 25px !important;
        width: 100%;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 20px rgba(194, 151, 77, 0.4) !important;
    }

    /* تحسين شكل الحقول الإدخال */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: rgba(10, 25, 47, 0.7) !important;
        color: #e6f1ff !important;
        border: 1px solid rgba(194, 151, 77, 0.3) !important;
        border-radius: 10px !important;
    }

    /* بطاقة النتائج الكبرى (Metric Card) */
    .metric-box {
        text-align: center;
        background: rgba(194, 151, 77, 0.1);
        border: 2px solid #c2974d;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 900;
        color: #c2974d;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (الشعار والترويسة)
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="font-size: 3.5rem; margin-bottom: 0;">م. داغستاني</h1>
        <div style="color: #c2974d; font-size: 1.5rem; font-weight: 700; margin-top: -10px;">
            من مكة المكرمة.. نصلكم بالعالم
        </div>
        <p style="color: #8892b0; max-width: 600px; margin: 15px auto;">
            النظام الذكي لتقدير القيم الإيجارية للعقارات الاستثمارية
        </p>
        <hr style="border-color: rgba(194, 151, 77, 0.2); width: 50%; margin: 20px auto;">
    </div>
    """, unsafe_allow_html=True)

# 4. مثال لاستخدام البطاقة الزجاجية في المدخلات
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("اسم العقار / المشروع")
    with col2:
        st.selectbox("نوع العقار", ["سكني", "تجاري", "صناعي", "إداري"])
    st.markdown('</div>', unsafe_allow_html=True)

# 5. مثال لعرض النتائج بالبطاقة الذهبية المقترحة
st.markdown("""
    <div class="metric-box">
        <div style="color: #e6f1ff; font-size: 1.2rem;">إجمالي القيمة الإيجارية السنوية التقديرية</div>
        <div class="metric-value">550,000 ريال</div>
    </div>
    """, unsafe_allow_html=True)
