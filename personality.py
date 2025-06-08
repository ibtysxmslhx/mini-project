import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Personality Data Dashboard")

# 🔗 GitHub CSV file (make sure it's RAW link)
GITHUB_CSV_URL = "https://raw.githubusercontent.com/ibtysxmslhx/mini-project/main/cleaned_personality_dataset.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

# Sidebar
with st.sidebar:
    st.header("🔧 Configuration")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Load data
df = load_data(uploaded_file) if uploaded_file else load_data(GITHUB_CSV_URL)

# ============================
# KPI Section
# ============================
st.markdown("### 📌 Key Insights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_alone = df["Time_spent_Alone"].mean()
    st.metric("🕒 Avg Time Alone", f"{avg_alone:.2f} hrs")

with col2:
    avg_post = df["Post_frequency"].mean()
    st.metric("📱 Avg Post Frequency", f"{avg_post:.2f}")

with col3:
    avg_friends = df["Friends_circle_size"].mean()
    st.metric("👥 Avg Friends Circle", f"{avg_friends:.1f}")

with col4:
    top_personality = df["Personality"].mode()[0]
    st.metric("🎭 Most Common Personality", top_personality)

# ============================
# Graph Section in 2x2 layout
# ============================
st.markdown("---")
st.markdown("### 📈 Visual Analysis")

# Row 1
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    bar_df = df.groupby("Personality")["Time_spent_Alone"].mean().reset_index()
    fig1 = px.bar(bar_df, x="Personality", y="Time_spent_Alone", color="Personality",
                  title="Average Time Spent Alone by Personality", labels={"Time_spent_Alone": "Hours"})
    st.plotly_chart(fig1, use_container_width=True)

with row1_col2:
    fig2 = px.histogram(df, x="Friends_circle_size", color="Personality", nbins=15, barmode="overlay",
                        title="Distribution of Friends Circle Size")
    st.plotly_chart(fig2, use_container_width=True)

# Row 2
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    fig3 = px.box(df, x="Personality", y="Post_frequency", color="Personality",
                  title="Post Frequency by Personality Type")
    st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
    fig4 = px.histogram(df, x="Stage_fear", color="Personality", barmode="group",
                        title="Stage Fear Count by Personality")
    st.plotly_chart(fig4, use_container_width=True)

# Row 3 - full width
st.markdown("### 😩 Social Energy Levels")
fig5 = px.histogram(df, x="Drained_after_socializing", color="Personality", barmode="group",
                    title="Feeling Drained After Socializing")
st.plotly_chart(fig5, use_container_width=True)

# Data Preview (last)
with st.expander("🗃️ Full Dataset Preview"):
    st.dataframe(df)
