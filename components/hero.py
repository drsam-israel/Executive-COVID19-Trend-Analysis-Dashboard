import streamlit as st
from config.settings import APP_TITLE, APP_SUBTITLE, APP_INSTITUTION, APP_DESCRIPTION


def render_hero():
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #0B1F4D 0%, #1E3A8A 55%, #2563EB 100%);
            padding: 34px 38px;
            border-radius: 18px;
            color: white;
            margin-bottom: 28px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.18);
        ">
            <h1 style="margin-bottom: 8px; font-size: 34px;">
                {APP_TITLE}
            </h1>
            <h3 style="margin-top: 0; font-weight: 500;">
                {APP_SUBTITLE}
            </h3>
            <p style="font-size: 18px; margin-bottom: 6px;">
                {APP_INSTITUTION}
            </p>
            <p style="font-size: 16px; max-width: 950px; line-height: 1.55;">
                {APP_DESCRIPTION}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )