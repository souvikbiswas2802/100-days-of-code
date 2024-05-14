from flask import Flask, request

app = Flask(__name__)

admin1 = {"emain": "admin1@mail.in", "password": "password1"}
admin2 = {"emain": "admin2@mail.in", "password": "password2"}
admin3 = {"emain": "admin3@mail.in", "password": "password3"}
username = {"admin1": admin1, "admin2": admin2, "admin3": admin3}

@app.route('/login', methods=["POST"])
def process():
  page = ""
  form = request.form
  try:
    if username[form["username"]]["password"] == form["password"] and username[form["username"]]["email"] == form["email"]:
      page += f"You are logged in {form['username']}"
    else:
      page += "Get out of here! You Hacker!"
  except:
    page += "Get out of here! You Hacker!"
  return page


@app.route('/')
def index():
  page = """
  <form method="post" action="/login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="Email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p> 
    <button type="submit">Login </button>
  </form>
    """
  return page
  
app.run(host='0.0.0.0', port=81)
