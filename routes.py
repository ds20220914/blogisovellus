from app import app
from flask import render_template,request
from user import login

@app.route("/")
def index():
    return render_template("start.html")

@app.route("/result", methods=["POST"])
def result():
    username1 = request.form["username"]
    password1 = request.form["password"]
    result=login(username1,password1)
    if result==False:
        return render_template("start.html")
    return render_template("result.html",result=result )
