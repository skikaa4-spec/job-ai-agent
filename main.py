from analyze_cv import analyze_cv
from search_jobs import search_jobs
from utils.matcher import calculate_match
from utils.export_excel import export_jobs
 
 
def main():
    print("=== AI Job Agent V1 ===")
 
    # قراءة الـ CV
    cv_text = analyze_cv("cv.pdf")
 
    if not cv_text:
        print("Erreur : impossible de lire le CV.")
        return
 
    # البحث عن الوظائف
    jobs = search_jobs()
 
    if not jobs:
        print("Aucune offre trouvée.")
        return
 
    results = []
 
    for job in jobs:
        match = calculate_match(
            cv_text,
            job.get("title", ""),
            job.get("description", "")
        )
 
        job["match"] = match
        results.append(job)
 
    # ترتيب النتائج
    results.sort(key=lambda x: x["match"], reverse=True)
 
    # عرض أفضل 20 وظيفة
    print("\n=== Top Jobs ===\n")
 
    for job in results[:20]:
        print("-" * 50)
        print("Titre      :", job["title"])
        print("Entreprise :", job["company"])
        print("Lieu       :", job["location"])
        print("Match      :", str(job["match"]) + "%")
        print("Lien       :", job["link"])
 
    export_jobs(results)
 
 
if __name__ == "__main__":
    main()
