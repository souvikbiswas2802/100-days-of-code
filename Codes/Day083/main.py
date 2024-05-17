from flask import Flask, request
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/', methods=["GET", "POST"])
def index():
    theme = request.args.get('theme', default='light')
    base_css_path = "template/style.css"
    with open(base_css_path, "r") as f:
        base_css = f.read()

    if theme == "dark":
        theme_css = """
        body {
            background-color: black;
            color: white;
        }
        """

    elif theme == "blue":
        theme_css = """
        body {
            background-color: rgb(14, 127, 241);
            color: rgb(2, 2, 178);
        }
        """
        
    else:
        theme_css = """
        body {
            background-color: white;
            color: black;
        }
        """

    css_content = base_css + theme_css

    with open("template/index.html", "r") as f:
        page = f.read()

    title = "Hello World"
    date = f"{datetime.date.today()}"
    text = "This is my first blog entry."
    page = page.replace("{blogTitle}", title)
    page = page.replace("{date}", date)
    page = page.replace("{blogText}", text)
    page = page.replace("{pageTitle}", "First Blog")
    page = page.replace("{pageStyle}", css_content)
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
