import streamlit as st


def render_insight(text):
    st.markdown(
        f'''
        <div class="insight-box">
            {text}
        </div>
        ''',
        unsafe_allow_html=True,
    )
