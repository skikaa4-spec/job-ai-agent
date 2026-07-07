import requests
 
def search_remotive():
    url = "https://remotive.com/api/remote-jobs"
 
    response = requests.get(url, timeout=20)
    response.raise_for_status()
 
    data = response.json()
 
    jobs = []
 
    for job in data["jobs"]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"],
            "link": job["url"],
            "keywords": [
                job["title"],
                job["category"]
            ]
        })
 
    return jobs
