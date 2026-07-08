from search.remotive import search_remotive
 
 
def search_jobs():
    jobs = []
 
    jobs.extend(search_remotive())
 
    return jobs
