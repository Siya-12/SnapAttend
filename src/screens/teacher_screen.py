import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.ui.base_layout import base_layout, style_background_dashboard
def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to Home",type="secondary",key='loginbackBtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()
    
    st.header("Login using Password",text_alignment="center")
    st.space()
    st.space()
    teacher_username=st.text_input("Enter Username", placeholder="siya_agarwal", key="teacher_username_login")
    
    teacher_pass=st.text_input("Enter password", type="password",placeholder="Enter your password", key="teacher_password_login")
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
        st.button("Login Now",icon=':material/passkey:', shortcut='control+enter',width='stretch')
    with btnc2:
        if st.button("Register Instead",icon=':material/passkey:',width='stretch'):
            st.session_state.teacher_login_type='register'
   
    footer_home()

def teacher_screen_register():
    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to Home",type="secondary",key='registerBackBtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()
    
    st.header("Register new user",text_alignment="center")
    st.space()
    st.space()
    teacher_username=st.text_input("Enter Username", placeholder="siya_agarwal", key="teacher_username")
    
    teacher_name=st.text_input("Enter Name", placeholder="Siya",  key="teacher_name")
    
    teacher_pass=st.text_input("Enter password", type="password",placeholder="Enter your password",  key="teacher_password")
    
    teacher_pass_confirm=st.text_input("Confirm your password", type="password",placeholder="Confirm your password",  key="teacher_conf_pass")
   
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
        st.button("Register Now",icon=':material/passkey:', shortcut='control+enter',width='stretch')
    with btnc2:
        if st.button("Login Instead",icon=':material/passkey:',width='stretch'):
            st.session_state.teacher_login_type="login"
           
    footer_home()
def teacher_screen():
    style_background_dashboard()
    base_layout()
    if 'teacher_login_type' not in st.session_state:
        st.session_state.teacher_login_type = 'login'

    if st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()



