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
     community=session["community"]
     list=blogs.find_all_blogs(session["community"])
     return render_template("Blog.html",community=community,list=list)

@app.route("/Blog2",methods=["POST","GET"])
def Blog2():
    button= request.args.get("find")
    community = session["community"]
    if button=="search":
        blog_name = request.args.get('query')
        list=blogs.find_all_blogs_byname(blog_name,community)
        return render_template("Blog.html",community=community,list=list)

    else:
        community=request.args.get('community')
        if session["community"]=="":
            session["community"]=community

        blog_id = request.args.get('blog_id')
        message=blogs.find_text(community,blog_id)
        blog_name=request.args.get('blog_name')
        comments=blogs.find_comments(blog_id)
        blog_password=blogs.check_if_blog_password(blog_id)
        writer_name=blogs.find_writer_name(blog_id)
        
        if blog_password!=None and session["username"]!="admin1" and writer_name[0]!=session["username"]:
            return render_template("private.html",passw=blog_password[0],blog_id=blog_id,community=community,blog_name=blog_name,message=message[0])

        return render_template("Blog2.html",blog_id=blog_id,community=community,blog_name=blog_name,message=message[0],comments=comments)


@app.route("/check_password",methods=["POST"])
def check_password():
    password=request.form["password"]
    password1=request.form["password1"]
    blog_id=request.form["blog_id"]
    community=request.form["community"]
    blog_name=request.form["blog_name"]
    message=request.form["message"]
    if password==password1:
        comments=blogs.find_comments(blog_id)
        return render_template("Blog2.html",blog_id=blog_id,community=community,blog_name=blog_name,message=message,comments=comments)

@app.route("/new_blog")
def new_blog():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    community=request.form["community"]
    content=request.form["content"]
    user=session["username"]
    userid=blogs.find_userid_by_name(user)
    blog_password=request.form["password"]
    blogs.create_blog(topic,content,int(userid[0]),community)
    blog_id=blogs.recently_added_blog(userid[0])
    if len(blog_password)!=0:
        blogs.add_blog_password(int(blog_id[0]),blog_password)
        
    return   render_template("start.html")

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
    blogs.add_comment(blog_id,content)
    message=blogs.find_text(community,blog_id)
    comments=blogs.find_comments(blog_id)
    return render_template("Blog2.html",community=community,blog_id=blog_id,blog_name=blog_name,message=message[0],comments=comments)

@app.route("/all_my_blogs",methods=["POST","GET"])
def all_my_blogs():
    if request.method=="POST":
        delete=request.form.getlist("id")
        blogs.delete_blog(delete)
    commu1="school"
    commu2="life"
    commu3="game"
    commu4="sport"
    username=session["username"]
    id=blogs.find_userid_by_name(username)
    admin=blogs.check_if_admin(id)
    if len(admin)!=0:
        list=blogs.find_all_all_blogs()
        return render_template("all_my_blogs.html",list=list,commu1=commu1,commu2=commu2,commu3=commu3,commu4=commu4)
    userid=blogs.find_userid_by_name(username)
    list=blogs.all_my_blogs(userid[0])
    return render_template("all_my_blogs.html",list=list,commu1=commu1,commu2=commu2,commu3=commu3,commu4=commu4)
    
