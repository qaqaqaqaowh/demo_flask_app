# 7-ENV variables
# 8-Hot reload
# 9-Template inheritance
# 10-URL helper
# 11-Forms
# 12-Adding database
# 13-Data validation

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile/<name>")
def profile(name): 
    return render_template("profile.html", name=name)

@app.route("/Hello_world")
def special():
    return "<h1>This is a special page</h1>"

app.run()