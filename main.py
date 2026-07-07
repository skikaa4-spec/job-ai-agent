from config import OPENAI_MODEL
from analyze_cv import load_cv
from search_jobs import search_jobs
 
print("===== AI JOB AGENT =====")
print(f"Model: {OPENAI_MODEL}")
 
if load_cv():
    print("CV loaded successfully.")
 
    jobs = search_jobs()
 
    print("Jobs found:")
    for job in jobs:
        print(f"- {job['title']} | {job['company']} | {job['city']}")
else:
    print("Please upload cv.pdf")
