import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Personality Data Dashboard")

# 🔗 Replace this with your actual GitHub raw CSV link
GITHUB_CSV_URL = "https://raw.githubusercontent.com/ibtysxmslhx/mini-project/refs/heads/main/cleaned_personality_dataset.csv"

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Sidebar configuration
with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Load data from uploaded file or GitHub
if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data(GITHUB_CSV_URL)

# Data Preview
with st.expander("📄 Data Preview"):
    st.dataframe(df)

# 1. Bar chart - Time Spent Alone
st.subheader("1. Average Time Spent Alone by Personality")
bar_df = df.groupby("Personality")["Time_spent_Alone"].mean().reset_index()
fig1 = px.bar(bar_df, x="Personality", y="Time_spent_Alone", color="Personality",
              title="Average Time Spent Alone by Personality", labels={"Time_spent_Alone": "Hours"})
st.plotly_chart(fig1, use_container_width=True)

# 2. Histogram - Friends Circle Size
st.subheader("2. Distribution of Friends Circle Size")
fig2 = px.histogram(df, x="Friends_circle_size", color="Personality", nbins=15, barmode="overlay",
                    title="Distribution of Friends Circle Size")
st.plotly_chart(fig2, use_container_width=True)

# 3. Boxplot - Post Frequency
st.subheader("3. Post Frequency by Personality Type")
fig3 = px.box(df, x="Personality", y="Post_frequency", color="Personality",
              title="Post Frequency by Personality Type")
st.plotly_chart(fig3, use_container_width=True)

# 4. Countplot - Stage Fear
st.subheader("4. Stage Fear Count by Personality")
fig4 = px.histogram(df, x="Stage_fear", color="Personality", barmode="group",
                    title="Stage Fear Count by Personality")
st.plotly_chart(fig4, use_container_width=True)

# 5. Countplot - Drained After Socializing
st.subheader("5. Feeling Drained After Socializing")
fig5 = px.histogram(df, x="Drained_after_socializing", color="Personality", barmode="group",
                    title="Feeling Drained After Socializing")
st.plotly_chart(fig5, use_container_width=True)

    st.dataframe(filtered_df)



