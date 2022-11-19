from flask import Flask
from flask import render_template
app = Flask(__name__)
import os

zespoly = {
    'myszy': '3',
    'koty': '4',
    'psy': '2'
}

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/blog/<blog_title>")
def show_user_profile(blog_title):
    foo = zespoly[blog_title]
    return render_template("blog.html", foo = foo)


@app.route("/test")
def another_hello():
    return "<p>Hello Fortnite!</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, use_reloader=True)  
