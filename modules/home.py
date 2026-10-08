
# import streamlit as st
# # =====================================================
# # HOME PAGE ANIMATION
# # =====================================================

# st.markdown(
#     """
#     <style>

#     .home-animation {
#         animation: homeFadeIn 0.8s ease-out;
#     }
    
#     @keyframes homeFadeIn {

#         from {
#             opacity: 0;
#             transform: translateY(20px);
#         }

#         to {
#             opacity: 1;
#             transform: translateY(0);
#         }

#     }

    
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# def show_home():
#     # =====================================================
#     # HERO SECTION
#     # =====================================================
#     st.markdown("""
#     <div class="home-animation" style="
#        background: linear-gradient(135deg, #1e1b4b, #312e81, #4338ca);
#        padding: 35px;
#        border-radius: 22px;
#        margin-bottom: 25px;
#        border: 1px solid rgba(255,255,255,0.12);
#     ">

#        <div style="
#          font-size: 42px;
#          font-weight: 700;
#          color: white;
#          margin-bottom: 8px;
#        ">
#          💰 Finance Analytics
#        </div>

#        <div style="
#          font-size: 23px;
#          font-weight: 600;
#          color: #e0e7ff;
#          margin-bottom: 12px;
#        ">
#          Smart Personal Finance Management
#        </div>

#        <div style="
#          font-size: 15px;
#          color: #c7d2fe;
#          margin-bottom: 20px;
#        ">
#          Track your money • Understand your spending •
#          Make smarter financial decisions
#        </div>

#        <div style="
#          display: inline-block;
#          background: rgba(255,255,255,0.12);
#          padding: 8px 14px;
#          border-radius: 20px;
#          color: white;
#          font-size: 13px;
#        ">
#         ✨ Smart Finance Dashboard
#        </div>

#     </div>
#     """, unsafe_allow_html=True)
#     # =====================================================
#     # WELCOME
#     # =====================================================
#     st.header("👋 Welcome!")

#     st.write(
#         "Manage your personal finances in one place. "
#         "Track income and expenses, analyze spending habits, "
#         "monitor your financial health, and get useful "
#         "financial insights."
#     )
#     # =====================================================
#     # WHAT YOU CAN DO
#     # =====================================================
#     st.divider()
#     st.header("✨ What You Can Do")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         with st.container(border=True):
#             st.markdown("### 💰 Track Income")
#             st.write(
#                 "Record your salary, business income, "
#                 "freelancing, investments and other "
#                 "sources of income."
#             )

#     with col2:
#         with st.container(border=True):
#             st.markdown("### 💸 Track Expenses")
#             st.write(
#                 "Record your daily expenses and organize "
#                 "them into categories such as food, "
#                 "travel, bills and shopping."
#             )

#     with col3:
#         with st.container(border=True):
#             st.markdown("### 📊 Analyze Finances")
#             st.write(
#                 "Understand your spending patterns, "
#                 "savings rate, financial health and "
#                 "overall financial performance."
#             )
#     # =====================================================
#     # AI INSIGHTS
#     # =====================================================
#     st.divider()
#     st.header("🤖 Intelligent Financial Insights")
#     st.write(
#         "Use your financial data to understand your "
#         "spending behavior and make better decisions."
#     )

#     col1, col2 = st.columns(2)

#     with col1:
#         with st.container(border=True):
#             st.markdown("### 📈 Financial Analysis")

#             st.write("• View income and expenses")
#             st.write("• Monitor your balance")
#             st.write("• Analyze spending categories")
#             st.write("• Check your financial health")

#     with col2:
#         with st.container(border=True):
#             st.markdown("### 💡 Smart Suggestions")

#             st.write("• Understand spending trends")
#             st.write("• Get financial suggestions")
#             st.write("• Monitor your budget")
#             st.write("• Predict future expenses")


#     # =====================================================
#     # GET STARTED
#     # =====================================================

#     st.divider()

#     st.header("🚀 Get Started")

#     st.write(
#         "Use the sidebar to explore the features "
#         "of your Finance Analytics application."
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         with st.container(border=True):
#             st.markdown("### ➕ Add Income")
#             st.write("Record your income.")

#     with col2:
#         with st.container(border=True):
#             st.markdown("### 💸 Add Expense")
#             st.write("Track your spending.")

#     with col3:
#         with st.container(border=True):
#             st.markdown("### 📊 Dashboard")
#             st.write("Analyze your finances.")


#     # =====================================================
#     # FOOTER
#     # =====================================================

#     st.divider()

#     st.caption(
#         "💰 Finance Analytics • Track • Analyze • Improve"
#     )





# 
# 
# 
# 
# import streamlit as st


# def show_home():
#       # =====================================================
#      # HERO SECTION
#      # =====================================================
#     st.markdown("""
#     <div style="background: linear-gradient(135deg, #312e81, #4f46e5); padding: 35px; border-radius: 22px; margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.15);">

#     <h1 style="color: white; margin: 0 0 10px 0;">
#     💰 Finance Analytics
#     </h1>

#     <h3 style="color: #e0e7ff; margin: 0 0 12px 0;">
#     Smart Personal Finance Management
#     </h3>

#     <p style="color: #c7d2fe; font-size: 16px; margin-bottom: 20px;">
#     Track your money • Understand your spending • Make smarter financial decisions
#     </p>

#     <div style="display: inline-block; background: rgba(255,255,255,0.15); padding: 9px 16px; border-radius: 20px; color: white; font-size: 14px;">
#     ✨ Smart Finance Dashboard
#     </div>

#     </div>
#     """, unsafe_allow_html=True)

#     # =====================================================
#     # WELCOME
#     # =====================================================

#     st.header("👋 Welcome!")

#     st.write(
#         "Manage your personal finances in one place. "
#         "Track income and expenses, analyze spending habits, "
#         "monitor your financial health, and get useful "
#         "financial insights."
#     )


#     # =====================================================
#     # WHAT YOU CAN DO
#     # =====================================================

#     st.divider()

#     st.header("✨ What You Can Do")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         with st.container(border=True):
#             st.markdown("## 💰 Track Income")
#             st.write(
#                 "Record your salary, business income, "
#                 "freelancing, investments and other "
#                 "sources of income."
#             )

#     with col2:
#         with st.container(border=True):
#             st.markdown("## 💸 Track Expenses")
#             st.write(
#                 "Record your daily expenses and organize "
#                 "them into categories such as food, "
#                 "travel, bills and shopping."
#             )

#     with col3:
#         with st.container(border=True):
#             st.markdown("## 📊 Analyze Finances")
#             st.write(
#                 "Understand your spending patterns, "
#                 "savings rate, financial health and "
#                 "overall financial performance."
#             )


#     # =====================================================
#     # AI INSIGHTS
#     # =====================================================

#     st.divider()

#     st.header("🤖 Intelligent Financial Insights")

#     st.write(
#         "Use your financial data to understand your "
#         "spending behavior and make better decisions."
#     )

#     col1, col2 = st.columns(2)

#     with col1:
#         with st.container(border=True):
#             st.markdown("## 📈 Financial Analysis")

#             st.write("• View income and expenses")
#             st.write("• Monitor your balance")
#             st.write("• Analyze spending categories")
#             st.write("• Check your financial health")

#     with col2:
#         with st.container(border=True):
#             st.markdown("## 💡 Smart Suggestions")

#             st.write("• Understand spending trends")
#             st.write("• Get financial suggestions")
#             st.write("• Monitor your budget")
#             st.write("• Predict future expenses")


#     # =====================================================
#     # GET STARTED
#     # =====================================================

#     st.divider()

#     st.header("🚀 Get Started")

#     st.write(
#         "Use the sidebar to explore the features "
#         "of your Finance Analytics application."
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         with st.container(border=True):
#             st.markdown("## ➕ Add Income")
#             st.write("Record your income.")

#     with col2:
#         with st.container(border=True):
#             st.markdown("## 💸 Add Expense")
#             st.write("Track your spending.")

#     with col3:
#         with st.container(border=True):
#             st.markdown("## 📊 Dashboard")
#             st.write("Analyze your finances.")


#     # =====================================================
#     # FOOTER
#     # =====================================================

#     st.divider()

#     st.caption(
#         "💰 Finance Analytics • Track • Analyze • Improve"
#     )





import streamlit as st


# =====================================================
# HOME PAGE - MODERN DESIGN
# =====================================================

def show_home():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.html("""
    <style>

    .finance-hero {
        padding: 42px;
        border-radius: 24px;
        margin-bottom: 30px;

        background:
            radial-gradient(
                circle at 90% 20%,
                rgba(37, 99, 235, 0.30),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #17152e,
                #25205a,
                #111827
            );

        border: 1px solid rgba(255,255,255,0.12);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.35);
    }

    .finance-hero-icon {
        font-size: 46px;
        margin-bottom: 8px;
    }

    .finance-hero-title {
        font-size: 42px;
        font-weight: 750;
        color: white;
        margin-bottom: 8px;
    }

    .finance-hero-subtitle {
        font-size: 21px;
        font-weight: 600;
        color: #c7d2fe;
        margin-bottom: 12px;
    }

    .finance-hero-text {
        font-size: 15px;
        color: #a5b4fc;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    .finance-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 25px;

        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);

        color: #e0e7ff;
        font-size: 13px;
    }

    </style>

    <div class="finance-hero">

        <div class="finance-hero-icon">💰</div>

        <div class="finance-hero-title">
            Finance Analytics
        </div>

        <div class="finance-hero-subtitle">
            Smart Personal Finance Management
        </div>

        <div class="finance-hero-text">
            Track your money • Understand your spending •
            Make smarter financial decisions
        </div>

        <div class="finance-badge">
            ✨ Smart Finance Dashboard
        </div>

    </div>
    """)


    # =====================================================
    # WELCOME
    # =====================================================

    st.html("""
    <style>

    .welcome-title {
        font-size: 30px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #a1a1aa;
        font-size: 15px;
        line-height: 1.7;
    }

    </style>

    <div class="welcome-title">
        👋 Welcome!
    </div>

    <div class="welcome-text">
        Manage your personal finances in one place.
        Track income and expenses, analyze spending habits,
        monitor your financial health, and get useful
        financial insights.
    </div>
    """)


    st.divider()


    # =====================================================
    # WHAT YOU CAN DO
    # =====================================================

    st.html("""
    <style>

    .section-title {
        font-size: 30px;
        font-weight: 700;
        color: white;
        margin-bottom: 7px;
    }

    .section-text {
        color: #a1a1aa;
        font-size: 15px;
        margin-bottom: 20px;
    }

    </style>

    <div class="section-title">
        ✨ What You Can Do
    </div>

    <div class="section-text">
        Everything you need to understand and manage your money.
    </div>
    """)


    col1, col2, col3 = st.columns(3)


    # =====================================================
    # INCOME CARD
    # =====================================================

    with col1:

        st.html("""
        <style>

        .income-card {
            min-height: 220px;
            padding: 28px;
            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(22,45,38,0.95),
                    rgba(17,24,39,0.98)
                );

            border: 1px solid rgba(34,197,94,0.22);

            box-shadow:
                0 10px 30px rgba(0,0,0,0.25);

            transition: 0.25s ease;
        }

        .income-card:hover {
            transform: translateY(-7px);
            box-shadow:
                0 18px 40px rgba(0,0,0,0.40);
        }

        .income-icon {
            font-size: 35px;
            margin-bottom: 18px;
        }

        .income-title {
            color: white;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .income-text {
            color: #aeb4c3;
            font-size: 14px;
            line-height: 1.7;
        }

        </style>

        <div class="income-card">

            <div class="income-icon">💰</div>

            <div class="income-title">
                Track Income
            </div>

            <div class="income-text">
                Record your salary, business income,
                freelancing, investments and other
                sources of income.
            </div>

        </div>
        """)


    # =====================================================
    # EXPENSE CARD
    # =====================================================

    with col2:

        st.html("""
        <style>

        .expense-card {
            min-height: 220px;
            padding: 28px;
            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(55,28,35,0.95),
                    rgba(17,24,39,0.98)
                );

            border: 1px solid rgba(239,68,68,0.22);

            box-shadow:
                0 10px 30px rgba(0,0,0,0.25);

            transition: 0.25s ease;
        }

        .expense-card:hover {
            transform: translateY(-7px);
            box-shadow:
                0 18px 40px rgba(0,0,0,0.40);
        }

        .expense-icon {
            font-size: 35px;
            margin-bottom: 18px;
        }

        .expense-title {
            color: white;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .expense-text {
            color: #aeb4c3;
            font-size: 14px;
            line-height: 1.7;
        }

        </style>

        <div class="expense-card">

            <div class="expense-icon">💸</div>

            <div class="expense-title">
                Track Expenses
            </div>

            <div class="expense-text">
                Record your daily expenses and organize
                them into categories such as food,
                travel, bills and shopping.
            </div>

        </div>
        """)


    # =====================================================
    # ANALYSIS CARD
    # =====================================================

    with col3:

        st.html("""
        <style>

        .analysis-card {
            min-height: 220px;
            padding: 28px;
            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(25,40,65,0.95),
                    rgba(17,24,39,0.98)
                );

            border: 1px solid rgba(59,130,246,0.25);

            box-shadow:
                0 10px 30px rgba(0,0,0,0.25);

            transition: 0.25s ease;
        }

        .analysis-card:hover {
            transform: translateY(-7px);
            box-shadow:
                0 18px 40px rgba(0,0,0,0.40);
        }

        .analysis-icon {
            font-size: 35px;
            margin-bottom: 18px;
        }

        .analysis-title {
            color: white;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .analysis-text {
            color: #aeb4c3;
            font-size: 14px;
            line-height: 1.7;
        }

        </style>

        <div class="analysis-card">

            <div class="analysis-icon">📊</div>

            <div class="analysis-title">
                Analyze Finances
            </div>

            <div class="analysis-text">
                Understand your spending patterns,
                savings rate, financial health and
                overall financial performance.
            </div>

        </div>
        """)


    # =====================================================
    # INTELLIGENT INSIGHTS
    # =====================================================

    st.divider()

    st.html("""
    <div class="section-title">
        🤖 Intelligent Financial Insights
    </div>

    <div class="section-text">
        Use your financial data to understand your
        spending behavior and make better decisions.
    </div>
    """)


    col1, col2 = st.columns(2)


    # =====================================================
    # FINANCIAL ANALYSIS
    # =====================================================

    with col1:

        st.html("""
        <style>

        .insight-card {
            min-height: 250px;
            padding: 28px;
            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(38,30,65,0.95),
                    rgba(17,24,39,0.98)
                );

            border: 1px solid rgba(168,85,247,0.22);

            box-shadow:
                0 10px 30px rgba(0,0,0,0.25);

            transition: 0.25s ease;
        }

        .insight-card:hover {
            transform: translateY(-7px);
            box-shadow:
                0 18px 40px rgba(0,0,0,0.40);
        }

        .insight-icon {
            font-size: 35px;
            margin-bottom: 18px;
        }

        .insight-title {
            color: white;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 15px;
        }

        .insight-item {
            color: #b5bac7;
            font-size: 14px;
            margin-bottom: 11px;
        }

        </style>

        <div class="insight-card">

            <div class="insight-icon">📈</div>

            <div class="insight-title">
                Financial Analysis
            </div>

            <div class="insight-item">
                • View income and expenses
            </div>

            <div class="insight-item">
                • Monitor your balance
            </div>

            <div class="insight-item">
                • Analyze spending categories
            </div>

            <div class="insight-item">
                • Check your financial health
            </div>

        </div>
        """)


    # =====================================================
    # SMART SUGGESTIONS
    # =====================================================

    with col2:

        st.html("""
        <div class="insight-card">

            <div class="insight-icon">💡</div>

            <div class="insight-title">
                Smart Suggestions
            </div>

            <div class="insight-item">
                • Understand spending trends
            </div>

            <div class="insight-item">
                • Get financial suggestions
            </div>

            <div class="insight-item">
                • Monitor your budget
            </div>

            <div class="insight-item">
                • Predict future expenses
            </div>

        </div>
        """)


    # =====================================================
    # GET STARTED
    # =====================================================

    st.divider()

    st.html("""
    <div class="section-title">
        🚀 Get Started
    </div>

    <div class="section-text">
        Use the sidebar to explore the features
        of your Finance Analytics application.
    </div>
    """)


    col1, col2, col3 = st.columns(3)


    # =====================================================
    # START CARD 1
    # =====================================================

    with col1:

        st.html("""
        <style>

        .start-card {
            padding: 24px;
            min-height: 145px;
            border-radius: 18px;

            background:
                rgba(25,29,43,0.95);

            border: 1px solid rgba(255,255,255,0.10);

            transition: 0.25s ease;
        }

        .start-card:hover {
            transform: translateY(-6px);
            border-color: rgba(99,102,241,0.40);
        }

        .start-icon {
            font-size: 32px;
            margin-bottom: 12px;
        }

        .start-title {
            color: white;
            font-size: 19px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .start-text {
            color: #9ca3af;
            font-size: 14px;
        }

        </style>

        <div class="start-card">

            <div class="start-icon">
                ➕
            </div>

            <div class="start-title">
                Add Income
            </div>

            <div class="start-text">
                Record your income.
            </div>

        </div>
        """)


    # =====================================================
    # START CARD 2
    # =====================================================

    with col2:

        st.html("""
        <div class="start-card">

            <div class="start-icon">
                💸
            </div>

            <div class="start-title">
                Add Expense
            </div>

            <div class="start-text">
                Track your spending.
            </div>

        </div>
        """)


    # =====================================================
    # START CARD 3
    # =====================================================

    with col3:

        st.html("""
        <div class="start-card">

            <div class="start-icon">
                📊
            </div>

            <div class="start-title">
                Dashboard
            </div>

            <div class="start-text">
                Analyze your finances.
            </div>

        </div>
        """)


    # =====================================================
    # FOOTER
    # =====================================================

    st.divider()

    st.html("""
    <div style="
        text-align:center;
        color:#71717a;
        font-size:13px;
        padding:8px 0 20px;
    ">
        💰 Finance Analytics • Track • Analyze • Improve
    </div>
    """)