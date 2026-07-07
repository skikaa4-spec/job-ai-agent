from analyze_cv import analyze_cv
from search_jobs import search_jobs
 
 
def main():
    cv_file = "Cv.pdf"
 
    # تحليل السيرة الذاتية
    cv_result = analyze_cv(cv_file)
 
    print("=== تحليل CV ===")
    print(cv_result)
 
    # البحث عن الوظائف
    jobs = search_jobs()
 
    print("\n=== الوظائف المناسبة ===")
 
    for job in jobs:
        print("----------------")
        print("Poste :", job["title"])
        print("Entreprise :", job["company"])
        print("Lieu :", job["location"])
        print("Lien :", job["link"])
 
 
if __name__ == "__main__":
    main()
