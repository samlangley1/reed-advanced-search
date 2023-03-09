from reed import ReedClient
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = ReedClient(os.getenv("API_KEY"))

params = {
    'keywords' : "frontend",
    'maximumSalary' : 36000,
    'permanent' : True,
    'contract' : False,
    'temp' : False,
    'partTime' : False,
    'fullTime' : True,
    'minimumSalary' : 22000,
}

response = client.search(**params)
data = [{}]
for i, r in enumerate(response):
    if "front" in r["jobTitle"].lower():
        data.append(response[i])

job_list = []

for job in data:
    for key in job.keys():
        r = f'\nJob title: {job["jobTitle"]}\nSalary range: {job["minimumSalary"]} - {job["maximumSalary"]}\nEmployer name: {job["employerName"]}\nNumber of applications: {job["applications"]}\nJob page URL: {job["jobUrl"]}\n'
        if r not in job_list:
            job_list.append(r)

for job in job_list:
    print(job)
