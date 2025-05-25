from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_rozee_jobs(keyword="data analyst", max_jobs=50):
    print(f"Starting Rozee.pk scraper for '{keyword}'...")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        # Build URL dynamically from keyword
        query = keyword.replace(" ", "%20")
        url = f"https://www.rozee.pk/job/jsearch/q/{query}"
        driver.get(url)
        time.sleep(5)  # Let the page load

        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")

        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job")
        print(f"Found {len(job_cards)} job cards\n")

        jobs = []

        for idx, card in enumerate(job_cards):
            if idx >= max_jobs:
                break  # Limit max jobs scraped

            text_content = card.text.strip()
            if not text_content:
                continue

            lines = text_content.split('\n')
            if len(lines) < 2:
                continue

            title = lines[0].strip()
            company_location = lines[1].strip()

            if ',' in company_location:
                parts = company_location.split(',')
                company = parts[0].strip()
                location = ','.join(parts[1:]).strip()
            else:
                company = company_location
                location = "N/A"

            experience = "N/A"
            salary = "N/A"
            skills = []

            for line in lines[2:]:
                line_lower = line.lower().strip()

                if "year" in line_lower or "fresh" in line_lower:
                    experience = line.strip()
                    continue

                if any(char.isdigit() for char in line) and ('k' in line_lower or '$' in line_lower):
                    salary = line.strip()
                    continue

                if not line_lower.startswith('may ') and not line_lower.startswith('job '):
                    skills.append(line.strip())

            job = {
                "Title": title,
                "Company": company,
                "Location": location,
                "Experience": experience,
                "Salary": salary,
                "Skills": ", ".join(skills),
            }
            jobs.append(job)

        return jobs

    finally:
        driver.quit()
