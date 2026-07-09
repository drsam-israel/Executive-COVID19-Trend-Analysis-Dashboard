import streamlit as st


def render_enterprise_sidebar():
    st.sidebar.markdown(
        '''
        <style>
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617 0%, #0F172A 55%, #111827 100%);
        }

        section[data-testid="stSidebar"] * {
            color: #E5E7EB;
        }

        section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
            padding-top: 10px;
        }

        section[data-testid="stSidebar"] [data-testid="stSidebarNav"] ul {
            padding-left: 0;
        }

        section[data-testid="stSidebar"] a {
            border-radius: 10px;
            padding: 8px 10px;
            font-weight: 700;
        }

        section[data-testid="stSidebar"] a:hover {
            background: rgba(37, 99, 235, 0.22);
        }

        .sidebar-title {
            font-size: 21px;
            font-weight: 900;
            color: #FFFFFF;
            line-height: 1.25;
            margin-bottom: 12px;
        }

        .sidebar-divider {
            border-top: 1px solid rgba(148, 163, 184, 0.35);
            margin: 18px 0;
        }

        .sidebar-text {
            font-size: 14px;
            color: #E5E7EB;
            line-height: 1.55;
            margin-bottom: 8px;
        }

        .sidebar-program {
            font-size: 13px;
            color: #93C5FD;
            font-weight: 800;
            line-height: 1.45;
            text-transform: uppercase;
        }

        .sidebar-footer {
            font-size: 12px;
            color: #CBD5E1;
            line-height: 1.6;
            margin-top: 16px;
        }
        </style>

        <div class="sidebar-title">
            Executive COVID-19<br>
            Trend Analysis &<br>
            Forecasting Dashboard
        </div>

        <div class="sidebar-divider"></div>

        <div class="sidebar-text">
            Indian Institute of Technology (IIT)<br>
            & Intellipaat
        </div>

        <div class="sidebar-program">
            Advanced Certification<br>
            in Data Science and AI
        </div>

        <div class="sidebar-divider"></div>
        ''',
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("### Navigation")

    st.sidebar.markdown(
        '''
        <div class="sidebar-divider"></div>

        <div class="sidebar-footer">
            Version 1.0<br>
            Samuel Israel<br>
            (c) 2026
        </div>
        ''',
        unsafe_allow_html=True,
    )
