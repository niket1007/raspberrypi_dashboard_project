from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def screen_config_func():
    return render_template("Screen_Config.html")

@app.route("/todo")
def todo_func():
    return render_template("Todo.html")

@app.route("/meetings")
def meetings_func():
    return render_template("Meeting.html")

@app.route("/calendar")
def calendar_func():
    return render_template("Calendar.html")


app.run(host="localhost", port=8080, debug=True)