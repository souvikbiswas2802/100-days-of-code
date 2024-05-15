from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    page = """
    <html>
    <head><title>Robot Test</title></head>
    <body>
      <form method="post" action="/process">
        <p>Are you made of metal?
          <label><input type="radio" id="yes" name="metal" value="yes"> Yes</label>
          <label><input type="radio" id="no" name="metal" value="no"> No</label>
        </p>
        <p>What is infinity + 1? <input type="text" name="infinity" required></p>
        <p>Which is your favorite food? 
          <select name="food">
            <option value="human food">Human food</option>
            <option value="synthetic oil">Synthetic oil</option>
          </select>
        </p>
        <button type="submit">I am not a robot</button>
      </form>
    </body>
    </html>
    """
    return page

@app.route('/process', methods=["POST"])
def process():
    page = ""
    form = request.form
    if form.get("metal") == "yes" or form.get("food") == "synthetic oil":
        page += "You're a robot!"
    else:
        page += "You're a human!"
    return page

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
