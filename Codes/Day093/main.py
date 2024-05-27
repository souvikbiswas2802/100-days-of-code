import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']
artist = input("Artist: ").lower()
artist= artist.replace(" ","%20")
url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)


accessToken = response.json()["access_token"]


url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {accessToken}"}
search = f"?q=artist%3A{artist}&type=track&limit=5"

fullURL = f"{url}{search}"

response = requests.get(fullURL, headers=headers)
data = response.json()


for track in data["tracks"]["items"]:
  print(f"\nSong:\t{track['name']}")
  print(f"URL:\t{track['preview_url']}")
