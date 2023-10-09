from app import app
from flask import redirect, render_template,request,session
import user
from flask_sqlalchemy import SQLAlchemy
import blogs


@app.route("/")
def index():
    return render_template("start.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/result", methods=["POST"])
def result():
    username1 = request.form["username"]
    password1 = request.form["password"]
    button_pressed = request.form.get("button")
    if button_pressed == "create new user":
        return render_template("new_user.html")
    if button_pressed == "sign in":
        result=user.login(username1,password1)
        if result==False:
            return render_template("error.html",message="username or password wrong, try again")
        message=""
        session["username"]=username1
        session["community"]=""
        return redirect("/")

@app.route("/new_user", methods=["POST"])
def new_user():
    new_username=request.form["new username"]
    new_password=request.form["new password"]
    right=user.new_user(new_username,new_password)
    if right==True:
        return redirect("/")
    if right==False:
        return render_template("error2.html",message="username is already exist or password is too short")

@app.route("/Blog",methods=["POST","GET"])
def Blog():
     if request.method=="POST":
         community = request.form["community"]
         session["community"]=community
     if session["community"]=="1":
         list=blogs.find_all_school_blogname()
         return render_template("Blog.html",community="School",list=list)
     if session["community"]=="2":
         list=blogs.find_all_Life_blogname()
         return render_template("Blog.html",community="Life",list=list)
     if session["community"]=="3":
         list=blogs.find_all_sport_blogname()
         return render_template("Blog.html",community="Sport",list=list)
     if session["community"]=="4":
         list=blogs.find_all_game_blogname()
         return render_template("Blog.html",community="Game",list=list)

@app.route("/Blog2")
def Blog2():
    button= request.args.get("find")
    community = session["community"]
    if button=="send":
        blog_name = request.args.get('query')
        if community=="1":
            list=blogs.find_all_school_blog_byname(blog_name)
            return render_template("Blog.html",community="School",list=list)
        if community=="2":
            list=blogs.find_all_Life_blog_byname(blog_name)
            return render_template("Blog.html",community="Life",list=list)
        if community=="3":
            list=blogs.find_all_sport_blog_byname(blog_name)
            return render_template("Blog.html",community="Sport",list=list)
        if community=="4":
            list=blogs.find_all_game_blog_byname(blog_name)
            return render_template("Blog.html",community="Game",list=list)

        
    else:
        blog_id = request.args.get('blog_id')
        message=blogs.find_text(community,blog_id)
        blog_name=request.args.get('blog_name')
        comments=blogs.find_comments(community,blog_id)
        return render_template("Blog2.html",blog_id=blog_id,community=community,blog_name=blog_name,message=message[0])

@app.route("/new_blog")
def new_blog():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    community=request.form["community"]
    content=request.form["content"]
    user=session["username"]
    if community=="1":
        blogs.create_school_blog(topic,content,user)
    message="blog added"
    return  redirect("/Blog")

@app.route("/add_comment", methods=["POST","GET"])
def add_comment():
    community=session["community"]
    blog_id=request.args.get("blog_id")
    blog_name=request.args.get("blog_name")
    return render_template("new_comment.html",community=community,blog_id=blog_id,blog_name=blog_name)

@app.route("/add_comment2", methods=["POST","GET"])
def add_comment2():
    community=session["community"]
    blog_id=request.form["blog_id"]
    content=request.form["query"]
    blog_name=request.form["blog_name"]
    blogs.add_comment(community,blog_id,content)
    message=blogs.find_text(community,blog_id)
    comments=blogs.find_comments(community,blog_id)
    return render_template("Blog2.html",community=community,blog_id=blog_id,blog_name=blog_name,message=message[0],comments=comments)
@app.route("/all_my_blogs",methods=["GET"])
def all_my_blogs():
    username=session["username"]
    list=blogs.all_my_blogs(username)
    return render_template("all_my_blogs.html",list=list)
    
