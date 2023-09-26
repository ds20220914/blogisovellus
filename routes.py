from app import app
from flask import redirect, render_template,request,session
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
        message=""
        return render_template("result.html",result=result,message=message)

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
         list=blogs.find_all_Life_blogname()
         return render_template("Blog.html",community="Life",list=list)
     if community=="3":
         list=blogs.find_all_sport_blogname()
         return render_template("Blog.html",community="Sport",list=list)
     if community=="4":
         list=blogs.find_all_game_blogname()
         return render_template("Blog.html",community="Game",list=list)

@app.route("/Blog2")
def Blog2():
    community = request.args.get('community')
    blog_name = request.args.get('blog_name')
    return render_template("Blog2.html",community=community,blog_name=blog_name)

@app.route("/new_blog")
def new_blog():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    community=request.form["community"]
    content=request.form["content"]
    if community=="1":
        blogs.create_school_blog(topic,content)
    result=session["username"]
    message="blog added"
    return  render_template("result.html",result=result,message=message)
