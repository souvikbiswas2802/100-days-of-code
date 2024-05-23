import os, datetime
from flask import Flask, redirect, request
from replit import db
import time

def updateComments():
  feed = ""
  keys = list(db.keys())
  keys = [key for key in keys if key.isdigit()]
  keys = sorted(keys, key=int)
  keys = reversed(keys)
  n = 0
  for key in keys:
      if n >= 5:
          break
      img = db[key]['profilepic']
      userName = db[key]['username']
      comment = db[key]['comment']
      timestamp = db[key]['timestamp']
      feed += f"""
      <hr>
      <img src = {img} width = "30"> {userName}
      <h3>at {timestamp}<h3>
      <p>Commented: {comment}</p>
      """
      n += 1
  return feed

def updateCommentsAdmin():
  feed = ""
  keys = list(db.keys())
  keys = sorted(keys, key=int)
  keys = reversed(keys)
  for key in keys:
    img = db[key]['profilepic']
    userName = db[key]['username']
    comment = db[key]['comment']
    timestamp = db[key]['timestamp']
    feed += f"""<hr>
<img src = {img} width = "30"> {userName}
<h3>at {timestamp}<h3>
<p>Commented: {comment} <a href="/deleteComment?key={key}"><button>❌</button></a></p>"""
  return feed

adminUserID = "31333784"

app = Flask(__name__, static_url_path = "/static")

@app.route("/")
def home():
  if request.headers["X-Replit-User-Name"]:
    userID = request.headers["X-Replit-User-Name"]
    if userID == adminUserID:
      return redirect("/loggedInAdmin")
    return redirect("/loggedIn")
  else:
    page = ""
    f = open("landingpage.html", "r")
    page = f.read()
    f.close()
    page += updateComments()
    return page

@app.route("/loggedIn")
def loggedIn():
  if not request.headers["X-Replit-User-Name"]:
    return redirect("/")
  page = ""
  f = open("loggedInPage.html", "r")
  page = f.read()
  f.close()
  username = request.headers["X-Replit-User-Name"]
  page = page.replace("{username}", username)
  page += updateComments()
  return page

@app.route("/loggedInAdmin", methods = ["GET"])
def loggedInAdmin():
  if not request.headers["X-Replit-User-Name"]:
    return redirect("/")
  page = ""
  f = open("adminLoggedInPage.html", "r")
  page = f.read()
  f.close()
  username = request.headers["X-Replit-User-Name"]
  page = page.replace("{username}", username)
  page += updateCommentsAdmin()
  return page

@app.route("/addComment", methods=["POST"])
def addComment():
    timestamp = datetime.datetime.now()
    timestamp = str(timestamp)
    form = request.form
    comment = form['comments']
    username = request.headers["X-Replit-User-Name"]
    profilepic = request.headers["X-Replit-User-Profile-Image"]
    dbKeys = list(db.keys())

    dbKeys = [key for key in dbKeys if key.isdigit()]

    dbKeys = sorted(dbKeys, key=int)

    if dbKeys:
        nthCommentNumber = dbKeys[-1] 
        dbKey = int(nthCommentNumber) + 1
    else:
        dbKey = 1

    dbKey = str(dbKey)
    db[dbKey] = {"username": username, "profilepic": profilepic, "comment": comment, "timestamp": timestamp}
    return redirect("/")

@app.route("/deleteComment", methods=["GET"])
def deleteComment():
    key = request.args.get('key')

    if key in db:
        del db[key]
        return redirect("/")
    else:
        return "Comment key not found"

app.run(host='0.0.0.0', port=81)
