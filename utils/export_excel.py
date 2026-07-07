from openpyxl import Workbook
import os
 
 
def export_jobs(jobs):
    os.makedirs("output", exist_ok=True)
 
    wb = Workbook()
    ws = wb.active
    ws.title = "Jobs"
 
    ws.append([
        "Title",
        "Company",
        "Country",
        "Match %",
        "Link"
    ])
 
    for job in jobs:
        ws.append([
            job["title"],
            job["company"],
            job["location"],
            job["match"],
            job["link"]
        ])
 
    wb.save("output/jobs.xlsx")
 
    print("Jobs exported to output/jobs.xlsx")
