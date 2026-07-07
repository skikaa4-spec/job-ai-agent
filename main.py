from config import OPENAI_MODEL
from analyze_cv import load_cv
 
print("===== AI JOB AGENT =====")
print(f"Model: {OPENAI_MODEL}")
 
if load_cv():
    print("CV loaded successfully.")
    print("Starting job search...")
else:
    print("Please upload cv.pdf")
