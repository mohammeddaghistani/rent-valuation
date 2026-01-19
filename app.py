import streamlit as st
import os

# 1. استيراد الموديولات الأصلية (لضمان عدم فقدان أي وظيفة)
try:
    from modules.db import init_db, ensure_settings
    from modules.auth import login_required
    from modules.dashboard import render_dashboard
except Exception as e:
    st.error(f"حدث خطأ في تحميل ملفات النظام الأساسية: {e}")
    st.stop()

# 2. إعدادات الهوية (أيقونة التبويب بناءً على شعارك)
LOGO_URL = "https://mdaghistani.com/wp-content/uploads/2023/05/logo-gold.png"
st.set_page_config(
    page_title="محمد داغستاني للتقييم العقاري",
    page_icon=LOGO_URL,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. محرك التنسيق "الهيبة والرشاقة" (Elite Slim RTL)
# هذا الجزء يعالج الألوان، الخطوط، واتجاه اليمين لليسار
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Amiri:wght@700&display=swap');

    /* فرض الاتجاه العربي بالكامل */
    html, body, .stApp {{
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        background-color: #ffffff !important;
    }}

    /* نحافة الخانات (Slim UI) لتعطي هيبة البرمجيات الاحترافية */
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="button"], .stTextArea textarea {{
        height: 32px !important;
        padding: 0px 10px !important;
        font-size: 0.9rem !important;
        border-radius: 4px !important;
        border: 1px solid #e2e8f0 !important;
        direction: rtl !important;
    }}

    /* تصغير العناوين الفرعية (Labels) */
    label {{
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        color: #b45309 !important; /* لون ذهبي الشعار */
        margin-bottom: 2px !important;
        text-align: right !important;
        display: block !important;
    }}

    /* تطوير التبويبات (Tabs) لتكون من اليمين لليسار */
    .stTabs [data-baseweb="tab-list"] {{
        direction: rtl !important;
        display: flex !important;
        flex-direction: row-reverse !important;
        justify-content: flex-end !important;
        gap: 15px !important;
        border-bottom: 2px solid #f1f5f9 !important;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        font-weight: 700 !important;
        color: #64748b !important;
        background-color: transparent !important;
    }}

    .stTabs [aria-selected="true"] {{
        color: #065f46 !important; /* أخضر الشعار */
        border-bottom: 3px solid #b45309 !important;
    }}

    /* الأزرار الملكية النحيفة */
    div.stButton > button {{
        height: 36px !important;
        background: #1a1a1a !important; /* أسود ملكي */
        color: #b45309 !important; /* ذهبي */
        border: 1px solid #b45309 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        width: 100% !important;
    }}

    /* إخفاء زوائد ستريمليت */
    #MainMenu, footer, header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

def main():
    # استدعاء الوظائف البرمجية الأصلية التي طلبتها
    init_db()
    ensure_settings()
    
    # شعار "محمد داغستاني للتقييم العقاري" الرسمي
    st.markdown(f"""
        <div style="text-align:center; padding:15px 0;">
            <img src="{LOGO_URL}" width="70" style="margin-bottom:10px;">
            <h1 style="font-family:'Amiri', serif; color:#b45309; font-size:2.6rem; margin:0;">محمد داغستاني للتقييم العقاري</h1>
            <p style="color:#065f46; font-size:1rem; font-weight:700; margin-top:-5px;">نظام إدارة العلاقات والتقدير الإيجاري الاستثماري</p>
            <div style="width:60px; height:2px; background:linear-gradient(to left, #b45309, #065f46); margin:10px auto;"></div>
        </div>
    """, unsafe_allow_html=True)

    # تشغيل نظام الدخول ولوحة التحكم الأصلية
    user = login_required()
    if user:
        # هنا يتم استدعاء موديول الساتلايت والمعادلات تلقائياً من داخل dashboard
        render_dashboard(user)

if __name__ == "__main__":
    main()
