import streamlit as st
import pandas as pd

# --- 1. إعدادات الهوية البصرية (تصميم م. داغستاني المطور) ---
st.set_page_config(
    page_title="M. DAGHISTANI | نظام التقدير العقاري",
    page_icon="🏢",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* الخلفية والتنسيق العام */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, #0a192f 100%);
        color: #e6f1ff;
    }
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        text-align: center;
    }

    /* الصناديق الزجاجية */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(194, 151, 77, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
    }

    /* الأزرار الذهبية */
    div.stButton > button {
        background: linear-gradient(45deg, #c2974d, #e0ac52) !important;
        color: #0a192f !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100%;
        padding: 15px !important;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(194, 151, 77, 0.4) !important;
    }

    /* حقول الإدخال */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: rgba(10, 25, 47, 0.8) !important;
        color: white !important;
        border: 1px solid rgba(194, 151, 77, 0.3) !important;
        border-radius: 10px !important;
    }

    /* بطاقة النتيجة النهائية */
    .result-box {
        text-align: center;
        background: rgba(194, 151, 77, 0.1);
        border: 2px solid #c2974d;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الهيدر (الشعار والترويسة) ---
st.markdown("""
    <div style="text-align: center; padding-bottom: 30px;">
        <h1 style="font-size: 3.8rem; margin: 0;">م. داغستاني</h1>
        <div style="color: #c2974d; font-size: 1.4rem; font-weight: 700; margin-top: -10px;">
            من مكة المكرمة.. نصلكم بالعالم
        </div>
        <hr style="border: 0.5px solid rgba(194, 151, 77, 0.2); width: 60%; margin: 20px auto;">
    </div>
    """, unsafe_allow_html=True)

# --- 3. نظام الحساب (إرجاع الكود المفقود) ---
# ملاحظة: هذا الهيكل مصمم لكي تضع فيه معادلاتك السابقة
def main():
    # التحقق من تسجيل الدخول (اختياري - حسب نظامك)
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🔐 تسجيل دخول النظام")
        user_pass = st.text_input("أدخل كلمة المرور", type="password")
        if st.button("دخول"):
            # التحقق من الـ Secrets (التي شرحناها سابقاً)
            if user_pass == st.secrets["passwords"]["admin"]:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("بيانات الدخول غير صحيحة")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # --- واجهة التطبيق الرئيسية بعد الدخول ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📋 مدخلات التقدير العقاري")
    
    col1, col2 = st.columns(2)
    with col1:
        building_name = st.text_input("اسم العقار")
        city = st.selectbox("المدينة", ["مكة المكرمة", "جدة", "الرياض"])
    with col2:
        area = st.number_input("المساحة الكلية (م²)", min_value=0.0)
        base_price = st.number_input("متوسط سعر المتر للمنطقة (ريال)", min_value=0.0)

    # زر الحساب الرئيسي
    if st.button("بدء عملية التقدير"):
        # هنا نضع المعادلة الحسابية (تأكد من مطابقتها لكودك القديم)
        total_value = area * base_price
        
        st.markdown(f"""
            <div class="result-box">
                <h3 style="margin:0; color:#e6f1ff;">إجمالي القيمة التقديرية</h3>
                <div style="font-size: 3rem; font-weight: 900; color: #c2974d;">
                    {total_value:,.2f} ريال
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # عرض البيانات في جدول منسق
        st.write("### تفاصيل الحساب المرجعية")
        results_df = pd.DataFrame({
            "المعلمة": ["اسم العقار", "المساحة", "سعر المتر", "النتيجة النهائية"],
            "القيمة": [building_name, f"{area} م²", f"{base_price} ريال", f"{total_value:,.2f} ريال"]
        })
        st.table(results_df)

    st.markdown('</div>', unsafe_allow_html=True)

    # زر تسجيل الخروج
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state["authenticated"] = False
        st.rerun()

if __name__ == "__main__":
    main()
