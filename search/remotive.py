import requests
 
KEYWORDS = [
    "QHSE",
    "Safety",
    "HSE",
    "Warehouse",
    "Logistics",
    "Stock",
    "Maintenance",
    "Supervisor",
    "Technician",
    "Odoo"
]
 
def search_remotive():
    url = "https://remotive.com/api/remote-jobs"
 
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
 
        jobs = []
 
        for job in data["jobs"]:
 
            title = job["title"].lower()
 
            if any(word.lower() in title for word in KEYWORDS):
 
                jobs.append({
                    "title": job["title"],
                    "company": job["company_name"],
                    "location": job["candidate_required_location"],
                    "link": job["url"],
                    "keywords": KEYWORDS
                })
 
        return jobs
 
    except Exception as e:
        print("Erreur:", e)
        return []
