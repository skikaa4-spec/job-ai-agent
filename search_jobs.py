from search.remotive import search_remotive
from search.emploi_ma import search_emploi_ma
 
 
def search_jobs():
    jobs = []
 
    jobs.extend(search_emploi_ma())
 
    jobs.extend(search_remotive())
 
    return jobs
