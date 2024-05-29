import os, requests, json

news = os.environ['newsapi']

country = "in"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"
result = requests.get(url)
data = result.json()

counter = 0
for article in data["articles"]:
    counter += 1
    if counter > 5:
        break
    text = article["title"]
    print(f"{counter}. {text}\n\n")
