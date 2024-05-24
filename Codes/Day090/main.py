import requests

for i in range (10):
  result = requests.get("https://randomuser.me/api/")
  user = result.json()
  for person in user['results']:
    name = f"""{person["name"]["first"]} {person["name"]["last"]}"""
  
    image = f"""{person["picture"]["medium"]}"""
    picture = requests.get(image)
    f = open(f"Images/{name}.jpg", "wb")
    f.write(picture.content) 
    f.close()
    print(f"Saves image of {name}")

print("All images downloaded")
  
