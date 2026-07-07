from analyze_cv import analyze_cv
from search_jobs import search_jobs
from utils.matcher import calculate_match
from utils.export_excel import export_jobs
 
 
def main():
 
    cv = analyze_cv("cv.pdf")
 
    jobs = search_jobs()
 
    results = []
 
    for job in jobs:
 
        match = calculate_match(
            cv,
            job["keywords"]
        )
 
        job["match"] = match
 
        results.append(job)
 
    results.sort(
        key=lambda x: x["match"],
        reverse=True
    )
 
    for job in results:
 
        print("----------------")
 
        print(job["title"])
 
        print(job["company"])
 
        print(job["location"])
 
        print(str(job["match"]) + "%")
 
        print(job["link"])
 
    export_jobs(results)
 
 
if __name__ == "__main__":
    main()
