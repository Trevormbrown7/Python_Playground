import json

with open('documents/seen_jobs.json', 'r') as f:
    data = json.load(f)


# Grab the whole "seen" dictionary
seen = data['seen']


#print(json.dumps(seen, indent=2))
print(data[1])
print()
print("--------------")
print()
# Pull one specific job by its URL key
url = "https://www.linkedin.com/jobs/view/av-tech-category-10-nashville-at-ryman-hospitality-properties-4438112261"
job = seen[url]

print(job['title'])    # AV Tech - Category 10 Nashville
print(job['company'])  # Ryman Hospitality Properties
print(job['fit'])      # high
print(job['location'])
print()
