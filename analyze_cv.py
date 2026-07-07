from pathlib import Path
 
 
def analyze_cv(cv_file):
    cv_path = Path(cv_file)
 
    print("Checking file:", cv_path.absolute())
 
    if cv_path.exists():
        return "CV found and analyzed."
 
    return "CV not found."
