import re
 
 
def extract_keywords(text):
    words = re.findall(r"[a-zA-ZÀ-ÿ]{3,}", text.lower())
 
    stop_words = {
        "the", "and", "for", "with", "from", "dans", "pour",
        "les", "des", "une", "est", "sur", "par", "aux",
        "de", "du", "la", "le", "et", "ou", "en"
    }
 
    return set(word for word in words if word not in stop_words)
 
 
def calculate_match(cv_text, title, description):
    cv_keywords = extract_keywords(cv_text)
    job_keywords = extract_keywords(title + " " + description)
 
    if not job_keywords:
        return 0
 
    common = cv_keywords.intersection(job_keywords)
 
    return round((len(common) / len(job_keywords)) * 100)
