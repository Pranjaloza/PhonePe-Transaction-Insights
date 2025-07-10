import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector
from PIL import Image
import json
import requests
# from llama_cpp import Llama

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PhonePe Transaction Insights Dashboard",
    layout="wide",
    page_icon="📲"
)

# --- CUSTOM LIGHT MODE STYLING WITH MOBILE RESPONSIVE TWEAK ---
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: #f5f0ff;
        color: #1e1e1e;
    }
    [data-testid="stSidebar"] {
        background-color: #ede7f6;
        padding: 2rem 1rem;
    }
    h1, h2, h3, h4, h5, h6, p, label, .stSelectbox, .stTextInput {
        color: #4A148C;
    }
    .stButton>button {
        background-color: #f5f0ff;
        color: #4A148C;
        font-weight: bold;
        border: none;
        border-bottom: 3px solid transparent;
        border-radius: 0;
        width: 180px;
        padding: 0.6rem 1rem;
        white-space: nowrap;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        border-bottom: 3px solid #7B1FA2;
        color: #311B92;
        cursor: pointer;
        transform: scale(1.05);
    }
    .block-container {
        padding: 1.0rem 2rem;
    }
    .kpi-card {
        background-color: #ede7f6;
        padding: 1.2rem;
        border-radius: 0.75rem;
        text-align: center;
        font-size: 1.6rem;
        color: #4A148C;
        font-weight: bold;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
    }
    .kpi-card:hover {
        transform: scale(1.03);
    }
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #4A148C;
        transition: all 0.3s ease-in-out;
    }
    .summary-text {
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        background-color: #f3e5f5;
        border-radius: 0.5rem;
        margin-top: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    
    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 2rem;
        color: #4A148C;
    }
    @media only screen and (max-width: 768px) {
        .kpi-card {
            font-size: 1.2rem !important;
            padding: 1rem !important;
        }
        .stButton>button {
            width: 100% !important;
            padding: 0.5rem;
            font-size: 0.9rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.title("📈 PhonePe Transaction Insights Dashboard")

# --- DATABASE CONNECTION ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2004",
        database="phonepe"
    )

conn = get_connection()
cursor = conn.cursor()

# --- TABS SETUP ---
tab_titles = [
    "ℹ️ About PhonePe", 
    "📈 Transaction Dynamics",
    "📱 Device Brand Engagement",
    "🌐 State-Level User Engagement",
    "🧾 Registration Analysis",
    "🏆 Top Performing Locations",
    "📌 Case Study Summary"
]


# # --- SIDEBAR LOGO ---
# with st.sidebar:
#     col_logo, col_text = st.columns([1, 2])
#     with col_logo:
#         st.image("phonepe_logo.png", width=60)
#     with col_text:
#         st.markdown("""<h3 style='color: #4A148C; margin: 0;'>PhonePe</h3>""", unsafe_allow_html=True)


        
if "active_tab" not in st.session_state:
    st.session_state.active_tab = tab_titles[0]

with st.expander("🔍 Choose Section", expanded=False):
    selected_tab = st.selectbox("Select Section", tab_titles, index=tab_titles.index(st.session_state.active_tab))
    st.session_state.active_tab = selected_tab

# --- COLOR PALETTE ---
custom_palette = px.colors.sequential.Viridis

# --- SIDEBAR FILTERS ---
with st.sidebar:
    #st.markdown("{st.session_state.active_tab}")
    filter_container = st.container()

# --- MAIN AREA CONTENT --- 
with st.container():
    if st.session_state.active_tab == "ℹ️ About PhonePe":
        with st.sidebar:
            st.markdown("""
            <div style="margin-bottom: 120px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("""
                <div style='margin-top: 0px;'>
                    👋 <b>Hello!<br>Welcome to the dashboard</b>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""<div class='section-title' align='center'>About PhonePe</div>""", unsafe_allow_html=True)
        
        st.markdown("""
        <h3 style='margin-bottom:0; text-align:center;'>India’s Trusted Digital Payment Powerhouse</h3>
        <p style='font-size:1rem;'>
        Launched in 2016, <b>PhonePe</b> is India’s top fintech platform facilitating secure and seamless UPI payments, recharges, bill payments, insurance, and investment services — all within one app.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # KPI CARDS
        k1, k2, k3, k4 = st.columns(4)
        k1.markdown("### 👥 Users")
        k1.markdown("<div class='kpi-card'>400M+</div>", unsafe_allow_html=True)

        k2.markdown("### 🏪 Merchants")
        k2.markdown("<div class='kpi-card'>20M+</div>", unsafe_allow_html=True)

        k3.markdown("### 🌍 Languages")
        k3.markdown("<div class='kpi-card'>11+</div>", unsafe_allow_html=True)

        k4.markdown("### 💳 Transactions")
        k4.markdown("<div class='kpi-card'>Billions / month</div>", unsafe_allow_html=True)

        st.markdown("---")

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("""
            ### 🔧 Core Services
            - ✅ UPI Payments & Transfers  
            - 📲 Mobile & DTH Recharges  
            - 💡 Utility Bill Payments  
            - 🛡️ Insurance & Mutual Funds  
            - 🏪 QR Code Merchant Payments
            """)

        with col4:
            st.markdown("""
            ### 🎯 Why This Dashboard?
            - Track real-time transaction growth  
            - Understand state-wise user patterns  
            - Gain regional business intelligence  
            - Visualize trends & peak activity  
            """)

        st.markdown("""
        ---
        <div class='summary-text'>
        📊 <b>This dashboard</b> provides interactive insights into PhonePe's platform performance, regional engagement, and usage patterns.<br>
        Built as a data visualization and business analysis case study using real-world PhonePe Pulse data.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        ---
        🔗 <a href='https://www.phonepe.com' target='_blank'>Official Website</a>  
        📱 <a href='https://play.google.com/store/apps/details?id=com.phonepe.app' target='_blank'>Get the App on Play Store</a>
        """, unsafe_allow_html=True)


    elif st.session_state.active_tab == tab_titles[1]:   
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-bottom: -80px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)

            # --- Filter container ---
            st.markdown(f"## Filters : 📈 Transaction Dynamics")
            cursor.execute("SELECT DISTINCT state FROM aggregated_transaction")
            states = sorted([row[0] for row in cursor.fetchall()])
            selected_state = st.selectbox("Select State", states, key='state_tx')

            cursor.execute(f"SELECT DISTINCT year FROM aggregated_transaction WHERE state='{selected_state}'")
            years = sorted([row[0] for row in cursor.fetchall()])
            selected_year = st.selectbox("Select Year", years, key='year_tx')

            cursor.execute(f"SELECT DISTINCT quarter FROM aggregated_transaction WHERE state='{selected_state}' AND year={selected_year}")
            quarters = sorted([row[0] for row in cursor.fetchall()])
            selected_quarter = st.selectbox("Select Quarter", quarters, key='quarter_tx')
            
        st.markdown("""<div class='section-title'>Transaction Dynamics</div>""", unsafe_allow_html=True)
        query = f"""
            SELECT transaction_type, SUM(count) as count, SUM(amount) as amount
            FROM aggregated_transaction
            WHERE state='{selected_state}' AND year={selected_year} AND quarter={selected_quarter}
            GROUP BY transaction_type
        """
        df_txn = pd.read_sql(query, conn)

        if not df_txn.empty:
            total_txns = df_txn['count'].sum()
            total_amount = df_txn['amount'].sum()

            kpi1, kpi2 = st.columns(2)
            kpi1.markdown("### 🔄 Total Transactions")
            kpi1.markdown(f"<div class='kpi-card'>{total_txns:,}</div>", unsafe_allow_html=True)

            kpi2.markdown("### 💰 Total Amount (INR)")
            kpi2.markdown(f"<div class='kpi-card'>₹ {total_amount:,.2f}</div>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            col1.plotly_chart(px.bar(df_txn, x="transaction_type", y="count", title="Total Transactions by Type", color_discrete_sequence=custom_palette), use_container_width=True)
            col2.plotly_chart(px.pie(df_txn, names="transaction_type", values="amount", title="Transaction Amount Share", color_discrete_sequence=custom_palette), use_container_width=True)

            top_txn = df_txn.sort_values(by='count', ascending=False).iloc[0]
            top_amt = df_txn.sort_values(by='amount', ascending=False).iloc[0]
            st.markdown("""
            <div class='summary-text'>
            📌 Summary Insights:<br>
            - Most frequent transaction type: <b>{}</b> with <b>{:,}</b> transactions.<br>
            - Highest value transaction type: <b>{}</b> with <b>₹ {:,.2f}</b>.
            </div>
            """.format(top_txn['transaction_type'], int(top_txn['count']), top_amt['transaction_type'], float(top_amt['amount'])), unsafe_allow_html=True)

    elif st.session_state.active_tab == tab_titles[2]:
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-bottom: -80px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(f"## Filters :📱 Device Brand Engagement")
            cursor.execute("SELECT DISTINCT brand FROM aggregated_user")
            brands = sorted([row[0] for row in cursor.fetchall() if row[0] != 'NULL'])
            selected_brand = st.selectbox("Select Device Brand", brands, key='brand_device')


            cursor.execute(f"SELECT DISTINCT state FROM aggregated_user WHERE brand='{selected_brand}'")
            states = sorted([row[0] for row in cursor.fetchall()])
            selected_state = st.selectbox("Select State", states, key='state_device')

            cursor.execute(f"SELECT DISTINCT year FROM aggregated_user WHERE brand='{selected_brand}' AND state='{selected_state}'")
            years = sorted([row[0] for row in cursor.fetchall()])
            selected_year = st.selectbox("Select Year", years, key='year_device')

        st.markdown("""<div class='section-title'>Device Brand Engagement</div>""", unsafe_allow_html=True)
        query = f"""
            SELECT quarter, SUM(count) as user_count
            FROM aggregated_user
            WHERE brand='{selected_brand}' AND state='{selected_state}' AND year={selected_year}
            GROUP BY quarter
        """
        df_brand = pd.read_sql(query, conn)

        if not df_brand.empty:
            st.plotly_chart(px.bar(df_brand, x="quarter", y="user_count", title="User Count by Quarter", color_discrete_sequence=custom_palette), use_container_width=True)
            total_users = df_brand['user_count'].sum()
            st.markdown(f"""
            <div class='summary-text'>
            📌 Summary Insight:<br>
            - <b>{selected_brand}</b> users in <b>{selected_state}</b> during <b>{selected_year}</b> totalled <b>{total_users:,}</b> app registrations across all quarters.
            </div>
            """, unsafe_allow_html=True)

    elif st.session_state.active_tab == tab_titles[3]:
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-bottom: -80px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"## Filters : 🌐 State-Level User Engagement")
            cursor.execute("SELECT DISTINCT year FROM aggregated_user")
            years = sorted([row[0] for row in cursor.fetchall()])
            selected_year = st.selectbox("Select Year", years, key='year_user')

            cursor.execute(f"SELECT DISTINCT quarter FROM aggregated_user WHERE year={selected_year}")
            quarters = sorted([row[0] for row in cursor.fetchall()])
            selected_quarter = st.selectbox("Select Quarter", quarters, key='quarter_user')

        st.markdown("""<div class='section-title'>State-Level User Engagement</div>""", unsafe_allow_html=True)
        query = f"""
            SELECT state, SUM(count) as user_count
            FROM aggregated_user
            WHERE year={selected_year} AND quarter={selected_quarter}
            GROUP BY state
            ORDER BY user_count DESC
        """
        df_state_user = pd.read_sql(query, conn)

        if not df_state_user.empty:
            col1, col2 = st.columns(2)
            col1.plotly_chart(px.bar(df_state_user, x="state", y="user_count", title="User Engagement by State", color_discrete_sequence=custom_palette), use_container_width=True)
            col2.plotly_chart(px.pie(df_state_user, names="state", values="user_count", title="User Share by State", color_discrete_sequence=custom_palette), use_container_width=True)

            top_state = df_state_user.iloc[0]
            st.markdown("""
            <div class='summary-text'>
            📌 Summary Insight:<br>
            - Top state in user engagement: <b>{}</b> with <b>{:,}</b> users.
            </div>
            """.format(top_state['state'], int(top_state['user_count'])), unsafe_allow_html=True)

            # Load GeoJSON for Indian states
                # Load GeoJSON from local file
            import json
            with open("india_state.geojson", "r", encoding="utf-8") as f:
                india_geo = json.load(f)

            st.markdown("""<div class='section-title'>🗺️ Choropleth Map: State Engagement</div>""", unsafe_allow_html=True)
            with st.spinner("Loading chart..."):
                df_state_user['state'] = df_state_user['state'].str.title().str.strip()

                fig_choropleth = px.choropleth(
                    df_state_user,
                    geojson=india_geo,
                    locations="state",
                    featureidkey="properties.NAME_1",  # ensure GeoJSON has state names under this key
                    color="user_count",
                    color_continuous_scale=custom_palette,
                    hover_data={"user_count": True},
                    labels={"user_count": "Users"},
                    projection="natural earth",
                    title=f"User Engagement Across States — {selected_year} Q{selected_quarter}"
                )

                fig_choropleth.update_geos(fitbounds="locations", visible=False)
                #fig_choropleth.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
                st.plotly_chart(fig_choropleth, use_container_width=True)
                st.markdown(f"""
                <div class='summary-text'>
                <br>
                - <b>Choropleth showing user count per state for Year </b> <b>{selected_year}</b> during Q <b>{selected_quarter}</b> 
                </div>
                """, unsafe_allow_html=True)
    elif st.session_state.active_tab == tab_titles[4]:
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-bottom: -80px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"## Filters : 🧾 Registration Analysis")
            cursor.execute("SELECT DISTINCT state FROM map_user")
            reg_states = sorted([row[0] for row in cursor.fetchall()])
            selected_reg_state = st.selectbox("Select State", reg_states, key='reg_state')

            cursor.execute(f"SELECT DISTINCT year FROM map_user WHERE state='{selected_reg_state}'")
            reg_years = sorted([row[0] for row in cursor.fetchall()])
            selected_reg_year = st.selectbox("Select Year", reg_years, key='reg_year')

            cursor.execute(f"SELECT DISTINCT quarter FROM map_user WHERE state='{selected_reg_state}' AND year={selected_reg_year}")
            reg_quarters = sorted([row[0] for row in cursor.fetchall()])
            selected_reg_quarter = st.selectbox("Select Quarter", reg_quarters, key='reg_quarter')

        st.markdown("""<div class='section-title'>User Registration Analysis</div>""", unsafe_allow_html=True)

        query = f"""
            SELECT SUM(registered_users) as total_users, SUM(app_opens) as total_opens
            FROM map_user
            WHERE state='{selected_reg_state}' AND year={selected_reg_year} AND quarter={selected_reg_quarter}
        """
        df_reg = pd.read_sql(query, conn)

        if not df_reg.empty:
            kpi1, kpi2 = st.columns(2)
            kpi1.markdown("### 👥 Registered Users")
            kpi1.markdown(f"<div class='kpi-card'>{df_reg['total_users'].values[0]:,}</div>", unsafe_allow_html=True)

            kpi2.markdown("### 📱 App Opens")
            kpi2.markdown(f"<div class='kpi-card'>{df_reg['total_opens'].values[0]:,}</div>", unsafe_allow_html=True)

        # Add time series charts for historical trends
        query_trend = f"""
            SELECT year, quarter, SUM(registered_users) as total_users, SUM(app_opens) as total_opens
            FROM map_user
            WHERE state='{selected_reg_state}'
            GROUP BY year, quarter
            ORDER BY year, quarter
        """
        df_trend = pd.read_sql(query_trend, conn)

        if not df_trend.empty:
            col1, col2 = st.columns(2)
            col1.plotly_chart(px.line(df_trend, x='quarter', y='total_users', color='year', markers=True, title="Registered Users Over Time", color_discrete_sequence=custom_palette), use_container_width=True)
            col2.plotly_chart(px.line(df_trend, x='quarter', y='total_opens', color='year', markers=True, title="App Opens Over Time", color_discrete_sequence=custom_palette), use_container_width=True)

            latest = df_trend.sort_values(['year', 'quarter'], ascending=False).iloc[0]
            st.markdown("""
            <div class='summary-text'>
            📌 Summary Insight:<br>
            - Latest quarter data (<b>Year {} - Q{}</b>) shows <b>{:,}</b> registered users and <b>{:,}</b> app opens.
            </div>
            """.format(latest['year'], latest['quarter'], int(latest['total_users']), int(latest['total_opens'])), unsafe_allow_html=True)
        

    elif st.session_state.active_tab == tab_titles[5]:
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-bottom: -80px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"## Filters : 🏆 Top Performing Locations")
            cursor.execute("SELECT DISTINCT year FROM aggregated_user")
            years = sorted([row[0] for row in cursor.fetchall()])
            selected_year = st.selectbox("Select Year", years, key='year_device')

        st.markdown("""<div class='section-title'>Top Performing Locations</div>""", unsafe_allow_html=True)

        query_top_states = f"""
        SELECT state, SUM(amount) as total_amount
        FROM aggregated_transaction 
        WHERE year = {selected_year}
        GROUP BY state, year
        ORDER BY total_amount DESC
        LIMIT 10
        """
        df_top_states = pd.read_sql(query_top_states, conn)

        query_top_districts = f"""
        SELECT district, SUM(amount) as total_amount
        FROM map_map
        WHERE year = {selected_year}
        GROUP BY district, year
        ORDER BY total_amount DESC
        LIMIT 10
        """
        df_top_districts = pd.read_sql(query_top_districts, conn)

        if not df_top_states.empty and not df_top_districts.empty:
            col1, col2 = st.columns(2)
            col1.plotly_chart(px.bar(df_top_states, x="state", y="total_amount", title="Top 10 States by Transaction Amount", color_discrete_sequence=custom_palette), use_container_width=True)
            col2.plotly_chart(px.bar(df_top_districts, x="district", y="total_amount", title="Top 10 Districts by Transaction Amount", color_discrete_sequence=custom_palette), use_container_width=True)

            top_state = df_top_states.iloc[0]
            top_district = df_top_districts.iloc[0]
            st.markdown(f"""
            <div class='summary-text'>
            📌 Summary Insight:<br>
            - <b>{top_state['state']}</b> leads all states with <b>₹ {top_state['total_amount']:,.2f}</b> in transactions.<br>
            - <b>{top_district['district']}</b> is the top district, contributing <b>₹ {top_district['total_amount']:,.2f}</b>.
            </div>
            """, unsafe_allow_html=True)


    elif st.session_state.active_tab == "📌 Case Study Summary":
        with st.sidebar:
            # --- Logo at the top ---
        
            st.markdown("""
            <div style="margin-top: 150px;">
                """, unsafe_allow_html=True)
            st.image("PhonePe-Logo.wine.png", width=220)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("""<div class='section-title'>📌 Case Study Summary</div>""", unsafe_allow_html=True)

        # Fetch top states
        df_states = pd.read_sql("SELECT state, SUM(amount) AS total_amount FROM aggregated_transaction GROUP BY state ORDER BY total_amount DESC LIMIT 3", conn)

        # Fetch top brands
        df_brands = pd.read_sql("SELECT brand, SUM(count) AS user_count FROM aggregated_user WHERE brand != 'NULL' GROUP BY brand ORDER BY user_count DESC LIMIT 3", conn)

        # Fetch peak quarter
        df_quarter = pd.read_sql("SELECT year, quarter, SUM(count) AS txn_count FROM aggregated_transaction GROUP BY year, quarter ORDER BY txn_count DESC LIMIT 1", conn)

        # Dynamic Summary
        top_states = ', '.join(df_states['state'].tolist())
        top_brands = ', '.join(df_brands['brand'].tolist())
        top_year = df_quarter.iloc[0]['year']
        top_quarter = df_quarter.iloc[0]['quarter']

        st.markdown(f"""
        ### 🧠 Key Findings
        - States like {top_states} lead in transaction volumes and values.
        - Device brands like {top_brands} dominate app registrations in key markets.
        - Q{top_quarter} {top_year} witnessed the highest transaction activity.

        ### 💼 Business Impact
        - High-value states can be prioritized for merchant onboarding.
        - Districts with lower transaction rates may be targeted for promotions or awareness campaigns.
        - Popular device brands suggest potential partners for bundled offers or advertisements.

        ### 📈 Recommended Actions
        - Expand user acquisition strategies in underperforming states.
        - Leverage Q{top_quarter} trends for nationwide campaigns.
        - Optimize app performance on top brands like {top_brands}.
        - Continue monitoring district-level trends for micro-targeting.
        """, unsafe_allow_html=True)

        st.markdown("### 📊 Visual Insights")

        fig_state = px.bar(
            df_states,
            x='state',
            y='total_amount',
            title='Top 3 States by Transaction Amount',
            color='state',
            text_auto='.2s',
            color_discrete_sequence=custom_palette
        )
        st.plotly_chart(fig_state, use_container_width=True)

        fig_brand = px.pie(
            df_brands,
            names='brand',
            values='user_count',
            title='Top 3 Device Brands by User Registrations',
            color_discrete_sequence=custom_palette
        )
        st.plotly_chart(fig_brand, use_container_width=True)

        df_trend = pd.read_sql("""
            SELECT year, quarter, SUM(count) AS txn_count
            FROM aggregated_transaction
            GROUP BY year, quarter
            ORDER BY year, quarter
        """, conn)
        df_trend['Quarter'] = df_trend['year'].astype(str) + '-Q' + df_trend['quarter'].astype(str)
        fig_trend = px.line(
            df_trend,
            x='Quarter',
            y='txn_count',
            title='Quarterly Transaction Volume Trend',
            markers=True,
            color_discrete_sequence=custom_palette
        )
        st.plotly_chart(fig_trend, use_container_width=True)

# --- FOOTER ---
st.markdown("""
---
<div class='footer'>
📧 Created by <a href='mailto:pranjaloza7@gmail.com'>Pranjal Oza</a> | 📅 Updated: July 2025
</div>
""", unsafe_allow_html=True)