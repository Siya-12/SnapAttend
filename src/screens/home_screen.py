import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import base_layout, style_background_home
def home_screen():
    base_layout()
    style_background_home()
    header_home()
    
    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)
    col1,col2=st.columns(2,gap="large")

    with col1:
        with st.container(border=True):
            st.header("I'm Student")
            st.image("src/assets/image/3.png", width=150)
            if st.button('Student Portal', key='btn1',type="primary",icon=':material/arrow_outward:',icon_position='right',use_container_width=True,):
                st.session_state['login_type']='student'
                st.rerun()
           
    with col2:
         with st.container(border=True):
            st.header("I'm Teacher")
            st.image("src/assets/image/2.png", width=150)
            if st.button('Teacher Portal', key='btn2',type="primary",icon=':material/arrow_outward:',icon_position='right',use_container_width=True):
                st.session_state['login_type']='teacher'
                st.rerun()
    footer_home()

