from pathlib import Path

def load_cv():
    cv_path = Path("cv.pdf")

    if cv_path.exists():
        print("CV found.")
        return True
    else:
        print("CV not found.")
        return False
