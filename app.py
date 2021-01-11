# 7-ENV variables
# 8-Hot reload
# 9-Template inheritance
# 10-URL helper
# 11-Forms
# 12-Adding database
# 13-Data validation

from flask import Flask, render_template, request
from models import *

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

@app.route("/form")
def see_form():
    return render_template("form.html")

@app.route("/receive", methods=["POST"])
def accept_form():
    task = request.form['task']
    todo = Todo(task=task)
    if todo.save():
        return "Todo saved"
    else:
        return ",".join(todo.errors)

@app.route("/todos")
def todos():
    todos = Todo.select()
    return render_template("todos.html", todos=todos)

@app.route("/todo/<todo_id>")
def todo(todo_id):
    todo = Todo.get_by_id(todo_id)
    return render_template("todo.html", todo=todo)

if __name__ == "__main__":
    app.run()