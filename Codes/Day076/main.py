from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = """ 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hello from Flask!</h1>
        <h2>Welcome to my website</h2>
        <br> <br>
        <h3><a href="/portfolio"> Go to Portfolio</a></h3>
        <h3><a href="/linktree"> Go to Link Tree</a></h3>
    </body>
    </html>
        """
    return page


@app.route('/portfolio')
def portfolio():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width">
      <title>My Portfolio</title>
     <link href="static/CSS/style1.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
      <h1>My Portfolio</h1>
      <h2>Day 71 Solution</h2>
      <p>So, day 71 is all about understanding hashing and salting is crucial for secure data management and authentication processes.</p>
      <div class="img">
        <img src="static/Images/p1.png" width="400px">
      </div>
      <p id="thnx"> Thanks for the support!🤠🩵</p>
<br>
<br>
<h3><a href="/"> Go Back</a></h3>
      <script src="script.js"></script>
    </body>

    </html>
    """
    return page


@app.route('/linktree')
def linktree():
    page = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/CSS/style2.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src="static/Images/image.jpg">
  <h1>Souvik Biswas</h1>
  <p class="about">Embarking on #100DaysOfCode Python Challenge 🐍 || Full Stack Web Development || Cyber security Enthusiast || IT'26 UG at BPPIMT</p>
  <h2>Socials</h2>
  <ul>
    <li><a href="https://twitter.com/souvik2802">Twitter (@souvik2802)</a></li>
    <li><a href="https://github.com/souvikbiswas2802">GitHub (souvikbiswas2802)</a></li>
    <li><a href="https://replit.com/@souvik2802">Replit (@souvik2802)</a></li>
  </ul>
<br>
<br>
<h3><a href="/"> Go Back</a></h3>
  <script src="script.js"></script>

</body>

</html>
    """
    return page

app.run(host='0.0.0.0', port=81)
