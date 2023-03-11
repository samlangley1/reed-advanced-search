import os
from dotenv import load_dotenv
from reed import ReedClient

# Load environment variables from .env file if exists
load_dotenv()

client = ReedClient(os.getenv("API_KEY"))


# Reed search parameters
params = {
    'keywords': "frontend",
    'maximumSalary': 36000,
    'permanent': True,
    'contract': False,
    'temp': False,
    'partTime': False,
    'fullTime': True,
    'minimumSalary': 22000,
}


# Reed search request
response = client.search(**params)
data = [{}]

# Used to return more specific results. For example STRING_MATCH = "front" will exclude any results that do not contain the word "front" in the title.
STRING_MATCH = "front"
for i, r in enumerate(response):
    if STRING_MATCH in r["jobTitle"].lower():
        data.append(response[i])

job_list = []

for job in data:
    for key in job.keys():
        r = f'\nJob title: {job["jobTitle"]}\nSalary range: {job["minimumSalary"]} - {job["maximumSalary"]}\nEmployer name: {job["employerName"]}\nNumber of applications: {job["applications"]}\nJob page URL: {job["jobUrl"]}\n'
        if r not in job_list:
            job_list.append(r)

for job in job_list:
    print(job)
