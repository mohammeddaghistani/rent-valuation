import streamlit as st

# استيراد الوظائف الأساسية
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("تنبيه: مجلد modules مفقود أو غير مكتمل")

# --- إعدادات الصفحة ---
st.set_page_config(page_title="M. DAGHISTANI", layout="wide")

# --- نظام الألوان الجديد (Modern Luxury) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* 1. الخلفية: تدرج احترافي مريح (Light-Dark Slate) */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        color: #f8fafc !important;
    }

    /* 2. النصوص: أبيض نقي للوضوح ورمادي فاتح للتفاصيل */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* 3. العناوين: ذهبي مشرق (Champagne Gold) */
    h1, h2, h3 {
        font-family: 'Amiri', serif !important;
        color: #f1c40f !important; /* لون ذهبي أكثر إشراقاً */
        text-shadow: 0px 2px 4px rgba(0,0,0,0.3);
    }

    /* 4. تنسيق الجداول: (الخلايا أصبحت واضحة جداً) */
    .stDataFrame, div[data-testid="stTable"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(241, 196, 15, 0.3) !important;
    }
    
    /* رأس الجدول: ذهبي مطفي */
    thead tr th {
        background-color: #d4af37 !important;
        color: #0f172a !important;
        font-weight: 900 !important;
    }
    
    /* خلايا الجدول: تبادل ألوان هادئ */
    tbody tr td {
        background-color: rgba(30, 41, 59, 0.7) !important;
        color: #ffffff !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* 5. الأزرار: تصميم عصري (Gradient Gold) */
    div.stButton > button {
        background: linear-gradient(90deg, #d4af37 0%, #f1c40f 100%) !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        border-radius: 50px !important; /* حواف دائرية عصرية */
        border: none !important;
        padding: 10px 30px !important;
        transition: 0.3s all ease;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(241, 196, 15, 0.4) !important;
    }

    /* 6. تنسيق المدخلات (Inputs) للآيفون والجوال */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: #f8fafc !important; /* خلفية فاتحة للمدخلات لسهولة القراءة */
        color: #0f172a !important;
        border: 2px solid #d4af37 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }

    /* 7. القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-left: 2px solid #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    init_db()
    ensure_settings()
    
    # الشعار العلوي بتصميم جديد
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h1 style="font-size: 3.5rem; margin: 0; color: #f1c40f;">م. داغستاني</h1>
            <p style="color: #d4af37; font-size: 1.2rem; font-weight: 700; letter-spacing: 2px; margin-top: -10px;">
                INVESTMENT REAL ESTATE VALUATION
            </p>
        </div>
    """, unsafe_allow_html=True)

    user = login_required()
    if user:
        render_dashboard(user)

if __name__ == "__main__":
    main()
