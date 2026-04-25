import streamlit as st
def style_background_home():
    st.markdown("""
    <style>
      .card
                {
                background-color:yellow !important;
                padding:3 rem !important;
                border-radius:2rem !important;
                }
    </style>
""",unsafe_allow_html=True)
    

def base_layout():
    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
                
                /* to remove top bar of streamlit */
                #MainMenu, footer, header
                {
                visibility:hidden;
                }

                .block-container
                {
                 padding-top:1.5rem !important;
                }

                h1,h2
                {
                font-family: 'Climate Crisis',sans-serif  !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0 rem !important;
                }

                # h3,h4,p
                # {
                #   font-family:'Outfit',sans-serif !important
                # }

                 button
                {
                 background:navy !important;
                border-radius:1.5 rem !important;
                color:white !important;
                border:none !important;
                padding: 10px 20px !important;
                transition: transform 0.25s ease-in-out !important;
                }

                button[kind="Secondary"]
                {
                 background:blue !important;
                border-radius:1.5 rem !important;
                color:white !important;
                border:none !important;
                padding: 10px 20px !important;
                transition: transform 0.25s ease-in-out !important;
                }

                 button[kind="tertiary"]
                {
                 background:green !important;
                border-radius:1.5 rem !important;
                color:white !important;
                border:none !important;
                padding: 10px 20px !important;
                transition: transform 0.25s ease-in-out !important;
                }

                button:hover
                {
                 transform: scale(1.05)
                }
        </style>
    """,unsafe_allow_html=True)

base_layout()