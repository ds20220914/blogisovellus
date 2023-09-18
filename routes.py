from app import app
from flask import redirect, render_template,request
import user
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def index():
    return render_template("start.html")

@app.route("/result", methods=["POST"])
def result():
    username1 = request.form["username"]
    password1 = request.form["password"]
    button_pressed = request.form.get("button")
    if button_pressed == "new":
        return render_template("new_user.html")
    if button_pressed == "next":
        result=user.login(username1,password1)
        if result==False:
            return render_template("start.html")
        return render_template("result.html",result=result )

@app.route("/new_user", methods=["POST"])
def new_user():
    new_username=request.form["new username"]
    new_password=request.form["new password"]
    right=user.new_user(new_username,new_password)
    return redirect("/")

