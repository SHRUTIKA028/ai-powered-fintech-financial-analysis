import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import base64
from pathlib import Path

from sklearn.linear_model import LinearRegression
from io import BytesIO
# from database import (
#     add_income,get_income,add_expense,
#     delete_expense,get_expense,total_income,total_expense,expense_by_category,monthly_expenses,register_user,
#     login_user,
#     monthly_expense_summary,delete_user_financial_data,change_password,add_bank_import,
#     get_bank_imports
# ) 
from database import (

    add_income,
    get_income,
    delete_income,
    add_expense,
    get_expense,
    delete_expense,
    total_income,
    total_expense,
    expense_by_category,
    monthly_expenses,
    register_user,
    login_user,
    monthly_expense_summary,
    delete_user_financial_data,
    change_password,
    add_bank_import,
    get_bank_imports

)
from modules.home import show_home
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# # =====================================================
# # APP UI STYLING
# # =====================================================

st.markdown(
    """
    <style>

    /* Main application */

    .main {
        padding-top: 2rem;
    }

    /* Main title */

    h1 {
        font-weight: 700;
    }

    /* Section headings */

    h2 {
        font-weight: 600;
    }

    h3 {
        font-weight: 600;
    }

    /* Buttons */

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
    }

    /* Metric cards */

    [data-testid="stMetric"] {
        border-radius: 12px;
        padding: 15px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* Dataframes */

    [data-testid="stDataFrame"] {
        border-radius: 10px;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {
        padding-top: 1rem;
    }

    /* Divider */

    hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)
# =====================================================
# APP UI STYLING
# =====================================================
# # =====================================================
# # APP UI STYLING
# # =====================================================

# if "appearance" not in st.session_state:
#     st.session_state.appearance = "🌙 Dark Mode"

# is_light = st.session_state.appearance == "☀️ Light Mode"

# bg_color = "#8295d3" if is_light else "#0e1117"
# text_color = "#3C66AA" if is_light else "#ffffff"
# card_color = "#989eac" if is_light else "#161b22"
# border_color = "rgba(79,70,229,0.15)" if is_light else "rgba(255,255,255,0.12)"

# st.markdown(
#     f"""
#     <style>

#     /* Main application */

#     .stApp {{
#         background-color: {bg_color} !important;
#         color: {text_color} !important;
#     }}

#     .main {{
#         padding-top: 2rem;
#     }}

#     /* Text */

#     h1, h2, h3, p, label {{
#         color: {text_color} !important;
#     }}

#     /* Metric cards */

#     [data-testid="stMetric"] {{
#         border-radius: 12px;
#         padding: 15px;
#         border: 1px solid {border_color};
#         background-color: {card_color} !important;
#     }}

#     [data-testid="stMetric"] label {{
#         color: {text_color} !important;
#     }}

#     [data-testid="stMetricValue"] {{
#         color: {text_color} !important;
#     }}

#     /* Buttons */

#     .stButton > button {{
#         border-radius: 8px;
#         font-weight: 600;
#         padding: 0.5rem 1rem;
#     }}

#     /* Inputs */

#     input, textarea {{
#         color: {text_color} !important;
#         background-color: {card_color} !important;
#     }}

#     /* Select boxes */

#     div[data-baseweb="select"] > div {{
#         background-color: {card_color} !important;
#         color: {text_color} !important;
#     }}

#     /* Dataframes */

#     [data-testid="stDataFrame"] {{
#         border-radius: 10px;
#     }}

#     /* Sidebar */

#     section[data-testid="stSidebar"] {{
#         padding-top: 1rem;
#     }}

#     /* Divider */

#     hr {{
#         margin-top: 1rem;
#         margin-bottom: 1rem;
#     }}

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Finance Analytics",
    page_icon="💰",
    layout="wide"
)
def create_financial_report(username, income, expense, balance):
    file_path = "financial_report.pdf"
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4
    )
    styles = getSampleStyleSheet()
    story = []
    title = Paragraph(
        "AI-Powered Personal Finance & Financial Analytics",
        styles["Title"]
    )
    story.append(title)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"User: {username}",
            styles["Normal"]
        )
    )
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Financial Summary",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 10))
    data = [
        ["Financial Metric", "Amount"],
        ["Total Income", f"₹ {income:.2f}"],
        ["Total Expense", f"₹ {expense:.2f}"],
        ["Balance", f"₹ {balance:.2f}"]
    ]

    table = Table(data)
    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("PADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(table)
    story.append(Spacer(1, 20))

    if income > 0:
        saving_percentage = (
            balance / income
        ) * 100
        if saving_percentage >= 50:
            suggestion = (
                "Excellent! You are saving more than "
                "50% of your income."
            )
        elif saving_percentage >= 30:
            suggestion = (
                "Good! Your savings are healthy."
            )
        elif saving_percentage >= 10:
            suggestion = (
                "Try to reduce unnecessary expenses."
            )
        else:
            suggestion = (
                "Your expenses are high. "
                "Consider creating a monthly budget."
            )
    else:
        suggestion = (
            "Add income information to receive "
            "financial suggestions."
        )
    story.append(
        Paragraph(
            "Financial Suggestion",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            suggestion,
            styles["Normal"]
        )
    )
    doc.build(story)
    return file_path
# =========================================================
# BUDGET SESSION
# =========================================================
if "monthly_budget" not in st.session_state:
    st.session_state.monthly_budget = 0.0

# =========================================================
# GLOBAL CURRENCY SETTINGS
# =========================================================

# if "currency_setting" not in st.session_state:
#     st.session_state.currency_setting = "₹ INR"

# currency_rates = {
#     "₹ INR": 1.0,
#     "$ USD": 0.0117,
#     "€ EUR": 0.0100,
#     "£ GBP": 0.0087
# }

# currency_symbols = {
#     "₹ INR": "₹",
#     "$ USD": "$",
#     "€ EUR": "€",
#     "£ GBP": "£"
# }


# def convert_currency(amount):
#     """
#     Convert stored INR amount into the selected currency.
#     """
#     selected_currency = st.session_state.currency_setting
#     rate = currency_rates[selected_currency]

#     return amount * rate


# def currency_symbol():
#     """
#     Return the symbol of the selected currency.
#     """
#     return currency_symbols[
#         st.session_state.currency_setting
#     ]
# =========================================================
# LOGIN SESSION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""
# =========================================================
# LOGIN / REGISTRATION
# =========================================================
# if not st.session_state.logged_in:
#     st.title("💰 Finance Analytics")
#     st.subheader("Login to your account")
if not st.session_state.logged_in: 

    st.markdown(
        '<h1 class="login-title">💰 Finance Analytics</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h3 class="login-subtitle">Login to your account</h3>',
        unsafe_allow_html=True
    )

   # =========================================================
    # LOGIN / REGISTRATION
    # =========================================================


if not st.session_state.logged_in:
    st.markdown(
        """
        <style>

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 15%,
                    rgba(100, 40, 220, 0.30),
                    transparent 32%
                ),
                radial-gradient(
                    circle at 90% 85%,
                    rgba(0, 140, 220, 0.25),
                    transparent 32%
                ),
                #080b14;
        }

        # /* ================================
        # LOGIN CARD
        # ================================= */
    
        [data-testid="stVerticalBlockBorderWrapper"] {
           background: rgba(25, 29, 43, 0.92);
           border: 1px solid rgba(255, 255, 255, 0.12);
           border-radius: 18px;
           box-shadow: 0px 20px 60px rgba(0, 0, 0, 0.45);

           animation: loginCardIn 0.8s ease-out;
           loginGlow 3s ease-in-out infinite alternate;
         }
        # /* ================================
        # LOGIN CARD ANIMATION
        # ================================= */

        @keyframes loginCardIn {

          from {
            opacity: 0;
            transform: translateY(25px) scale(0.97);
    }

          to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }

    }
    
        # /* ================================
        # LOGIN TITLE ANIMATION
        # ================================ */

        .login-title {
           animation: titleAppear 0.9s ease-out;
        }

        .login-subtitle {
           animation: subtitleAppear 1s ease-out;
           animation-delay: 0.25s;
           animation-fill-mode: both;
        }


        # /* TITLE */

        @keyframes titleAppear {

           from {
            opacity: 0;
            transform: translateY(-20px);
    }

            to {
            opacity: 1;
            transform: translateY(0);
    }

}


        /* SUBTITLE */

        @keyframes subtitleAppear {

        from {
           opacity: 0;
           transform: translateY(-10px);
    }

        to {
           opacity: 1;
           transform: translateY(0);
        }

    }
        # /* ================================
        # LOGIN CARD GLOW
        # ================================ */

        [data-testid="stVerticalBlockBorderWrapper"] {
            animation:
               loginCardIn 0.8s ease-out,
               loginGlow 3s ease-in-out infinite alternate;
        }

        @keyframes loginGlow {

            from {
                box-shadow:
                  0px 20px 60px rgba(0, 0, 0, 0.45);
    }

            to {
                box-shadow:
                  0px 20px 65px rgba(80, 80, 255, 0.35);
    }

}

        # /* ================================
        # BUTTON HOVER ANIMATION
        # ================================= */

        .stButton > button {
           transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 18px rgba(100, 40, 220, 0.25);
}
        /* ================================
           INPUT BOXES
        ================================= */

        div[data-baseweb="input"] {
            border-radius: 10px !important;
        }

        /* ================================
           BUTTON
        ================================= */

        .stButton > button {
            border-radius: 10px;
            height: 45px;
            font-weight: 600;
        }

        /* ================================
           TABS
        ================================= */

        button[data-baseweb="tab"] {
            font-weight: 600;
        }

        /* ================================
           FOOTER
        ================================= */

        .login-footer {
            text-align: center;
            color: #7f8798;
            font-size: 14px;
            margin-top: 25px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # CENTER THE LOGIN AREA
    # =====================================================

    left, center, right = st.columns(
        [1, 1.6, 1]
    )

    with center:

        # =================================================
        # LOGIN CARD
        # =================================================

        with st.container(border=True):

            # ---------------------------------------------
            # LOGO / TITLE
            # ---------------------------------------------

            # st.markdown(
            #     """
            #     <div style="
            #         text-align:center;
            #         padding-top:10px;
            #     ">

            #         <div style="
            #             font-size:45px;
            #             margin-bottom:5px;
            #         ">
            #             💰
            #         </div>

            #         <h1 style="
            #             font-size:32px;
            #             margin:0;
            #         ">
            #             Finance Analytics
            #         </h1>

            #         <p style="
            #             color:#9da5b5;
            #             font-size:15px;
            #             margin-top:8px;
            #         ">
            #             Smart Personal Finance Management
            #         </p>

            #     </div>
            #     """,
            #     unsafe_allow_html=True
            # )

            # st.write("")

            # ---------------------------------------------
            # WELCOME
            # ---------------------------------------------

            # st.markdown(
            #     """
            #     <div style="text-align:center;">

            #         <h2 style="margin-bottom:5px;">
            #             Welcome Back 👋
            #         </h2>

            #         <p style="
            #             color:#9da5b5;
            #             margin-top:0;
            #         ">
            #             Login to manage your finances
            #         </p>

            #     </div>
            #     """,
            #     unsafe_allow_html=True
            # )

            # st.write("")

            # =================================================
            # LOGIN / REGISTER TABS
            # =================================================

            login_tab, register_tab = st.tabs(
                ["🔐 Login", "📝 Register"]
            )

            # =================================================
            # LOGIN
            # =================================================

            with login_tab:

                username = st.text_input(
                    "Username",
                    placeholder="Enter your username",
                    key="login_username"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password",
                    key="login_password"
                )

                st.write("")

                if st.button(
                    "🔐 Login",
                    # use_container_width=True,
                    width="stretch",
                    key="login_button"
                ):

                    user = login_user(
                        username,
                        password
                    )

                    if user:

                        st.session_state.logged_in = True
                        st.session_state.username = username

                        st.success(
                            "✅ Login successful!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "❌ Invalid username or password."
                        )

            # =================================================
            # REGISTER
            # =================================================

            with register_tab:

                new_username = st.text_input(
                    "Create Username",
                    placeholder="Choose a username",
                    key="register_username"
                )

                new_password = st.text_input(
                    "Create Password",
                    type="password",
                    placeholder="Create a password",
                    key="register_password"
                )

                st.write("")

                if st.button(
                    "📝 Create Account",
                    # use_container_width=True,
                    width="stretch",
                    key="register_button"
                ):

                    if new_username and new_password:

                        result = register_user(
                            new_username,
                            new_password
                        )

                        if result:

                            st.success(
                                "✅ Registration successful! "
                                "You can now login."
                            )

                        else:

                            st.error(
                                "❌ Username already exists."
                            )

                    else:

                        st.warning(
                            "⚠️ Please enter username and password."
                        )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown(
        """
        <div class="login-footer">
            💰 Finance Analytics • Track • Analyze • Improve
        </div>
        """,
        unsafe_allow_html=True
    )
# =========================================================
# MAIN APPLICATION
# =========================================================
else:
    # =====================================================
    # SIDEBAR - MODERN DESIGN
    # =====================================================

    # Sidebar CSS
    st.markdown("""
    <style>

        /* ================= SIDEBAR ================= */

        [data-testid="stSidebar"] {
           background: linear-gradient(
            180deg,
            #17152b 0%,
            #111827 100%
        );
           border-right: 1px solid rgba(255,255,255,0.08);
    }

        [data-testid="stSidebar"] > div:first-child {
          padding-top: 2rem;
          padding-left: 1.2rem;
          padding-right: 1.2rem;
    }

        /* ================= BRAND ================= */

        .sidebar-brand {
         text-align: center;
         padding: 10px 5px 20px 5px;
    }

        .sidebar-logo {
          font-size: 42px;
          margin-bottom: 5px;
    }

        .sidebar-title {
          font-size: 24px;
          font-weight: 700;
          color: white;
          margin: 0;
    }

        .sidebar-subtitle {
          font-size: 12px;
          color: #9da5b4;
          margin-top: 5px;
    }

        /* ================= USER CARD ================= */

        .user-card {
         background: rgba(255,255,255,0.06);
         border: 1px solid rgba(255,255,255,0.08);
         border-radius: 12px;
         padding: 12px;
         margin: 8px 0 20px 0;
    }

        .user-name {
         color: white;
         font-size: 14px;
         font-weight: 600;
    }

        .user-status {
         color: #9da5b4;
         font-size: 11px;
         margin-top: 3px;
    }
   
        /* ================= NAVIGATION TITLE ================= */

        .nav-title {
         color: #9da5b4;
         font-size: 12px;
         font-weight: 600;
         text-transform: uppercase;
         letter-spacing: 1px;
         margin-bottom: 8px;
    }

        /* ================= RADIO BUTTONS ================= */

        [data-testid="stSidebar"] div[role="radiogroup"] {
          gap: 5px;
    }

        [data-testid="stSidebar"] div[role="radiogroup"] label {
         background: transparent;
         border-radius: 10px;
         padding: 9px 10px;
         margin: 2px 0;
         transition: all 0.2s ease;
    }

        [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
         background: rgba(255,255,255,0.08);
    }

        /* Hide radio circles */

        [data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
           display: none;
    }

        /* Navigation text */

        [data-testid="stSidebar"] div[role="radiogroup"] label p {
          color: #d7d9e0;
          font-size: 14px;
          font-weight: 500;
    }

        /* ================= INFO CARD ================= */

        .sidebar-tip {
         background: rgba(59,130,246,0.15);
         border: 1px solid rgba(59,130,246,0.2);
         border-radius: 10px;
         padding: 12px;
         text-align: center;
         color: #93c5fd;
         font-size: 12px;
         margin-top: 15px;
    }

    </style>
    """, unsafe_allow_html=True)

#     # =====================================================
#     # SIDEBAR - MODERN DESIGN
#     # =====================================================

#     # Sidebar CSS

#     is_light = st.session_state.appearance == "☀️ Light Mode"

#     sidebar_bg = (
#        "linear-gradient(180deg, #e0e7ff 0%, #455a77 100%)"
#        if is_light
#        else "linear-gradient(180deg, #17152b 0%, #111827 100%)"
# )

#     sidebar_text = "#0B0929" if is_light else "#ffffff"
#     sidebar_secondary = "#071529" if is_light else "#112853"
#     sidebar_card = (
#        "rgba(0,0,0,0.05)"
#        if is_light
#        else "rgba(255,255,255,0.06)"
#     )
#     sidebar_border = (
#        "rgba(0,0,0,0.10)"
#        if is_light
#        else "rgba(255,255,255,0.08)"
# )
#     nav_text = "#10203A" if is_light else "#d7d9e0"

#     st.markdown(
#        f"""
#        <style>

#             /* ================= SIDEBAR ================= */

#             [data-testid="stSidebar"] {{
#                 background: {sidebar_bg} !important;
#                 border-right: 1px solid {sidebar_border};
#         }}

#             [data-testid="stSidebar"] > div:first-child {{
#                 padding-top: 2rem;
#                 padding-left: 1.2rem;
#                 padding-right: 1.2rem;
#         }}

#             /* ================= BRAND ================= */

#             .sidebar-brand {{
#                text-align: center;
#                padding: 10px 5px 20px 5px;
#         }}

#             .sidebar-logo {{
#                font-size: 42px;
#                margin-bottom: 5px;
#         }}

#             .sidebar-title {{
#                font-size: 24px;
#                font-weight: 700;
#                color: {sidebar_text};
#                margin: 0;
#         }}

#             .sidebar-subtitle {{
#                font-size: 12px;
#                color: {sidebar_secondary};
#                margin-top: 5px;
#         }}

#             /* ================= USER CARD ================= */

#             .user-card {{
#                background: {sidebar_card};
#                border: 1px solid {sidebar_border};
#                border-radius: 12px;
#                padding: 12px;
#                margin: 8px 0 20px 0;
#         }}

#             .user-name {{
#                color: {sidebar_text};
#                font-size: 14px;
#                font-weight: 600;
#         }}

#             .user-status {{
#                color: {sidebar_secondary};
#                font-size: 11px;
#                margin-top: 3px;
#         }}

#             /* ================= NAVIGATION TITLE ================= */

#             .nav-title {{
#                color: {sidebar_secondary};
#                font-size: 12px;
#                font-weight: 600;
#                text-transform: uppercase;
#                letter-spacing: 1px;
#                margin-bottom: 8px;
#         }} 

#             /* ================= RADIO BUTTONS ================= */

#             [data-testid="stSidebar"] div[role="radiogroup"] {{
#                 gap: 5px;
#         }}

#             [data-testid="stSidebar"] div[role="radiogroup"] label {{
#                background: transparent;
#                border-radius: 10px;
#                padding: 9px 10px;
#                margin: 2px 0;
#                transition: all 0.2s ease;
#         }}

#             [data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
#                background: {sidebar_card};
#         }}

#             /* Hide radio circles */

#             [data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {{
#                display: none;
#         }}

#             /* Navigation text */

#             [data-testid="stSidebar"] div[role="radiogroup"] label p {{
#                color: {nav_text};
#                font-size: 14px;
#                font-weight: 500;
#         }}

#             /* ================= INFO CARD ================= */

#             .sidebar-tip {{
#                background: rgba(59,130,246,0.15);
#                border: 1px solid rgba(59,130,246,0.2);
#                border-radius: 10px;
#                padding: 12px;
#                text-align: center;
#                color: #2563eb;
#                font-size: 12px;
#                margin-top: 15px;
#         }}

#         </style>
#         """,
#         unsafe_allow_html=True
# )


# =====================================================
# BRAND
# =====================================================

    st.sidebar.markdown("""
    <div class="sidebar-brand">

      <div class="sidebar-logo">💰</div>

      <div class="sidebar-title">
        Finance Analytics
      </div>

      <div class="sidebar-subtitle">
        Smart Personal Finance
      </div>

    </div>
    """, unsafe_allow_html=True)


# =====================================================
# USER
# =====================================================

    st.sidebar.markdown(f"""
     <div class="user-card">

     <div class="user-name">
        👤 {st.session_state.username}
     </div>

     <div class="user-status">
        ● Account Active
     </div>

    </div>
    """, unsafe_allow_html=True)


# =====================================================
# NAVIGATION
# =====================================================

    st.sidebar.markdown(
       '<div class="nav-title">Navigation</div>',
       unsafe_allow_html=True
)

    menu = st.sidebar.radio(
     "Select a page:",
    [
        "🏠 Home",
        "➕ Add Income",
        "💸 Add Expense",
        "🏦 Bank Statement Import",
        "📊 Dashboard",
        "🤖 AI Prediction",
        "🚨 Anomaly Detection",
        "💡 What-If Simulator",
        "💰 Budget",
        "⚙️ Settings"
    ],
     label_visibility="collapsed"
)


# =====================================================
# BOTTOM TIP
# =====================================================

    st.sidebar.markdown("""
    <div class="sidebar-tip">
    💡 Track • Analyze • Improve
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# LOGOUT
# =====================================================

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    if st.sidebar.button(
       "🔓 Logout",
    #    use_container_width=True
       width="stretch"

):

       st.session_state.logged_in = False
       st.session_state.username = ""

       st.rerun()
    # =====================================================
    # HOME PAGE
    # =====================================================
    if menu == "🏠 Home":
        show_home()
    # # # =====================================================
    # # # ADD INCOME
    # # # =====================================================
    # elif menu == "➕ Add Income":
    #     st.title("➕ Add Income")
    #     income = st.number_input(
    #         "Enter Income (₹)",
    #         min_value=0.0,
    #         step=100.0
    #     )
    #     source = st.selectbox(
    #         "Income Source",
    #         [
    #             "Salary",
    #             "Business",
    #             "Freelancing",
    #             "Investment",
    #             "Other"
    #         ]
    #     )
    #     date = st.date_input("Date")
    #     if st.button("Save Income"):
    #         add_income(
    #             income,
    #             source,
    #             date,
    #             st.session_state.username
    #         )
    #         st.success("✅ Income Saved Successfully!")
    #     st.subheader("Saved Income Records")
    #     records = get_income(st.session_state.username)
    #     if records:

    #         df = pd.DataFrame(
    #             records,
    #             columns=[
    #                 "ID",
    #                 "Income (₹)",
    #                 "Source",
    #                 "Date"
    #             ]
    #         )
    #         # Create user-wise display numbers
    #         df["ID"] = range(1, len(df) + 1)

    #         st.dataframe(
    #             df,
    #             # use_container_width=True,
    #             width="stretch",
    #             hide_index=True
    #         )
    # =====================================================
    # ADD INCOME
    # =====================================================
    elif menu == "➕ Add Income":

        st.title("➕ Add Income")

        income = st.number_input(
            "Enter Income (₹)",
            min_value=1.0,
            step=500.0
    )

        source = st.selectbox(
            "Income Source",
            [
               "Salary",
               "Freelancing",
               "Business",
               "Investment",
               "Other"
        ]
    )

        date = st.date_input(
           "Income Date"
    )

        if st.button("Save Income"):

            add_income(
               income,
               source,
               date,
               st.session_state.username
        )

            st.success(
                "✅ Income Saved Successfully!"
        )

        records = get_income(
            st.session_state.username
    )

        if records:

            st.subheader(
               "Saved Income Records"
        )

            for index, record in enumerate(records):

                db_id = record[0]
                amount = record[1]
                income_source = record[2]
                income_date = record[3]

                col1, col2, col3, col4, col5 = st.columns(
                  [0.8, 2, 2, 2, 1]
            )

                with col1:
                  st.write(index + 1)

                with col2:
                  st.write(
                    f"₹ {amount:,.2f}"
                )

                with col3:
                  st.write(
                    income_source
                )

                with col4:
                  st.write(
                    income_date
                )

                with col5:

                    if st.button(
                        "🗑️",
                        key=f"delete_income_{db_id}"
                ):

                        deleted = delete_income(
                          db_id,
                          st.session_state.username
                    )

                        if deleted:

                          st.success(
                            "✅ Income deleted successfully!"
                        )

                          st.rerun()
    # #=====================================================
    # # ADD EXPENSE
    # # =====================================================
    # elif menu == "💸 Add Expense":
    #     st.title("💸 Add Expense")
    #     expense = st.number_input(
    #         "Enter Expense (₹)",
    #         min_value=1.0,
    #         step=100.0
    #     )
    #     category = st.selectbox(
    #         "Expense Category",
    #         [
    #             "Food",
    #             "Travel",
    #             "Shopping",
    #             "Bills",
    #             "Education",
    #             "Medical",
    #             "Entertainment",
    #             "Other"
    #         ]
    #     )
    #     date = st.date_input(
    #         "Expense Date")
    #     if st.button("Save Expense"):
    #         add_expense(
    #             expense,
    #             category,
    #             date,
    #             st.session_state.username
    #         )
    #         st.success(
    #             "✅ Expense Saved Successfully!")
    #     records = get_expense(st.session_state.username)
    #     if records:
    #         df = pd.DataFrame(
    #             records,
    #             columns=[
    #                 "ID",
    #                 "Expense (₹)",
    #                 "Category",
    #                 "Date"
    #             ]
    #         )
    #         # Create user-wise display numbers
    #         df["ID"] = range(1, len(df) + 1)
    #         st.subheader(
    #             "Saved Expense Records")

    #         st.dataframe(
    #             df,
    #             # use_container_width=True,
    #             width="stretch",
    #             hide_index=True
    #         )
    # =====================================================
    # ADD EXPENSE
    # =====================================================
    elif menu == "💸 Add Expense":

        st.title("💸 Add Expense")

        expense = st.number_input(
            "Enter Expense (₹)",
            min_value=1.0,
            step=100.0
    )

        category = st.selectbox(
            "Expense Category",
            [
               "Food",
               "Travel",
               "Shopping",
               "Bills",
               "Education",
               "Medical",
               "Entertainment",
               "Other"
        ]
    )

        date = st.date_input(
            "Expense Date"
    )

        if st.button("Save Expense"):

            add_expense(
              expense,
              category,
              date,
              st.session_state.username
        )

            st.success(
              "✅ Expense Saved Successfully!"
        )

        records = get_expense(
           st.session_state.username
    )

        if records:

            st.subheader(
            "Saved Expense Records"
        )

            for index, record in enumerate(records):

                db_id = record[0]
                amount = record[1]
                expense_category = record[2]
                expense_date = record[3]

                col1, col2, col3, col4, col5 = st.columns(
                [0.8, 2, 2, 2, 1]
            )

                with col1:
                   st.write(index + 1)

                with col2:
                   st.write(
                    f"₹ {amount:,.2f}"
                )

                with col3:
                  st.write(
                    expense_category
                )

                with col4:
                  st.write(
                    expense_date
                )

                with col5:

                    if st.button(
                        "🗑️",
                        key=f"delete_expense_{db_id}"
                ):

                        deleted = delete_expense(
                          db_id,
                          st.session_state.username
                    )

                        if deleted:

                           st.success(
                            "✅ Expense deleted successfully!"
                        )

                           st.rerun()
    # # =====================================================
    # # BANK STATEMENT IMPORT
    # # =====================================================
    # elif menu == "🏦 Bank Statement Import":

    #     st.title("🏦 Bank Statement Import")

    #     st.write(
    #        "Upload your bank statement in CSV format "
    #        "to import your financial transactions."
    # )

    #     uploaded_file = st.file_uploader(
    #        "📄 Upload Bank Statement (CSV)",
    #        type=["csv"]
    # )

    #     if uploaded_file is not None:

    #         df = pd.read_csv(uploaded_file)

    #         st.subheader("📋 Statement Preview")

    #         st.dataframe(
    #            df,
    #            width="stretch",
    #            hide_index=True
    #     )

    #         st.info(
    #            "ℹ️ Please make sure your CSV contains "
    #            "Date, Description, Amount and Type columns."
    #     )
    #         if st.button("📥 Import Transactions"):

    #             for _, row in df.iterrows():

    #                 if row["Type"].strip().lower() == "income":

    #                     add_income(
    #                         float(row["Amount"]),
    #                         row["Description"],
    #                         row["Date"],
    #                         st.session_state.username
    #         )

    #                 elif row["Type"].strip().lower() == "expense":

    #                     add_expense(
    #                         float(row["Amount"]),
    #                         row["Category"],
    #                         row["Date"],
    #                     st.session_state.username
    #         )

    #             st.success(
    #               "✅ Transactions imported successfully!"
    # )
    # =====================================================
    # BANK STATEMENT IMPORT
    # =====================================================
    # elif menu == "🏦 Bank Statement Import":

    #     st.title("🏦 Bank Statement Import")

    #     st.write(
    #     "Upload your bank statement in CSV format "
    #     "to import your financial transactions."
    # )

    #     uploaded_file = st.file_uploader(
    #         "📄 Upload Bank Statement (CSV)",
    #         type=["csv"]
    # )

    #     if uploaded_file is not None:

    #         df = pd.read_csv(uploaded_file)

    #         st.subheader("📋 Statement Preview")

    #         st.dataframe(
    #            df,
    #            width="stretch",
    #            hide_index=True
    #     )

    #         required_columns = [
    #            "Date",
    #            "Description",
    #            "Amount",
    #            "Type",
    #            "Category"
    #     ]

    #         if all(
    #           column in df.columns
    #           for column in required_columns
    #     ):

    #           if st.button("📥 Import Transactions"):

    #             for _, row in df.iterrows():

    #                 transaction_type = (
    #                     str(row["Type"])
    #                     .strip()
    #                     .lower()
    #                 )

    #                 if transaction_type == "income":

    #                     add_income(
    #                         float(row["Amount"]),
    #                         row["Description"],
    #                         row["Date"],
    #                         st.session_state.username
    #                     )

    #                 elif transaction_type == "expense":

    #                     add_expense(
    #                         float(row["Amount"]),
    #                         row["Category"],
    #                         row["Date"],
    #                         st.session_state.username
    #                     )

    #             st.success(
    #                 "✅ Transactions imported successfully!"
    #             )

    #         else:

    #            st.error(
    #             "❌ CSV must contain: "
    #             "Date, Description, Amount, Type and Category."
    #         )
    elif menu == "🏦 Bank Statement Import":

        st.title("🏦 Bank Statement Import")

        st.write(
          "Upload your bank statement in CSV format "
          "to import your financial transactions."
    )

        uploaded_file = st.file_uploader(
           "📄 Upload Bank Statement (CSV)",
           type=["csv"]
    )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.subheader("📋 Statement Preview")

            st.dataframe(
               df,
               width="stretch",
               hide_index=True
        )

            required_columns = [
               "Date",
               "Description",
               "Amount",
               "Type",
               "Category"
        ]

            if all(
                column in df.columns
                for column in required_columns
        ):

                if st.button("📥 Import Transactions"):
                    imported_count=0
                    duplicate_count=0
                    
                    for _, row in df.iterrows():
                        
                        transaction_type = (
                           str(row["Type"])
                           .strip()
                           .lower()
                    )

                        # new added
                        imported = add_bank_import(
                            row["Date"],
                            row["Description"],
                            float(row["Amount"]),
                            transaction_type,
                            row["Category"],
                            st.session_state.username
                    )

                        if imported:

                            if transaction_type == "income":

                                add_income(
                                    float(row["Amount"]),
                                    row["Description"],
                                    row["Date"],
                                    st.session_state.username
        )

                            elif transaction_type == "expense":

                                add_expense(
                                    float(row["Amount"]),
                                    row["Category"],
                                    row["Date"],
                                    st.session_state.username
                                )
                            imported_count+=1
                        else:
                            duplicate_count+=1
                        
        

                        # if transaction_type == "income":

                        #     add_income(
                        #         float(row["Amount"]),
                        #         row["Description"],
                        #         row["Date"],
                        #         st.session_state.username
                        # )

                        # elif transaction_type == "expense":

                        #     add_expense(
                        #         float(row["Amount"]),
                        #         row["Category"],
                        #         row["Date"],
                        #         st.session_state.username
                        # )

                    #     add_bank_import(
                    #        row["Date"],
                    #        row["Description"],
                    #        float(row["Amount"]),
                    #        transaction_type,
                    #        row["Category"],
                    #        st.session_state.username
                    # )


                    st.success(
                    #   "✅ Transactions imported successfully!"
                    f"✅ {imported_count} new transaction(s) imported."
                )
                    if duplicate_count>0:
                        st.warning( f"⚠️ {duplicate_count} duplicate transaction(s) skipped.")

            else:

                st.error(
                "❌ CSV must contain: "
                "Date, Description, Amount, Type and Category."
            )

        st.divider()

        st.subheader("📋 Imported Bank Transactions")

        imported_records = get_bank_imports(
            st.session_state.username
    )

        if imported_records:

            imported_df = pd.DataFrame(
                imported_records,
                columns=[
                "Date",
                "Description",
                "Amount",
                "Type",
                "Category"
            ]
        )

            st.dataframe(
                imported_df,
                width="stretch",
                hide_index=True
        )

        else:

           st.info(
            "ℹ️ No bank transactions have been imported yet."
        )
    # # =====================================================
    # # DASHBOARD
    # # =====================================================
    elif menu == "📊 Dashboard":
        st.title(
            "📊 Financial Dashboard")
    
        income = total_income(st.session_state.username)
        expense = total_expense(st.session_state.username)
        balance = income - expense
        # -------------------------------------------------
        # FINANCIAL SUMMARY
        # -------------------------------------------------
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                "💰 Total Income",
                f"₹ {income:.0f}"
            )
        with col2:
            st.metric(
                "💸 Total Expense",
                f"₹ {expense:.0f}"
            )
        with col3:
            st.metric(
                "💵 Balance",
                f"₹ {balance:.0f}"
            )
        with col4:
          if income > 0:
           savings_rate = (balance / income) * 100
          else:
           savings_rate = 0
          st.metric(
              "📈 Savings Rate",
              f"{savings_rate:.1f}%"
    )
        # -------------------------------------------------
        # INCOME VS EXPENSE CHART
        # -------------------------------------------------

        st.divider()
        st.subheader("📊 Income vs Expense")

        comparison_df = pd.DataFrame(
            {
                "Type": ["Income", "Expense"],
                "Amount": [income, expense]
            }
        )

        fig = px.bar(
            comparison_df,
            x="Type",
            y="Amount",
            title="",
            text="Amount"
        )

        fig.update_traces(
            texttemplate="₹ %{text:.2f}",
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            # use_container_width=True
            width="stretch"
        )
        # -------------------------------------------------
        # EXPENSE PIE CHART
        # -------------------------------------------------
        st.divider()
        st.subheader("📊 Expense Distribution")
        data = expense_by_category(
        st.session_state.username
    )
        if data:
           total_spending = sum(row[1] for row in data)
           st.info(
            f"💸 You have spent ₹{total_spending:.2f} in total."
        )
           categories = [row[0] for row in data]
           amounts = [row[1] for row in data]
           fig = px.pie(
            names=categories,
            values=amounts,
            title="Expenses by Category"
        )
           st.plotly_chart(
            fig,
            # use_container_width=True
            width="stretch"
        )
        else:
         st.info("No expense data available.")
        # -------------------------------------------------
        # EXPENSE CATEGORY ANALYSIS
        # -------------------------------------------------
        st.divider()
        st.subheader("🔍 Spending Analysis")
        category_data = expense_by_category(st.session_state.username)
        if category_data:
            categories = [
                row[0]
                for row in category_data
            ]
            amounts = [
                row[1]
                for row in category_data
            ]
            # Find highest spending category
            highest_index = amounts.index(
                max(amounts)
            )
            highest_category = categories[
                highest_index
            ]
            highest_amount = amounts[
                highest_index
            ]
            # Calculate percentage
            total_spending = sum(amounts)
            spending_percentage = (
                highest_amount / total_spending
            ) * 100
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    "🏆 Highest Spending",
                    highest_category
                )
            with col2:
                st.metric(
                    "💸 Amount Spent",
                    f"₹ {highest_amount:.2f}"
                )
            with col3:
                st.metric(
                    "📊 Percentage",
                    f"{spending_percentage:.1f}%"
                )
            # Financial insight
            if spending_percentage >= 40:
                st.warning(
                    f"⚠️ {highest_category} is your "
                    f"largest expense category. "
                    f"Consider reducing unnecessary "
                    f"spending in this category."
                )
            elif spending_percentage >= 25:
                st.info(
                    f"💡 {highest_category} takes a "
                    f"significant portion of your spending."
                )
            else:
                st.success(
                    f"✅ Your spending is reasonably "
                    f"distributed across categories."
                )
        else:
            st.info(
                "Add expenses to generate spending analysis.")
        # -------------------------------------------------
        # FINANCIAL HEALTH SCORE
        # -------------------------------------------------
        st.divider()

        st.subheader("🏦 Financial Health Score")

        # Calculate savings rate
        if income > 0:

            savings_rate = (
                balance / income
            ) * 100
        else:
            savings_rate = 0
        # Calculate health score
        health_score = 0
        # Savings rate points
        if savings_rate >= 50:

            health_score += 50

        elif savings_rate >= 30:

            health_score += 40

        elif savings_rate >= 20:

            health_score += 30

        elif savings_rate >= 10:

            health_score += 20

        elif savings_rate > 0:

            health_score += 10

        # Expense control points

        if income > 0:

            expense_percentage = (
            expense / income
        ) * 100

            if expense_percentage <= 50:
               health_score += 50

            elif expense_percentage <= 70:
               health_score += 40

            elif expense_percentage <= 80:
               health_score += 30

            elif expense_percentage <= 90:
               health_score += 20

            elif expense_percentage <= 100:
               health_score += 10

        else:

          expense_percentage = 0
        # # Expense control points
      


        # Display score
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🏦 Financial Health Score",
                f"{health_score}/100"
            )
        with col2:
            st.metric(
                "📈 Savings Rate",
                f"{savings_rate:.1f}%"
            )


        # Financial health message
        if income == 0 and expense == 0:

           st.info(
             "⚪ Add income and expenses to assess your financial health."
    )
        elif health_score >= 80:

            st.success(
                "🟢 Excellent Financial Health! "
                "Your savings and spending are well managed."
            )

        elif health_score >= 60:

            st.info(
                "🟡 Good Financial Health. "
                "You are managing your finances reasonably well."
            )

        elif health_score >= 40:

            st.warning(
                "🟠 Financial Health Needs Improvement. "
                "Try to increase savings and reduce unnecessary expenses."
            )

        else:

            st.error(
                "🔴 Financial Health Needs Attention. "
                "Your expenses are high compared with your income."
            )

        # -------------------------------------------------
        # AI FINANCIAL SUGGESTION
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "💡 AI Financial Suggestion"
        )

        if income == 0:

            st.warning(
                "Please add income first."
            )

        else:

            # saving_percentage = (
            #     saving / income
            # ) * 100
            saving_percentage = (
                balance / income
            ) * 100

            if saving_percentage >= 50:

                st.success(
                    "🎉 Excellent! You are saving "
                    "more than 50% of your income."
                )

            elif saving_percentage >= 30:

                st.info(
                    "👍 Good! Your savings are healthy."
                )

            elif saving_percentage >= 10:

                st.warning(
                    "⚠️ Try to reduce unnecessary expenses."
                )

            else:

                st.error(
                    "🚨 Your expenses are too high. "
                    "Consider planning a monthly budget."
                )

                st.divider()

        st.subheader("📄 Financial Report")

        if st.button("Generate Financial Report"):

            report_file = create_financial_report(
                st.session_state.username,
                income,
                expense,
                balance
            )

            with open(report_file, "rb") as file:

                st.download_button(
                    label="📥 Download Financial Report",
                    data=file,
                    file_name="financial_report.pdf",
                    mime="application/pdf"
                )
        # -------------------------------------------------
        # EXPORT FINANCIAL DATA
        # -------------------------------------------------
        st.divider()
        st.subheader(
            "📥 Export Financial Data"
        )
        # =========================================================
        # EXPORT INCOME DATA
        # =========================================================

        income_records = get_income(st.session_state.username)

        if income_records:
            income_df = pd.DataFrame(
               income_records,
               columns=[
                   "ID",
                   "Income (₹)",
                   "Source",
                   "Date"
                ]
             )

    # Remove the database ID column for export
            income_export_df = income_df.drop(columns=["ID"])

            income_csv = income_export_df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
              label="📥 Download Income Data",
              data=income_csv,
              file_name="income_data.csv",
              mime="text/csv"
    )

        else:
           st.info("No income data available.")


# =========================================================
# EXPORT EXPENSE DATA
# =========================================================

        expense_records = get_expense(st.session_state.username)

        if expense_records:
            expense_df = pd.DataFrame(
               expense_records,
               columns=[
                  "ID",
                  "Expense (₹)",
                  "Category",
                  "Date"
        ]
    )

    # Remove the database ID column for export
            expense_export_df = expense_df.drop(columns=["ID"])

            expense_csv = expense_export_df.to_csv(
               index=False
            ).encode("utf-8")

            st.download_button(
               label="📥 Download Expense Data",
               data=expense_csv,
               file_name="expense_data.csv",
               mime="text/csv"
    )

        else:
             st.info("No expense data available.")
# =====================================================
# AI PREDICTION
# =====================================================
    elif menu == "🤖 AI Prediction":

       st.title("🤖 AI Monthly Expense Prediction")

       st.write(
        "Analyze your previous monthly spending and "
        "estimate your next month's total expenses."
    )

    # Get user's expense records
       data = get_expense(
        st.session_state.username
    )

       if len(data) >= 2:

        # -------------------------------------------------
        # CREATE MONTHLY EXPENSE TOTALS
        # -------------------------------------------------

        monthly_data = {}

        for row in data:

            amount = float(row[1])
            date = str(row[3])

            month = date[:7]

            if month not in monthly_data:
                monthly_data[month] = 0

            monthly_data[month] += amount

        sorted_months = sorted(
            monthly_data.keys()
        )

        monthly_expenses_list = [
            monthly_data[month]
            for month in sorted_months
        ]

        # -------------------------------------------------
        # MONTHLY PREDICTION
        # -------------------------------------------------

        if len(monthly_expenses_list) >= 2:

            average_monthly_expense = (
                sum(monthly_expenses_list)
                / len(monthly_expenses_list)
            )

            highest_monthly_expense = max(
                monthly_expenses_list
            )

            lowest_monthly_expense = min(
                monthly_expenses_list
            )

            X = np.arange(
                len(monthly_expenses_list)
            ).reshape(-1, 1)

            y = np.array(
                monthly_expenses_list
            )

            model = LinearRegression()

            model.fit(
                X,
                y
            )
            if len(monthly_expenses_list) < 3:

    # Use average when there is very little history
              prediction = average_monthly_expense

            else:

              prediction = model.predict(
              [[len(monthly_expenses_list)]]
              )[0]

    # Keep prediction realistic
              prediction = max(
                 prediction,
                 average_monthly_expense * 0.5
                )

              prediction = min(
                 prediction,
                 average_monthly_expense * 1.5
                )
            # -------------------------------------------------
            # SPENDING TREND
            # -------------------------------------------------

            # if model.coef_[0] > 0:

            #     trend = "📈 Increasing"

            #     trend_message = (
            #         "Your monthly spending is showing an "
            #         "increasing trend."
            #     )

            # elif model.coef_[0] < 0:

            #     trend = "📉 Decreasing"

            #     trend_message = (
            #         "Your monthly spending is showing a "
            #         "decreasing trend."
            #     )

            # else:

            #     trend = "➡️ Stable"

            #     trend_message = (
            #         "Your monthly spending is relatively stable."
            #     )
            if len(monthly_expenses_list) < 3:

                trend = "➡️ Not enough data"

                trend_message = (
                   "Add expenses for at least 3 months "
                   "to identify a more meaningful spending trend."
              )

            elif model.coef_[0] > 0:

                trend = "📈 Increasing"

                trend_message = (
                   "Your monthly spending is showing an "
                   "increasing trend."
                )

            elif model.coef_[0] < 0:

                trend = "📉 Decreasing"

                trend_message = (
                   "Your monthly spending is showing a "
                   "decreasing trend."
                )

            else:

                trend = "➡️ Stable"

                trend_message = (
                    "Your monthly spending is relatively stable."
                )

            # -------------------------------------------------
            # PREDICTION RESULT
            # -------------------------------------------------

            st.divider()

            st.subheader(
                "🤖 Next Month Prediction"
            )

            st.success(
                f"📅 Predicted Next-Month Expense: "
                f"₹ {prediction:.2f}"
            )

            # -------------------------------------------------
            # MONTHLY SUMMARY
            # -------------------------------------------------

            st.subheader(
                "📊 Monthly Expense Summary"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "💰 Average Monthly Expense",
                    f"₹ {average_monthly_expense:.2f}"
                )

            with col2:

                st.metric(
                    "🔺 Highest Monthly Expense",
                    f"₹ {highest_monthly_expense:.2f}"
                )

            with col3:

                st.metric(
                    "🔻 Lowest Monthly Expense",
                    f"₹ {lowest_monthly_expense:.2f}"
                )

            # -------------------------------------------------
            # TREND
            # -------------------------------------------------

            st.divider()

            st.subheader(
                "📈 Monthly Spending Trend"
            )

            st.info(
                f"Current trend: **{trend}**\n\n"
                f"{trend_message}"
            )

            # -------------------------------------------------
            # MONTHLY CHART
            # -------------------------------------------------

            # st.subheader(
            #     "📉 Monthly Expense History"
            # )

            # chart_data = pd.DataFrame(
            #     {
            #         "Month": sorted_months,
            #         "Expense": monthly_expenses_list
            #     }
            # )

            # chart_data = chart_data.set_index(
            #     "Month"
            # )

            # st.line_chart(
            #     chart_data
            # )
            st.subheader("📉 Monthly Expense History")

            chart_data = pd.DataFrame(
              {
                "Month": sorted_months,
                "Expense": monthly_expenses_list
              }
            )

            fig = px.line(
                chart_data,
                x="Month",
                y="Expense",
                markers=True,
                title=""
            )

            fig.update_traces(
                line=dict(width=3),
                marker=dict(size=8)
            )

            fig.update_layout(
                xaxis_title="Month",
                yaxis_title="Expense (₹)",
                hovermode="x unified",
                xaxis_type="category"
            )

            fig.update_yaxes(
                tickprefix="₹ "
            )
            st.plotly_chart(
                fig,
                # use_container_width=True
                width="stretch"
            )

            # -------------------------------------------------
            # SMART FINANCIAL SUGGESTION
            # -------------------------------------------------

            st.subheader(
                "💡 Financial Suggestion"
            )

            if prediction > average_monthly_expense:

                difference = (
                    prediction
                    - average_monthly_expense
                )

                st.warning(
                    f"⚠️ Your predicted next-month "
                    f"expense is ₹ {difference:.2f} "
                    f"higher than your average monthly "
                    f"spending. Consider reducing "
                    f"unnecessary expenses."
                )

            elif prediction < average_monthly_expense:

                difference = (
                    average_monthly_expense
                    - prediction
                )

                st.success(
                    f"✅ Your predicted next-month "
                    f"expense is ₹ {difference:.2f} "
                    f"lower than your average monthly "
                    f"spending. Keep maintaining "
                    f"good spending habits!"
                )

            else:

                st.info(
                    "ℹ️ Your predicted next-month "
                    "expense is close to your average "
                    "monthly spending."
                )

        else:

            st.warning(
                "⚠️ You need expenses from at least "
                "2 different months to generate a "
                "monthly prediction."
            )

            st.info(
                "Add expenses in different months "
                "to generate a meaningful monthly "
                "prediction."
            )

       else:

        st.warning(
            "⚠️ Add at least 2 expense records "
            "to start the prediction."
        )

        st.info(
            "Go to ➕ Add Expense and add some "
            "expense records first."
        )

    # =====================================================
    # HIGHEST SPENDING CATEGORY INSIGHT
    # =====================================================

       st.divider()

       st.subheader(
        "🏆 Highest Spending Category"
    )

       category_data = expense_by_category(
        st.session_state.username
    )

       if category_data:

        highest_category = max(
            category_data,
            key=lambda x: x[1]
        )

        category_name = highest_category[0]
        category_amount = highest_category[1]

        st.warning(
            f"🏆 Your highest spending category is "
            f"**{category_name}** with total spending of "
            f"**₹ {category_amount:.2f}**."
        )

        st.info(
            f"💡 Consider reviewing your spending in "
            f"**{category_name}** and reducing unnecessary "
            f"expenses where possible."
        )

       else:

        st.info(
            "No expense category data available yet."
        )

    # =====================================================
    # CATEGORY SPENDING PERCENTAGE
    # =====================================================

        st.divider()

        st.subheader(
           "📊 Category Spending Breakdown"
)

        if category_data:

         total_category_expense = sum(
            amount
            for category, amount in category_data
    )

         category_percentage_data = []

         for category, amount in category_data:

          percentage = (
            amount
            / total_category_expense
        ) * 100

          category_percentage_data.append(
            [
                category,
                amount,
                percentage
            ]
        )

    # Sort from highest to lowest spending
         category_percentage_data.sort(
            key=lambda x: x[1],
            reverse=True
    )

    # -------------------------------------------------
    # DISPLAY ALL CATEGORIES
    # -------------------------------------------------

         for category, amount, percentage in category_percentage_data:

          col1, col2, col3 = st.columns(
            [2, 1, 1]
        )

          with col1:
            st.write(
                f"**{category}**"
            )

          with col2:
            st.write(
                f"₹ {amount:.2f}"
            )

          with col3:
            st.write(
                f"{percentage:.1f}%"
            )

    # -------------------------------------------------
    # CATEGORY INSIGHT
    # -------------------------------------------------

         top_category = category_percentage_data[0]

         top_category_name = top_category[0]

         top_category_percentage = top_category[2]

         if top_category_percentage >= 50:

            st.warning(
            f"⚠️ **{top_category_name}** accounts for "
            f"{top_category_percentage:.1f}% of your total "
            f"expenses. Consider reviewing this category "
            f"to control your spending."
        )

         elif top_category_percentage >= 30:

               st.info(
            f"💡 **{top_category_name}** accounts for "
            f"{top_category_percentage:.1f}% of your total "
            f"expenses. Keep an eye on this category."
        )

         else:

                st.success(
            f"✅ Your spending is relatively distributed "
            f"across categories. Your highest category, "
            f"**{top_category_name}**, represents only "
            f"{top_category_percentage:.1f}% of total expenses."
        )

        else:

          st.info(
        "Add expenses to see your category spending breakdown."
    )
# ====================================
# "🚨 Anomaly Detection"
# ====================================
    # ====================================
# "🚨 Anomaly Detection"
# ====================================
    elif menu == "🚨 Anomaly Detection":

        st.title("🚨 Expense Anomaly Detection")

        st.write(
        "Detect unusually high expenses using Machine Learning."
    )

        # Get expense records
        records = get_expense(
            st.session_state.username
    )

        if not records:

           st.info(
            "💡 Add some expenses first to detect unusual spending."
        )

        elif len(records) < 5:

           st.warning(
            "⚠️ At least 5 expense records are recommended "
            "for meaningful anomaly detection."
        )

        else:

            from sklearn.ensemble import IsolationForest

        # Create DataFrame
            df = pd.DataFrame(
                records,
                columns=[
                   "ID",
                   "Expense (₹)",
                   "Category",
                   "Date"
            ]
        )

        # Convert expense amount to numeric
            df["Expense (₹)"] = pd.to_numeric(
                df["Expense (₹)"]
        )

        # --------------------------------
        # Machine Learning Model
        # --------------------------------

            model = IsolationForest(
                contamination=0.1,
                random_state=42
        )

            df["Prediction"] = model.fit_predict(
                 df[["Expense (₹)"]]
        )

        # --------------------------------
        # Finance-specific high expense check
        # --------------------------------

            q1 = df["Expense (₹)"].quantile(0.25)
            q3 = df["Expense (₹)"].quantile(0.75)

            iqr = q3 - q1

            upper_limit = q3 + (1.5 * iqr)

        # Mark unusual only when the expense is
        # unusually HIGH compared with normal spending
            df["Is_Anomaly"] = (
                (df["Prediction"] == -1)
                &
                (df["Expense (₹)"] > upper_limit)
        )

        # Convert result into readable status
            df["Status"] = df["Is_Anomaly"].apply(
                lambda x: "🚨 Unusual" if x else "✅ Normal"
        )

        # --------------------------------
        # Expense Analysis Table
        # --------------------------------

            st.subheader("🔍 Expense Analysis")

            display_df = df[
               [
                   "Expense (₹)",
                   "Category",
                   "Date",
                   "Status"
               ]
        ]

            st.dataframe(
                display_df,
                width="stretch",
                hide_index=True
        )

        # --------------------------------
        # Anomaly Count
        # --------------------------------

            anomaly_count = (
               df["Is_Anomaly"]
            ).sum()

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                   "Total Expenses",
                   len(df)
            )

            with col2:

                st.metric(
                   "Unusual Expenses",
                   anomaly_count
            ) 

        # --------------------------------
        # Alert Message
        # --------------------------------

            if anomaly_count > 0:

                st.error(
                    f"🚨 {anomaly_count} unusually high "
                    f"expense(s) detected. Please review them."
            )

            else:

                st.success(
                    "✅ No unusually high expenses were detected."
            )

            st.caption(
              "ℹ️ The system uses Isolation Forest Machine Learning "
              "along with statistical analysis to identify unusually "
              "high spending. An unusual expense is not necessarily "
              "an incorrect transaction."
        )
#======================================
#What-If Simulator"
# =====================================

    elif menu == "💡 What-If Simulator":

     st.title("💡 What-If Financial Simulator")

     st.write(
        "See how reducing your spending could increase your savings."
    )

     income = total_income(
        st.session_state.username
    )

     data = expense_by_category(
        st.session_state.username
    )

     if income <= 0:

        st.info(
            "💡 Add some income first to use the simulator."
        )

     elif not data:

        st.info(
            "💡 Add some expenses first to use the simulator."
        )

     else:

        categories = [
            row[0]
            for row in data
        ]

        amounts = [
            float(row[1])
            for row in data
        ]

        total_expenses = sum(amounts)

        # Category selection

        selected_category = st.selectbox(
            "Choose an expense category",
            categories
        )

        selected_index = categories.index(
            selected_category
        )

        selected_amount = amounts[
            selected_index
        ]

        st.metric(
            "💸 Current Category Spending",
            f"₹ {selected_amount:,.0f}"
        )

        # Reduction slider

        reduction = st.slider(
            "How much would you reduce this spending?",
            min_value=0,
            max_value=50,
            value=20,
            step=5
        )

        # Calculations

        monthly_saving = (
            selected_amount * reduction / 100
        )

        simulated_category_spending = (
            selected_amount - monthly_saving
        )

        simulated_total_expense = (
            total_expenses - monthly_saving
        )

        current_savings = (
            income - total_expenses
        )

        simulated_savings = (
            income - simulated_total_expense
        )

        yearly_saving = (
            monthly_saving * 12
        )

        # Current vs Simulated

        st.divider()

        st.subheader(
            "📊 Current vs Simulated"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### 🔵 Current")

            st.metric(
                "Total Spending",
                f"₹ {total_expenses:,.0f}"
            )

            st.metric(
                "Savings",
                f"₹ {current_savings:,.0f}"
            )

        with col2:

            st.markdown("### 🟣 Simulated")

            st.metric(
                "Total Spending",
                f"₹ {simulated_total_expense:,.0f}",
                delta=f"-₹ {monthly_saving:,.0f}"
            )

            st.metric(
                "Savings",
                f"₹ {simulated_savings:,.0f}",
                delta=f"+₹ {monthly_saving:,.0f}"
            )

        # Potential savings

        st.divider()

        st.subheader(
            "📈 Your Potential Savings"
        )

        st.success(
            f"💡 By reducing your "
            f"{selected_category} spending by "
            f"{reduction}%, you could save "
            f"₹ {monthly_saving:,.0f} more every month."
        )

        st.info(
            f"🗓️ If you maintain this change for "
            f"one year, you could save an additional "
            f"₹ {yearly_saving:,.0f}."
        )

        # Category comparison

        st.subheader(
            "🔎 Category Simulation"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Current Category Spending",
                f"₹ {selected_amount:,.0f}"
            )

        with col2:

            st.metric(
                "Simulated Category Spending",
                f"₹ {simulated_category_spending:,.0f}"
            )

        st.caption(
            "ℹ️ This is only a simulation. "
            "Your actual expense records are not changed."
        )
# =====================================================
# BUDGET MANAGEMENT
# =====================================================
    elif menu == "💰 Budget":

        st.title("💰 Monthly Budget")

        st.write(
            "Set a monthly spending limit and monitor your expenses."
        )

        # ---------------------------------------------
        # SET MONTHLY BUDGET
        # ---------------------------------------------

        budget = st.number_input(
            "Enter Monthly Budget (₹)",
            min_value=0.0,
            step=500.0,
            value=st.session_state.monthly_budget
        )

        if st.button("💾 Save Budget"):

            st.session_state.monthly_budget = budget

            st.success(
                "✅ Monthly budget saved successfully!"
            )

        current_expense = total_expense(
            st.session_state.username
        )

        st.divider()

        # ---------------------------------------------
        # NO BUDGET SET
        # ---------------------------------------------

        if st.session_state.monthly_budget == 0:

            st.subheader("📊 Budget Tracking")

            st.info(
                "💡 No monthly budget has been set yet. "
                "Set a budget above to start tracking your spending."
            )

        # ---------------------------------------------
        # BUDGET IS SET
        # ---------------------------------------------

        else:

            monthly_budget = st.session_state.monthly_budget

            remaining = monthly_budget - current_expense

            # -----------------------------------------
            # BUDGET SUMMARY
            # -----------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "💰 Monthly Budget",
                    f"₹ {monthly_budget:,.2f}"
                )

            with col2:

                st.metric(
                    "💸 Current Expense",
                    f"₹ {current_expense:,.2f}"
                )

            with col3:

                st.metric(
                    "💵 Remaining Budget",
                    f"₹ {remaining:,.2f}"
                )

            st.divider()

            # -----------------------------------------
            # BUDGET USAGE
            # -----------------------------------------

            st.subheader("📊 Budget Usage")

            percentage_used = (
                current_expense / monthly_budget
            ) * 100

            # Keep progress bar between 0 and 100
            progress = min(
                max(percentage_used / 100, 0.0),
                1.0
            )

            st.progress(progress)

            st.write(
                f"₹ {current_expense:,.2f} "
                f"of ₹ {monthly_budget:,.2f} spent"
            )

            st.caption(
                f"{percentage_used:.1f}% of your monthly budget used"
            )

            # -----------------------------------------
            # BUDGET STATUS
            # -----------------------------------------

            if current_expense > monthly_budget:

                exceeded = (
                    current_expense - monthly_budget
                )

                st.error(
                    f"🚨 Budget exceeded by "
                    f"₹ {exceeded:,.2f}"
                )

            elif percentage_used >= 80:

                st.warning(
                    f"⚠️ You have used {percentage_used:.1f}% "
                    "of your budget. Spend carefully."
                )

            else:

                st.success(
                    f"✅ You are within your budget. "
                    f"You have {remaining:,.2f} remaining."
                )

# =====================================================
# SETTINGS
# =====================================================
    elif menu == "⚙️ Settings":

      
      st.title("⚙️ Settings")
    # =================================================
    # SETTINGS PAGE
    # =================================================

      st.markdown(
        '<div class="settings-title"></div>',
        unsafe_allow_html=True
    )

    # =================================================
    # PROFILE
    # =================================================

    #   if "profile_picture" not in st.session_state:
    #     st.session_state.profile_picture = None

    #   if "profile_picture_type" not in st.session_state:
    #     st.session_state.profile_picture_type = None

    # ---------- PROFILE DISPLAY ----------

      col1, col2 = st.columns([1, 3])

      with col1:

        # if st.session_state.profile_picture:

        #     picture_base64 = base64.b64encode(
        #         st.session_state.profile_picture
        #     ).decode("utf-8")

        #     picture_type = st.session_state.get(
        #         "profile_picture_type",
        #         "image/jpeg"
        #     )

        #     st.markdown(
        #         f"""
        #         <div style="
        #             width:130px;
        #             height:130px;
        #             border-radius:50%;
        #             overflow:hidden;
        #             border:4px solid #6366f1;
        #             box-shadow:0 8px 20px rgba(99,102,241,0.35);
        #             margin-top:10px;
        #         ">
        #             <img
        #                 src="data:{picture_type};base64,{picture_base64}"
        #                 style="
        #                     width:100%;
        #                     height:100%;
        #                     object-fit:cover;
        #                 "
        #             >
        #         </div>
        #         """,
        #         unsafe_allow_html=True
        #     )

        # else:

            st.markdown(
                """
                <div style="
                    width:130px;
                    height:130px;
                    border-radius:50%;
                    background:linear-gradient(135deg,#4f46e5,#7c3aed);
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:55px;
                    border:4px solid #6366f1;
                ">
                    👤
                </div>
                """,
                unsafe_allow_html=True
            )

      with col2:

        st.markdown(
            f"""
            <div style="
                font-size:28px;
                font-weight:700;
                margin-top:5px;
            ">
                {st.session_state.username}
            </div>

            <div style="
                color:#86efac;
                font-size:14px;
                margin-top:6px;
            ">
                ● Account Active
            </div>

            <div style="
                font-size:16px;
                margin-top:8px;
            ">
                Personal Finance Account
            </div>
            """,
            unsafe_allow_html=True
        )
    # =================================================
    # ACCOUNT INFORMATION
    # =================================================

      st.subheader("📋 Account Information")

      col1, col2 = st.columns(2)

      with col1:
         st.markdown("**USERNAME**")
         st.write(f"👤 {st.session_state.username}")

      with col2:
         st.markdown("**ACCOUNT STATUS**")
         st.success("● Active")


      st.divider()
    
    # =====================================================
    # APPEARANCE
    # =====================================================

    #   st.subheader("🎨 Appearance")

    #   st.session_state.appearance = st.radio(
    #     "Choose Theme",
    #     ["🌙 Dark Mode", "☀️ Light Mode"],
    #     index=0 if st.session_state.appearance == "🌙 Dark Mode" else 1,
    #     horizontal=True
    # )

    #   if st.session_state.appearance == "☀️ Light Mode":
    #       st.info("☀️ Light Mode selected")
    #   else:
    #       st.info("🌙 Dark Mode selected")
    # =================================================
    # FINANCIAL PREFERENCES
    # =================================================

#       st.subheader("💰 Financial Preferences")

#       currency = st.selectbox(
#         "💱 Select Currency",
#         ["₹ INR", "$ USD", "€ EUR", "£ GBP"],
#         key="currency_setting"
# )

#       st.caption(
#        f"Your selected currency: {currency}"
# )

#       st.divider()

    # =================================================
    # CHANGE PASSWORD
    # =================================================

      st.subheader("🔐 Change Password")

      current_password = st.text_input(
          "Current Password",
          type="password",
          key="settings_current_password"
    )

      new_password = st.text_input(
          "New Password",
          type="password",
          key="settings_new_password"
    )

      confirm_password = st.text_input(
          "Confirm New Password",
          type="password",
          key="settings_confirm_password"
    )

      if st.button(
          "🔐 Change Password",
          key="change_password_button"
    ):

            if not current_password or not new_password or not confirm_password:

              st.warning(
                "⚠️ Please fill in all password fields."
            )

            elif new_password != confirm_password:

              st.error(
                "❌ New passwords do not match."
            )

            elif current_password == new_password:

              st.warning(
                "⚠️ New password must be different "
                "from your current password."
            )

            else:

              user = login_user(
                st.session_state.username,
                current_password
            )

              if user:

                success = change_password(
                    st.session_state.username,
                    new_password
                )

                if success:
                    st.success(
                        "✅ Password changed successfully!"
                    )

              else:

                st.error(
                    "❌ Current password is incorrect."
                )


      st.divider()


    # =================================================
    # DELETE FINANCIAL DATA
    # =================================================

      st.subheader("🗑️ Delete Financial Data")

      st.warning(
        "This will permanently delete all your "
        "income and expense records."
    )

    #   st.info(
    #         "Your login account will NOT be deleted."
    # )

      if st.session_state.get(
        "delete_success",
        False
    ):

          st.success(
            "✅ Your financial data has been deleted successfully."
        )

          st.session_state.delete_success = False


      if st.button(
        "🗑️ Delete My Data",
        key="delete_financial_data_button"
    ):

          st.session_state.show_delete_confirmation = True


      if st.session_state.get(
        "show_delete_confirmation",
        False
    ):

          st.error(
            "⚠️ Are you sure? This action cannot be undone."
        )

          col1, col2 = st.columns(2)

          with col1:

            if st.button(
                "❌ Cancel",
                key="cancel_delete"
            ):

                st.session_state.show_delete_confirmation = False
                st.rerun()

          with col2:

            if st.button(
                "✅ Yes, Delete My Data",
                key="confirm_delete"
            ):

                delete_user_financial_data(
                    st.session_state.username
                )

                st.session_state.show_delete_confirmation = False
                st.session_state.delete_success = True

                st.rerun()


      st.divider()


    # =================================================
    # ABOUT ACCOUNT
    # =================================================

      st.subheader("ℹ️ About Your Account")

      st.write(
        "Your login account remains active even when "
        "you delete your financial records."
    )

      st.write(
        "🔒 Your financial data is associated with your "
        "personal account."
    )


      st.divider()

      st.caption(
        "💰 Finance Analytics • Account Settings"
    )