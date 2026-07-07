import requests

def search_jobs():
    print("Searching jobs...")

    jobs = [
        "Magasinier",
        "Chef Magasinier",
        "Superviseur Sécurité",
        "Conducteur de Manitou"
    ]

    countries = [
        "Morocco",
        "France",
        "Canada",
        "United Arab Emirates"
    ]

    results = []

    for country in countries:
        for job in jobs:
            results.append({
                "job": job,
                "country": country
            })

    return results
