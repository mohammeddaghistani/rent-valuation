import streamlit as st
# استيراد الوظائف الأصلية لبرنامجك
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except ImportError:
    st.error("تنبيه: تأكد من رفع مجلد modules كاملاً إلى GitHub")

# --- تنسيق الهوية البصرية وتحسين وضوح الخط ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');

    /* تحسين وضوح النصوص بشكل جذري */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
        color: #FFFFFF !important; /* لون أبيض ناصع للخط */
    }

    /* خلفية داكنة ملكية */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #1a2a44 0%, #0a192f 100%) !important;
    }

    /* العناوين باللون الذهبي الواضح */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Amiri', serif !important;
        color: #c2974d !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }

    /* تحسين وضوح حقول الإدخال */
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        color: #FFFFFF !important;
        background-color: rgba(255,255,255,0.1) !important;
        border: 1px solid #c2974d !important;
        font-weight: bold !important;
    }

    /* جعل الليبل (أسماء الحقول) ذهبية وواضحة */
    label {
        color: #c2974d !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # 1. تشغيل قاعدة البيانات (كودك الأصلي)
    try:
        init_db()
        ensure_settings()
    except:
        pass
    
    # 2. الهيدر الفخم
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="font-size: 3.5rem; margin-bottom: 0;">م. داغستاني</h1>
            <p style="color: #c2974d; font-size: 1.5rem; font-weight: bold;">من مكة المكرمة.. نصلكم بالعالم</p>
            <hr style="border: 0.5px solid rgba(194, 151, 77, 0.3);">
        </div>
        """, unsafe_allow_html=True)

    # 3. تشغيل نظام الدخول ولوحة التحكم (كودك الأصلي)
    try:
        user = login_required()
        if user:
            render_dashboard(user)
    except NameError:
        st.warning("جاري تحميل النظام... تأكد من اكتمال رفع الملفات.")

if __name__ == "__main__":
    main()
