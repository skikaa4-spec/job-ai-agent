from analyze_cv import load_cv
 
print("===== AI JOB AGENT =====")
 
if load_cv():
    print("Starting job search...")
else:
    print("Please upload cv.pdf")
