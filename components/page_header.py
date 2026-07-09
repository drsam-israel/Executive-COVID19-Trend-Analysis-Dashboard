import streamlit as st


def render_page_header(title, subtitle):
    st.markdown(
        f'''
        <div class="main-title">{title}</div>
        <div class="subtitle">{subtitle}</div>
        ''',
        unsafe_allow_html=True,
    )
