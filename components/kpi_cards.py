import streamlit as st


def render_kpi_card(title, value, subtitle, icon):
    st.markdown(
        f"""
        <div style="
            background: white;
            padding: 22px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
            min-height: 145px;
        ">
            <div style="font-size: 28px;">{icon}</div>
            <p style="color: #64748B; margin-bottom: 6px; font-weight: 600;">
                {title}
            </p>
            <h2 style="color: #0F172A; margin: 0;">
                {value}
            </h2>
            <p style="color: #64748B; margin-top: 8px;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )