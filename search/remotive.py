import requests
 
 
def search_remotive(limit=50):
    url = "https://remotive.com/api/remote-jobs"
 
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
 
        data = response.json()
        jobs = []
 
        for job in data.get("jobs", [])[:limit]:
 
            jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company_name", ""),
                "location": job.get("candidate_required_location", ""),
                "description": job.get("description", ""),
                "link": job.get("url", "")
            })
 
        return jobs
 
    except Exception as e:
        print("Erreur Remotive :", e)
        return []
