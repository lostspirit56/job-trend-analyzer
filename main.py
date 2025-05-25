import os
import pandas as pd
from scraper.rozee_scraper import scrape_rozee_jobs

def run_scraper():
    jobs = scrape_rozee_jobs("data analyst")  # You can change the query here
    if not jobs:
        print("No jobs found.")
        return
    
    df = pd.DataFrame(jobs)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/jobs.csv", index=False)
    print("Saved scraped data to data/jobs.csv")

if __name__ == "__main__":
    run_scraper()
