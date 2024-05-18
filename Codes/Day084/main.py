from flask import Flask, request, redirect

from replit import db

app = Flask(__name__, static_url_path='/static')


@app.route('/login', methods=["POST"])
def dologin():
  form = request.form
  try:
    if db[request.form["username"]]["password"]== request.form["password"]:
      return f"Hello {db[request.form['username']]['name']}, have a nice day."
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")

@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""

@app.route("/signup", methods=["POST"])
def dosignup():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return "Username already exists"

@app.route("/login")
def login():
    page = ""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page


@app.route("/signup")
def signup():
    page = ""
    f = open("signup.html", "r")
    page = f.read()
    f.close()
    return page

@app.route('/')
def index():
  page = """
<p> <a href="/login">Log In </a></p>
<p> <a href="/signup">Sign Up </a></p>
"""
  return page


app.run(host='0.0.0.0', port=81)
