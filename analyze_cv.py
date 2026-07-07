from pathlib import Path
from pypdf import PdfReader
 
 
def analyze_cv(cv_file):
    cv_path = Path(cv_file)
 
    if not cv_path.exists():
        return "CV not found."
 
    try:
        reader = PdfReader(cv_path)
 
        text = ""
 
        for page in reader.pages:
            text += page.extract_text() or ""
 
        return text
 
    except Exception as e:
        return f"Error reading CV: {e}"
