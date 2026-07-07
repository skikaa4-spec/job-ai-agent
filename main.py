from search_jobs import search_jobs
 
def main():
    print("Searching for jobs...")
    jobs = search_jobs()
 
    if not jobs:
        print("No jobs found.")
        return
 
    for job in jobs:
        print(job)
 
if __name__ == "__main__":
    main()
