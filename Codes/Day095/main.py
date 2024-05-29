import os, requests, json
from requests.auth import HTTPBasicAuth

max= 10
news = os.environ['news']

country = "in"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"
result = requests.get(url)
data = result.json()
responses = []
for article in data["articles"]:
  responses.append(article["title"])

clientID = os.environ['CLIENT_ID']
clientSECRET = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = { "grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSECRET)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]
headers = {"Authorization" : f"Bearer {accessToken}"}

songs = []

for response in responses:
  headline = response.replace(" ", "%20")
  headline = response.replace(".", "")
  url = "https://api.spotify.com/v1/search"
  search = f"?q={headline}&type=track"
  fullURL = f"{url}{search}"
  response = requests.get(fullURL, headers=headers)
  data = response.json()
  try:
    songs.append(data["tracks"]["items"][0])
  except:
    songs.append({"name": None, "preview_url": None})

for i in range(max):
  if songs[i]["name"]!=None:
    print(f'News:\t {responses[i]}')
    print(f'Song:\t {songs[i]["name"]}')
    print(f'Preview Url:\t {songs[i]["preview_url"]}')
    print()
