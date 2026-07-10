import json

with open('documents/seen_jobs.json', 'r') as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {value}")
