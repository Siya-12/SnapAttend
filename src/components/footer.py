# import streamlit as st

# def footer_home():
#     col1, col2 = st.columns([1, 5])
#     with col1:
#         st.markdown(
#             """
#             <h4 style="
#             margin-top:2rem;
#             display:flex;
#             gap:6px;
#             justify-center:center;
#             items-align:center;
#             font-family:Tomorrow;
#             ">
#             Created by Siya Agarwal</h4>
#             """,
#             unsafe_allow_html=True
#         )

# footer_home()
import streamlit as st

def footer_home():
    st.markdown(
        """
        <style>
        .custom-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            font-family: 'Arial', sans-serif;
            font-size: 14px;
            color: white;
            text-align: center;
            background-color: navy;
            padding: 12px 0;
            z-index: 9999;
        }
        </style>

        <div class="custom-footer">
            Created by Siya Agarwal
        </div>
        """,
        unsafe_allow_html=True
    )

footer_home()
