import streamlit as st
from config.settings import APP_TITLE, APP_SUBTITLE, APP_INSTITUTION, AUTHOR


def render_footer():
    st.markdown("---")
    st.markdown(
        f"""
        <div style="text-align:center; color:#64748B; padding: 15px;">
            <strong>{APP_TITLE}</strong><br>
            {APP_SUBTITLE} | {APP_INSTITUTION}<br>
            Developed by {AUTHOR}
        </div>
        """,
        unsafe_allow_html=True,
    )