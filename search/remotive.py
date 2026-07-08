import requests
 
def search_remotive():
    url = "https://remotive.com/api/remote-jobs"
 
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
 
        jobs = []
 
        for job in data["jobs"][:20]:
            jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "link": job["url"],
                "keywords": []
            })
 
        return jobs
 
    except Exception as e:
        print("Erreur:", e)
        return []
 
