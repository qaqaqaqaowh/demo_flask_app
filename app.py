# 1-Basic flask app
# 2-Routing with wildcard
# 3-Templates
# 4-Static files
# 5-Display variables on html
# 6-If else in html

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

app.run()