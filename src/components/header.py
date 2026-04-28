import streamlit as st

def header_home():
    col1, col2 = st.columns([1, 6], vertical_alignment="center")

    with col1:
        st.image("src/assets/image/logo.png", width=100)

    with col2:
        st.markdown(
            """
            <h1 style="
                margin: 0;
                color: navy;
                font-size: 64px;
                font-weight: 800;
                white-space: nowrap;
                line-height: 1;
            ">
                SNAP ATTEND
            </h1>
            """,
            unsafe_allow_html=True
        )


def header_dashboard():
    col1, col2 = st.columns([1, 6], vertical_alignment="center")

    with col1:
        st.image("src/assets/image/logo.png", width=250)

    with col2:
        st.markdown(
            """
            <h1 style="
                margin: 0;
                color: navy;
                font-size: 64px;
                font-weight: 800;
                white-space: nowrap;
                line-height: 1;
                text-alignment:left;
            ">
                SNAP ATTEND
            </h1>
            """,
            unsafe_allow_html=True
        )

