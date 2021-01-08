# 1-Basic flask app
# 2-Routing with wildcard
# 3-Templates
# 4-Static files
# 5-Display variables on templates
# 6-If else in html

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def profile(name):
    return render_template("profile.html", name=name)

app.run()