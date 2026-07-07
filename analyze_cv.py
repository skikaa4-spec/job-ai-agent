from pathlib import Path
 
 
def analyze_cv(cv_file):
    cv_path = Path("/workspaces/job-ai-agent/Cv.pdf")
 
    print("Looking for:", cv_path)
 
    if cv_path.exists():
        return "CV found and analyzed."
 
    return "CV not found."
