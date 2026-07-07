def calculate_match(cv_text, keywords):
    cv = cv_text.lower()
 
    score = 0
 
    for keyword in keywords:
        if keyword.lower() in cv:
            score += 1
 
    return round(score / len(keywords) * 100)
