import requests
import random

url = 'https://hub.docker.com/v2/repositories/library/?page_size=100&tags=latest&operating_system=linux'


results = []

while len(results) < 1000:
    response = requests.get(url)
    json_data = response.json()
    for result in json_data['results']:
        name = result['name']
        results.append(name)
        if len(results) >= 1000:
            break
    if 'next' in json_data and json_data['next']:
        url = json_data['next']
    else:
        break

random_results = random.sample(results, min(len(results), 1000))
print(random_results)

# write results to file
with open('random_images.txt', 'w') as f:
    for image in random_results:
        f.write(image + '\n')

