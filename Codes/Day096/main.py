import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
print("News Search\n")
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
results = False
myLinks = soup.find_all("span",{"class" : "titleline"})
keyword = input("Enter the keyword: ")
for links in myLinks:
  a_tag = links.find('a')
  if a_tag is not None:
    if keyword.lower() in a_tag.text.lower():
      results = True
      print(a_tag.text)
      print(a_tag.get('href'))
      print()
  else:
    print("No link found")
if results == False:
  print("No results found with that keyword")
