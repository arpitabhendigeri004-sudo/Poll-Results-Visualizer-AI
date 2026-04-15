import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import time

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Poll Dashboard", layout="wide")

st.title("📊 Real-Time Poll Results Visualizer")

# -----------------------------
# SIDEBAR INPUT (LIVE VOTING)
# -----------------------------
st.sidebar.header("🗳 Submit Your Vote")

user = st.sidebar.text_input("Your Name")
tool = st.sidebar.selectbox("Select Tool", ["Python", "Excel", "R", "Tableau"])
region = st.sidebar.selectbox("Select Region", ["North", "South", "East", "West"])
rating = st.sidebar.slider("Rating", 1, 5)
feedback = st.sidebar.text_area("Your Feedback")

if st.sidebar.button("Submit Vote"):
    try:
        response = requests.post(
            f"{API_URL}/submit",
            params={
                "user": user,
                "tool": tool,
                "region": region,
                "rating": rating,
                "feedback": feedback
            }
        )

        sentiment = response.json()["sentiment"]
        st.sidebar.success(f"Vote Submitted ✅ ({sentiment})")

    except:
        st.sidebar.error("API not running ❌")

# -----------------------------
# FETCH DATA FUNCTIONS
# -----------------------------
def fetch_results():
    try:
        response = requests.get(f"{API_URL}/results")
        data = response.json()["results"]
        return pd.DataFrame(list(data.items()), columns=["Tool", "Votes"])
    except:
        return pd.DataFrame(columns=["Tool", "Votes"])


def fetch_all_data():
    try:
        response = requests.get(f"{API_URL}/all-data")
        data = response.json()
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# -----------------------------
# AUTO REFRESH LOOP
# -----------------------------
refresh_interval = 5

while True:
    df_votes = fetch_results()
    df_full = fetch_all_data()

    if df_votes.empty:
        st.warning("No data yet. Submit a vote!")
    else:
        # RAW DATA
        st.subheader("📄 Raw Data")
        st.dataframe(df_full)

        # TOOL CHARTS
        st.subheader("📊 Tool Popularity")

        col1, col2 = st.columns(2)

        with col1:
            fig_bar = px.bar(df_votes, x="Tool", y="Votes", title="Votes per Tool")
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            fig_pie = px.pie(df_votes, names="Tool", values="Votes", title="Vote Share")
            st.plotly_chart(fig_pie, use_container_width=True)

        # REGION ANALYSIS
        if not df_full.empty:
            st.subheader("🌍 Region-wise Analysis")
            region_data = df_full.groupby("Region")["Tool"].value_counts().unstack().fillna(0)
            fig_heatmap = px.imshow(region_data, text_auto=True)
            st.plotly_chart(fig_heatmap, use_container_width=True)

        # RATING DISTRIBUTION
        st.subheader("⭐ Ratings Distribution")
        fig_hist = px.histogram(df_full, x="Rating", nbins=5)
        st.plotly_chart(fig_hist, use_container_width=True)

        # 🔥 SENTIMENT ANALYSIS
        st.subheader("🧠 Sentiment Analysis")

        sentiment_counts = df_full["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]

        fig_sent = px.bar(sentiment_counts, x="Sentiment", y="Count", color="Sentiment")
        st.plotly_chart(fig_sent, use_container_width=True)

        # 🔥 AI INSIGHT
        top_tool = df_votes.sort_values("Votes", ascending=False).iloc[0]["Tool"]
        st.success(f"🔥 {top_tool} is trending among users!")

        # 📝 BLOG SECTION
        st.subheader("📝 Insights Blog")

        try:
            with open("blog/blog.md", "r") as f:
                st.markdown(f.read())
        except:
            st.info("No blog found. Add blog/blog.md")

    time.sleep(refresh_interval)
    st.rerun()