from analyze_cv import analyze_cv
from search_jobs import search_jobs
 
 
def calculate_match(cv_text, keywords):
    cv_text = cv_text.lower()
 
    score = 0
 
    for keyword in keywords:
        if keyword.lower() in cv_text:
            score += 1
 
    return round(score / len(keywords) * 100)
 
 
def main():
    cv_text = analyze_cv("cv.pdf")
 
    jobs = search_jobs()
 
    print("=== Résultats ===")
 
    for job in jobs:
        match = calculate_match(cv_text, job["keywords"])
 
        print("----------------")
        print("Poste :", job["title"])
        print("Entreprise :", job["company"])
        print("Match :", f"{match}%")
        print("Lien :", job["link"])
 
 
if __name__ == "__main__":
    main()
