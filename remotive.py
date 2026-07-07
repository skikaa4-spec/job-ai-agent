keywords = [
    "safety",
    "hse",
    "qhse",
    "warehouse",
    "logistics",
    "stock",
    "maintenance",
    "supervisor",
    "odoo",
    "technician"
]
 
title = job["title"].lower()
category = job["category"].lower()
 
if any(k in title or k in category for k in keywords):
    jobs.append({
        "title": job["title"],
        "company": job["company_name"],
        "location": job["candidate_required_location"],
        "link": job["url"],
        "keywords": keywords
    })
