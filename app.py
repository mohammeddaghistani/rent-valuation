import streamlit as st
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("خطأ: يرجى التأكد من رفع جميع ملفات المجلد modules")

# --- الإعدادات المتقدمة للفخامة والتوافق ---
st.set_page_config(
    page_title="M. DAGHISTANI | نظام التقدير العقاري",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&family=Amiri:wght@700&display=swap');

    /* 1. التوافق مع الشاشات (Responsive) والخلفية السيادية */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 50% 50%, #112240 0%, #0a192f 100%) !important;
        color: #FFFFFF !important;
    }

    /* 2. توحيد الخطوط وتنسيق النصوص */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* 3. الهيدر الملكي (متوافق مع الجوال) */
    .main-header {
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid rgba(194, 151, 77, 0.3);
        margin-bottom: 40px;
    }
    .main-header h1 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        font-size: clamp(2rem, 8vw, 4rem) !important; /* حجم خط مرن للجوال */
        margin: 0;
    }

    /* 4. تنسيق الخلايا والجداول الفخم */
    .stDataFrame, div[data-testid="stTable"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(194, 151, 77, 0.2) !important;
        border-radius: 15px !important;
        overflow: hidden !important;
    }
    
    /* ألوان خلايا الجدول */
    th {
        background-color: #c2974d !important;
        color: #0a192f !important;
        font-weight: 900 !important;
        text-align: center !important;
    }
    td {
        background-color: rgba(10, 25, 47, 0.5) !important;
        color: #e6f1ff !important;
        border-bottom: 0.1px solid rgba(194, 151, 77, 0.1) !important;
    }

    /* 5. تصميم الحقول والمدخلات (Premium UI) */
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(194, 151, 77, 0.4) !important;
        border-radius: 12px !important;
        height: 50px !important;
        transition: 0.3s all ease;
    }
    .stTextInput input:focus {
        border-color: #c2974d !important;
        box-shadow: 0 0 15px rgba(194, 151, 77, 0.3) !important;
    }

    /* 6. الأزرار الذهبية (تأثير المرآة) */
    div.stButton > button {
        background: linear-gradient(145deg, #c2974d, #a67c37) !important;
        color: #0a192f !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(194, 151, 77, 0.5) !important;
    }

    /* 7. تحسين القائمة الجانبية للجوال */
    [data-testid="stSidebar"] {
        background-color: #0a192f !important;
        border-left: 1px solid rgba(194, 151, 77, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # استدعاء الوظائف الأصلية
    init_db()
    ensure_settings()
    
    # عرض الهيدر المطور
    st.markdown("""
        <div class="main-header">
            <h1>م. داغستاني</h1>
            <div style="color: #c2974d; font-weight: 700; font-size: 1.2rem;">
                نصلكم بالعالم.. من قلب مكة المكرمة
            </div>
        </div>
    """, unsafe_allow_html=True)

    # تشغيل نظام الدخول ولوحة التحكم
    user = login_required()
    if user:
        render_dashboard(user)

if __name__ == "__main__":
    main()
