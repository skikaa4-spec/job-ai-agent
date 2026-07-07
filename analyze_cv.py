from pathlib import Path
 
 
def analyze_cv(cv_file):
    cv_path = Path(cv_file)
 
    if cv_path.exists():
        return "CV found and analyzed."
 
    return "CV not found."
 
 
def load_cv():
    cv_path = Path("cv.pdf")
 
    if cv_path.exists():
        print("CV found.")
    else:
        print("CV not found.")
