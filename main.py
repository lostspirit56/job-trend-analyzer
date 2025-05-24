import os
import pandas as pd
from scraper.indeed_scraper import scrape_indeed

def run_scraper():
    jobs = scrape_indeed("data analyst")
    df = pd.DataFrame(jobs, columns=["Title", "Company", "Location", "Skills", "Date"])

    # ✅ This line creates the "data" folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # ✅ Now this will work without error
    df.to_csv("data/jobs.csv", index=False)

if __name__ == "__main__":
    run_scraper()
