from flask import Flask

app = Flask(__name__, static_url_path="/static")

myReflections = {}

myReflections["76"] = {"link": "https://replit.com/@souvik2802/Day76100Days#main.py", "Reflection": "Flask provides a powerful framework for building web applications in Python, allowing seamless integration of front-end and back-end components."}

myReflections["77"] = {"link": "https://replit.com/@souvik2802/Day77100Days#main.py", "Reflection": "Leveraging file handling and string formatting within Flask allows for versatile and dynamic web applications, enabling easy management and presentation of content."}


@app.route('/')
def home():
  page = "Welcome to my reflections"
  return page
  

@app.route('/<pageNumber>')
def index(pageNumber):
  global Reflections
  page = ""
  f = open("template/reflection.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{day}", pageNumber)
  page = page.replace("{link}", myReflections[pageNumber]["link"])
  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
  return page


app.run(host='0.0.0.0', port=81)
