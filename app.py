from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mainpage", methods=["POST"])
def mainpage():
    return render_template("mainpage.html",name=request.form["name"])