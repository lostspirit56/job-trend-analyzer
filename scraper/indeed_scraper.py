def scrape_indeed(keyword="software", limit=50):
    import requests
    from bs4 import BeautifulSoup

    url = f"https://www.indeed.com/jobs?q={keyword}&limit={limit}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for card in soup.select(".job_seen_beacon"):
        title_elem = card.select_one("h2 span")
        company_elem = card.select_one(".companyName")
        location_elem = card.select_one(".companyLocation")
        date_elem = card.select_one(".date")

        title = title_elem.text.strip() if title_elem else "N/A"
        company = company_elem.text.strip() if company_elem else "N/A"
        location = location_elem.text.strip() if location_elem else "N/A"
        date = date_elem.text.strip() if date_elem else "N/A"

        jobs.append([title, company, location, "N/A", date])
    
    return jobs
