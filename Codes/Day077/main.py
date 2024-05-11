from flask import Flask
import datetime


app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = ""
    f = open("template/index.html", "r")
    title = "Hello World"
    date = f"{datetime.date.today()}"
    text = "This is my first blog entry."
    page = f.read()
    page = page.replace("{blogTitle}", title)
    page = page.replace("{date}", date)
    page = page.replace("{blogText}", text)
    page = page.replace("{pageTitle}", "First Blog")
    return page

@app.route('/lastblog')
def lastblog():
    page = ""
    f = open("template/index.html", "r")
    title = "Bye World"
    date = f"{datetime.date.today()}"
    text = "This is my last blog entry."
    page = f.read()
    page = page.replace("{blogTitle}", title)
    page = page.replace("{date}", date)
    page = page.replace("{blogText}", text)
    page = page.replace("{pageTitle}", "Last Blog")
    return page
    

app.run(host='0.0.0.0', port=81)
