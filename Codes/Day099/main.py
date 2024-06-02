import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from replit import db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

interests = ["teams", "education"]

keys = db.keys()
for key in keys:
  del db[key]
   
def email(text, link):
  password = os.environ['mailPassword']
  username = os.environ['mailUsername']
  host = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=host, port=port)
  s.starttls()
  s.login(username, password)
  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "New Community Event"
  if link != None:
    newtext = f"""<a href="{link}">{text}</a>"""
  else:
    newtext = text
  msg.attach(MIMEText(newtext, 'html'))
  s.send_message(msg)
  del msg

def getHub():
  url = "https://replit.com/community-hub"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")
  myLinks = soup.find_all("div", {"class": "css-1bms7u6"})
  counter = 0
  keys = db.keys()
  for link in myLinks:
    if "Community Spaces" in link.text:
      break
    if counter!=0:
      print(link.text)
      thisLink = link.find("a")['href']
      print(thisLink)
      print()
      words = link.text.split()
      amInterested = False
      for word in words:
        if word.lower() in interests:
          amInterested = True
      if link.text not in keys:
        if amInterested:
          db[link.text] = thisLink
          email(link.text, thisLink)
        else:
          email(link.text, None)
    counter += 1

getHub()
schedule.every(10).hours.do(getHub)
while True:
  schedule.run_pending()
  time.sleep(1)
