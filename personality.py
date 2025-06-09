import streamlit as st
import pandas as pd
import plotly.express as px

# Browser tab title
st.set_page_config(page_title="Personality Data Dashboard", layout="wide")

# Load data
GITHUB_CSV_URL = "https://raw.githubusercontent.com/ibtysxmslhx/mini-project/main/cleaned_personality_dataset.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(GITHUB_CSV_URL)

# Sidebar – Navigation only (always visible)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/ibtysxmslhx/mini-project/main/LL.jpg")
    st.title("🎯 Insight Menu")
    page = st.radio("🧭 Select View", ["Dashboard", "Full Dataset Preview"])

# 🏠 DASHBOARD PAGE
if page == "Dashboard":
    # Header image and title
    st.image("https://raw.githubusercontent.com/ibtysxmslhx/mini-project/main/LL.jpg")
    st.title("🎭 Personality Data Dashboard")

    # Filters – only shown on Dashboard
    with st.sidebar:
        st.header("🔍 Filter the data")
        personalities = df["Personality"].unique()
        selected_personalities = st.multiselect("Select Personality Type", options=personalities, default=personalities)

        stage_fear_options = df["Stage_fear"].unique()
        selected_stage_fear = st.selectbox("Stage Fear", options=["All"] + list(stage_fear_options))

        drained_options = df["Drained_after_socializing"].unique()
        selected_drained = st.selectbox("Drained After Socializing", options=["All"] + list(drained_options))

    # Apply filters
    filtered_df = df[(df["Personality"].isin(selected_personalities)) ]
    if selected_stage_fear != "All":
        filtered_df = filtered_df[filtered_df["Stage_fear"] == selected_stage_fear]
    if selected_drained != "All":
        filtered_df = filtered_df[filtered_df["Drained_after_socializing"] == selected_drained]

    # KPI Section
    st.markdown("### 📌 Key Insights")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🕒 Avg Time Alone", f"{df['Time_spent_Alone'].mean():.2f} hrs")
    with col2:
        st.metric("📱 Avg Post Frequency", f"{df['Post_frequency'].mean():.2f}")
    with col3:
        st.metric("👥 Avg Friends Circle", f"{df['Friends_circle_size'].mean():.1f}")
    with col4:
        st.metric("🎭 Most Common Personality", df["Personality"].mode()[0])

    # Graph Section
    st.markdown("---")
    st.markdown("### 📈 Visual Analysis")
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        fig1 = px.bar(df.groupby("Personality")["Time_spent_Alone"].mean().reset_index(),
                      x="Personality", y="Time_spent_Alone", color="Personality",
                      title="Average Time Spent Alone by Personality",
                      labels={"Time_spent_Alone": "Hours"}, color_discrete_sequence=["#CDAF9C", "#34464D"])
        st.plotly_chart(fig1, use_container_width=True)

    with row1_col2:
        fig2 = px.histogram(df, x="Friends_circle_size", color="Personality", nbins=15, barmode="overlay",
                            title="Distribution of Friends Circle Size", color_discrete_sequence=["#98ABA1", "#CFC5B0"])
        st.plotly_chart(fig2, use_container_width=True)

    row2_col1, row2_col2 = st.columns(2)
    
    with row2_col1:
     fig3 = px.violin(df, x="Personality", y="Post_frequency", color="Personality",
                 box=True, points="all",  # box inside violin + show points
                 color_discrete_sequence=["#CDAF9C", "#34464D"],
                 title="Post Frequency by Personality Type")

st.plotly_chart(fig3, use_container_width=True)

    with row2_col2:
        fig4 = px.histogram(df, x="Stage_fear", color="Personality", barmode="group",
                            title="Stage Fear Count by Personality", color_discrete_sequence=["#424A45", "#CFC5B0"])
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("### 😩 Social Energy Levels")
    fig5 = px.histogram(df, x="Drained_after_socializing", color="Personality", barmode="group",
                        title="Feeling Drained After Socializing", color_discrete_sequence=["#CDAF9C", "#34464D"])
    st.plotly_chart(fig5, use_container_width=True)

# 📄 FULL DATASET PREVIEW PAGE
elif page == "Full Dataset Preview":
    st.image("https://raw.githubusercontent.com/ibtysxmslhx/mini-project/main/LL.jpg")
    st.title("🗃️ Full Dataset Preview")
    st.dataframe(df, use_container_width=True)
