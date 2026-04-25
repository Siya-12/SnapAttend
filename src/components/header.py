import streamlit as st

def header_home():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("src/assets/image/logo.png", width=150)
    st.markdown("""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;">
              <h1 style='text-alignment:center; color:navy;'>SNAP <br/> ATTEND</h1>
            </div>
                """,unsafe_allow_html=True)
header_home()
