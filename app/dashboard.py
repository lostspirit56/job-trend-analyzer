import streamlit as st
import pandas as pd
from analysis.analyzer import analyze_jobs

st.title("📊 Real-Time Job Trend Analyzer")

df = pd.read_csv("data/jobs.csv")
st.dataframe(df.head(10))

keyword = st.text_input("Search for a job title (e.g., Data Analyst)")
filtered = df[df['title'].str.contains(keyword, case=False)] if keyword else df

stats = analyze_jobs("data/jobs.csv")
st.bar_chart(stats["top_titles"])
st.bar_chart(stats["top_locations"])
st.line_chart(stats["posting_trend"])
