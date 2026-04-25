import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import base_layout, style_background_home
def home_screen():
    header_home()
    style_background_home()
    base_layout()
    col1,col2=st.columns(2,gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.header("I'm Student")
        st.image("src/assets/image/3.png", width=150)
        if st.button('Student Portal', key='btn1',type="primary",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.header("I'm Teacher")
        st.image("src/assets/image/2.png", width=150)
        if st.button('Teacher Portal', key='btn2',type="primary",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
 
home_screen()