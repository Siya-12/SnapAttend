import streamlit as st
def style_background_home():
    st.markdown("""
    <style>
      div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 1.5px solid #d7dcf5 !important;
            border-radius: 24px !important;
            padding: 1.5rem !important;
            background: white !important;
            box-shadow: 0 8px 24px rgba(14, 23, 92, 0.06);
        }

        div[data-testid="stVerticalBlockBorderWrapper"] h2 {
            text-align: center !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] .stImage {
            display: flex;
            justify-content: center;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] .stButton {
            display: flex;
            justify-content: center;
        }
    </style>
""",unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
    <style>
         .stApp
                {
                # background-color:beige !important;
                }
    </style>
""",unsafe_allow_html=True)
    


def base_layout():
    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Tomorrow:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
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
                font-family: 'Tomorrow',sans-serif  !important;
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

                # button[kind="Secondary"]
                # {
                #  background:blue !important;
                # border-radius:2px !important;
                # color:white !important;
                # border:none !important;
                # padding: 6px 16px !important;
                # display:inline; !important;
                # transition: transform 0.25s ease-in-out !important;
                # }
                button[kind="secondary"] {
    background: navy !important;
    border-radius: 6px !important;
    color: white !important;
    border: none !important;
    padding: 6px 16px !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    min-height: 36px !important;
    line-height: 1 !important;
    transition: transform 0.25s ease-in-out !important;
}

div.stButton {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-top: 8px;
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
