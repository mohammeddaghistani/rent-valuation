import streamlit as st

# استيراد الوظائف الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("تنبيه: مجلد modules مفقود أو غير مكتمل في GitHub")

# --- إعدادات الفخامة القصوى وتوافق الأجهزة ---
st.set_page_config(
    page_title="M. DAGHISTANI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- محرك التنسيق الاحترافي (Professional UI Engine) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* 1. الخلفية السيادية (Deep Midnight) */
    [data-testid="stAppViewContainer"] {
        background-color: #050a14 !important;
        background-image: radial-gradient(circle at 50% 50%, #0a192f 0%, #050a14 100%) !important;
    }

    /* 2. وضوح النصوص (Pure White & Gold) */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
        color: #FFFFFF !important; /* أبيض ناصع لأقصى وضوح */
    }

    /* 3. العناوين (Royal Gold) */
    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        text-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }

    /* 4. تنسيق الجداول والخلايا (Elite Tables) */
    /* جعل الجدول يبدو كقطعة واحدة فخمة */
    .stDataFrame, div[data-testid="stTable"] {
        border: 1px solid rgba(194, 151, 77, 0.3) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        background: rgba(255, 255, 255, 0.02) !important;
    }
    
    th {
        background-color: #c2974d !important;
        color: #050a14 !important;
        font-weight: 900 !important;
        padding: 15px !important;
    }
    
    td {
        background-color: rgba(10, 25, 47, 0.4) !important;
        border-bottom: 1px solid rgba(194, 151, 77, 0.1) !important;
        color: #ffffff !important;
        padding: 12px !important;
    }

    /* 5. الأزرار (Gold Leaf Effect) */
    div.stButton > button {
        background: linear-gradient(135deg, #c2974d 0%, #a67c37 100%) !important;
        color: #050a14 !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-size: 1.1rem !important;
        transition: 0.3s all ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(194, 151, 77, 0.6) !important;
    }

    /* 6. توافق الجوال (Mobile Optimization) */
    @media (max-width: 768px) {
        .stMain { padding: 10px !important; }
        h1 { font-size: 2.2rem !important; }
    }

    /* 7. تنسيق المدخلات (Modern Inputs) */
    input, select, textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(194, 151, 77, 0.4) !important;
        color: white !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # الوظائف الأساسية
    init_db()
    ensure_settings()
    
    # شعار م. داغستاني الفخم
    st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="margin: 0;">م. داغستاني</h1>
            <div style="color: #c2974d; font-size: 1.4rem; font-weight: 700; letter-spacing: 1px;">
                من مكة المكرمة.. نصلكم بالعالم
            </div>
            <div style="width: 60px; height: 3px; background: #c2974d; margin: 15px auto; border-radius: 10px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # تشغيل النظام
    user = login_required()
    if user:
        render_dashboard(user)

if __name__ == "__main__":
    main()
