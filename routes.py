from app import app
from flask import redirect, render_template,request
import user
from flask_sqlalchemy import SQLAlchemy
import blogs

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

@app.route("/Blog", methods=["POST"])
def Blog():
     community = request.form["community"]
     if community=="1":
         list=blogs.find_all_school_blogname()
         return render_template("Blog.html",community="School",list=list)
     if community=="2":
         return render_template("Blog.html",community="Life")
     if community=="3":
         return render_template("Blog.html",community="Sport")
     if community=="4":
         return render_template("Blog.html",community="Game")

@app.route("/Blog2/<name>")
def Blog2(name):
    return render_template("Blog2.html")
