import hashlib
import streamlit as st
from sqlalchemy.orm import Session
from modules.db import init_db, SessionLocal, User, ensure_settings
from modules.style import apply_branding, render_footer

def _hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def ensure_admin():
    init_db()
    ensure_settings()
    # جلب البيانات من السيكرتس أو استخدام افتراضي
    admin_user = st.secrets.get("ADMIN_USERNAME", "admin")
    admin_pass = st.secrets.get("ADMIN_PASSWORD", "admin")
    db: Session = SessionLocal()
    try:
        u = db.query(User).filter(User.username == admin_user).first()
        if not u:
            db.add(User(username=admin_user, password_hash=_hash_password(admin_pass), role="admin", is_active=True))
            db.commit()
    finally:
        db.close()

def login_required():
    ensure_admin()
    if "user" in st.session_state and st.session_state.user.get("username"):
        return st.session_state.user

    # --- التعديل الجمالي (هوية م. داغستاني) ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@700&display=swap');
        
        /* تحسين مظهر صفحة الدخول */
        .stForm {
            background: rgba(255, 255, 255, 0.03) !important;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(194, 151, 77, 0.3) !important;
            border-radius: 20px !important;
            padding: 40px !important;
        }
        
        label { color: #c2974d !important; font-weight: bold !important; font-family: 'Cairo' !important; }
        input { background-color: #0a192f !important; color: white !important; border: 1px solid #c2974d !important; }
        
        .login-title {
            font-family: 'Amiri', serif;
            font-size: 3rem;
            color: #c2974d;
            text-align: center;
            margin-bottom: 0;
        }
        </style>
        
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 class="login-title">م. داغستاني</h1>
            <p style="color: #c2974d; font-weight: bold; font-size: 1.2rem;">نظام تقدير القيمة الإيجارية - دخول الموظفين</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("اسم المستخدم", key="login_username")
        password = st.text_input("كلمة المرور", type="password", key="login_password")
        submit = st.form_submit_button("تسجيل الدخول للنظام")

    if submit:
        db: Session = SessionLocal()
        try:
            u = db.query(User).filter(User.username == username, User.is_active == True).first()
            if not u or u.password_hash != _hash_password(password):
                st.error("⚠️ بيانات الدخول غير صحيحة. تأكد من الإعدادات في Secrets.")
            else:
                st.session_state.user = {"username": u.username, "role": u.role}
                st.success("✅ مرحباً بك.. جاري تحميل لوحة التحكم")
                st.rerun()
        finally:
            db.close()

    render_footer()
    st.stop()

def require_role(allowed_roles):
    user = st.session_state.get("user", {})
    if user.get("role") not in allowed_roles:
        st.error("ليس لديك صلاحية للوصول إلى هذه الصفحة")
        st.stop()
