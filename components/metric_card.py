import streamlit as st


def render_metric_card(label, value, subtitle, color="blue"):
    st.markdown(
        f'''
        <div class="metric-card {color}">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-sub">{subtitle}</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
