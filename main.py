import requests
 
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
 
print("========== AI JOB AGENT ==========")
 
for country in countries:
    print(f"\n🌍 {country}")
    for job in jobs:
        print(f"🔍 Searching for: {job}")
 
print("\nSearch completed successfully.")
