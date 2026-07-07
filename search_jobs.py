import requests
from bs4 import BeautifulSoup
 
 
def search_jobs():
    url = "https://www.emploi.ma/recherche-jobs-maroc"
 
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
 
    jobs = []
 
    try:
        response = requests.get(url, headers=headers, timeout=10)
 
        if response.status_code != 200:
            return jobs
 
        soup = BeautifulSoup(response.text, "html.parser")
 
        for link in soup.find_all("a", href=True)[:20]:
            title = link.get_text(strip=True)
 
            if len(title) > 10:
                jobs.append({
                    "title": title,
                    "company": "Emploi.ma",
                    "location": "Maroc",
                    "link": "https://www.emploi.ma" + link["href"]
                })
 
    except Exception as e:
        print(e)
 
    return jobs
