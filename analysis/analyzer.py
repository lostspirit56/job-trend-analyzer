import pandas as pd
from collections import Counter

def analyze_jobs(csv_file):
    df = pd.read_csv(csv_file)
    top_titles = df['title'].value_counts().head(5)
    top_locations = df['location'].value_counts().head(5)
    top_dates = df['date'].value_counts().sort_index()

    return {
        "top_titles": top_titles,
        "top_locations": top_locations,
        "posting_trend": top_dates
    }
