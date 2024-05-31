import requests
import os
from bs4 import BeautifulSoup
import google.generativeai as genai
from pathlib import Path
import json

GOOGLE_API_KEY = os.environ['GEMINI_API']
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

url = input("Paste Wikipedia URL: ")
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find_all("p")
text = ""
for article in content:
  text += article.text

response = model.generate_content(f"Write summary for the following article in plain text form: {text}")
generated_text = response.candidates[0].content.parts[0].text
print("\033[34m\n","Summary:","\033[0m",f"\n{generated_text}\n\n")

print("\033[34m","References:","\033[0m")
refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ",""))
