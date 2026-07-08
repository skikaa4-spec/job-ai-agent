from search.remotive import search_remotive
 
def get_all_jobs():
    jobs = []
 
    try:
        jobs.extend(search_remotive())
    except Exception as e:
        print("Remotive error:", e)
 
    return jobs
