from pathlib import Path
from pypdf import PdfReader
 
 
def analyze_cv(file_path):
    path = Path(file_path)
 
    if not path.exists():
        print(f"CV introuvable : {file_path}")
        return ""
 
    try:
        reader = PdfReader(str(path))
        text = ""
 
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
 
        return text.lower()
 
    except Exception as e:
        print("Erreur lors de la lecture du CV :", e)
        return ""
