import streamlit as st


def open_section(title):
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def close_section():
    st.markdown('</div>', unsafe_allow_html=True)
