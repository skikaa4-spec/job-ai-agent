import requests
from bs4 import BeautifulSoup
 
 
KEYWORDS = [
    "magasinier",
    "logistique",
    "stock",
    "gestionnaire de stock",
    "préparateur de commandes",
    "maintenance",
    "qhse",
    "sécurité"
]
 
 
def search_emploi_ma():
    jobs = []
 
    try:
        url = "https://www.emploi.ma/recherche-jobs-maroc"
 
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
 
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "lxml")
 
        cards = soup.find_all("div", class_="card-job")
 
        for card in cards:
 
            title = card.get_text(" ", strip=True)
 
            title_lower = title.lower()
 
            if any(word in title_lower for word in KEYWORDS):
 
                jobs.append({
                    "title": title,
                    "company": "Emploi.ma",
                    "location": "Maroc",
                    "description": title,
                    "link": url
                })
 
        return jobs
 
    except Exception as e:
        print("Emploi.ma :", e)
        return []
