"""here are all the passes between the pages"""
from flask import redirect, render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from app import app
import user
import blogs
import secrets

@app.route("/")
def index():
    """
       This route renders and displays the start page to the user.
       returns:Rendered templates"""
    return render_template("start.html")

@app.route("/logout")
def logout():
    """ This route delete the user's login session,
        and displays the start page to the user.
        returns:Rendered templates"""
    del session["username"]
    return redirect("/")

@app.route("/result", methods=["POST"])
def result():
    """Process the form data and handle user sign-in or new user creation.
       returns: redirects to start route."""
    username1 = request.form["username"]
    password1 = request.form["password"]
    button_pressed = request.form.get("button")
    if button_pressed == "create new user":
        return render_template("new_user.html")
    if button_pressed == "sign in":
        result1=user.login(username1,password1)
        if result1 is False:
            return render_template("error.html",message="username or password wrong, try again")
        session["username"]=username1
        session["csrf_token"] = secrets.token_hex(16)
        session["community"]=''
        return redirect("/")

@app.route("/new_user", methods=["POST"])
def new_user():
    """Handle the creation of a new user.
       returns:rendered templates or redirect to start page"""
    new_username=request.form["new username"]
    new_password=request.form["new password"]
    right=user.new_user(new_username,new_password)
    if right is True:
        return redirect("/")
    if right is False:
        return render_template("error2.html",
                                message="username is already exist or password is too short")

@app.route("/Blog",methods=["POST","GET"])
def Blog():
    """show all the blogs in a community
       returns: Rendered templates"""
    if request.method=="POST":
        community = request.form["community"]
        session["community"]=community
    community=session["community"]
    list1=blogs.find_all_blogs(community)
    session["blog"]=""
    return render_template("Blog.html",community=community,list1=list1)

@app.route("/Blog2",methods=["POST","GET"])
def Blog2():
    """show single blog
       returns: Rendered templates"""
    button= request.args.get("find")
    if button=="search":
        blog_name = request.args.get('query')
        if blog_name is None or len(blog_name)==0:
            list1=blogs.find_all_blogs(session["community"])
            return render_template("Blog.html",community=session["community"],list1=list1)
        list1=blogs.find_all_blogs_byname(blog_name,session["community"])
        return render_template("Blog.html",community=session["community"],list1=list1)

    community=request.args.get('community')
    session["community"]=community
    if session["community"]=="":
        session["community"]=community

    blog_id = request.args.get('blog_id')
    message=blogs.find_text(community,blog_id)
    new_message=message[0].replace('\n', '<br>')
    blog_name=request.args.get('blog_name')
    blog_password=blogs.check_if_blog_password(blog_id)
    comments=blogs.find_comments(blog_id)
    comments2=[]
    writer_name1=blogs.find_writer_name(blog_id)
    for i in comments:
        writer_name=blogs.find_comment_writer_name(i[0])
        comments2.append((i[1],writer_name[0],i[3]))
    if blog_password is not None:
        if writer_name1[0]!=session["username"] and session["username"]!="admin1" and session["blog"]!=blog_id:
            return render_template("private.html",
                                    passw=blog_password[0],blog_id=blog_id,
                                    community=community,blog_name=blog_name,
                                    message=new_message,blog_time=message[2],blog_writer=writer_name1[0])

    return render_template("Blog2.html",
                            blog_id=blog_id,community=community,message2=message,
                            blog_name=blog_name,message=new_message,
                            comments=comments2,blog_time=message[2],blog_writer=writer_name1[0])


@app.route("/check_password",methods=["POST"])
def check_password():
    """check if a blog has password
       returns: Rendered template"""
    password=request.form["password"]
    password1=request.form["password1"]
    blog_id=request.form["blog_id"]
    community=request.form["community"]
    blog_name=request.form["blog_name"]
    message=request.form["message"]
    message2=blogs.find_text(community,blog_id)
    writer=request.form["blog_writer"]
    time=request.form["blog_time"]
    if password==password1:
        session["blog"]=blog_id
        comments=blogs.find_comments(blog_id)
        comments2=[]
        for i in comments:
            writer_name=blogs.find_comment_writer_name(i[0])
            comments2.append((i[1],writer_name[0],i[3]))
        return render_template("Blog2.html",blog_id=blog_id,community=community,
                                blog_name=blog_name,message=message,comments=comments2,
                                blog_time=time,blog_writer=writer,message2=message2)
    else:
        return render_template("error5.html",
                                passw=password1,blog_id=blog_id,
                                community=community,blog_name=blog_name,
                                message=message,blog_time=time,blog_writer=writer,
                                message3="password wrong, try again!")

@app.route("/new_blog")
def new_blog():
    """show the page where user can write new blog
       returns: Rendered template"""
    session.csrf_token=session["csrf_token"]
    return render_template("new.html" )

@app.route("/create", methods=["POST"])
def create():
    """create a new blog and go back to start page
       returns: rendered templates"""
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    topic = request.form["topic"]
    community=request.form["community"]
    content=request.form["content"]
    check_content_blank=content.strip()
    check_topic_blank=topic.strip()
    if len(check_topic_blank)==0 or len(check_content_blank)==0 or community=="":
        return render_template("error3.html",
           message="topic,community and blog content cannot be blank,"
                    "write something into the box.")
    user1=session["username"]
    userid=blogs.find_userid_by_name(user1)
    blog_password=request.form["password"]
    blogs.create_blog(topic,content,int(userid[0]),community)
    blog_id=blogs.recently_added_blog(userid[0])
    if len(blog_password)!=0:
        blogs.add_blog_password(int(blog_id[0]),blog_password)

    return   render_template("start.html")

@app.route("/add_comment", methods=["POST","GET"])
def add_comment():
    """show add a comment page
       returns:rendered template"""
    community=request.args.get("community")
    blog_id=request.args.get("blog_id")
    blog_name=request.args.get("blog_name")
    return render_template("new_comment.html",
                            community=community,blog_id=blog_id,blog_name=blog_name)

@app.route("/add_comment2", methods=["POST","GET"])
def add_comment2():
    """add a comment can go back to list page
       returns:rendered template"""
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    community=request.form["community"]
    blog_id=request.form["blog_id"]
    content=request.form["query"]
    blog_name=request.form["blog_name"]
    check_blank=content.strip()
    if len(check_blank)==0:
        return render_template("error4.html",community=community,blog_id=blog_id,
                                blog_name=blog_name,
                                message="comment cannot be blank, write something")
    new_content=content.replace('\n', '<br>')
    user1=session["username"]
    userid=blogs.find_userid_by_name(user1)
    blogs.add_comment(blog_id,new_content,userid[0])
    return redirect(f"/Blog2?community={community}&blog_name={blog_name}&blog_id={blog_id}")
@app.route("/all_my_blogs",methods=["POST","GET"])
def all_my_blogs():
    """find all the blogs user has posted
       returns:rendered templates"""
    if request.method=="POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        delete=request.form.getlist("id")
        blogs.delete_blog(delete)
    commu1="school"
    commu2="life"
    commu3="sport"
    commu4="game"
    username=session["username"]
    id1=blogs.find_userid_by_name(username)
    number=blogs.count_user_blog(id1[0])
    time=blogs.user_first_blog(id1[0])
    if time!=None:
        time=time[0]
    admin=blogs.check_if_admin(id1)
    if len(admin)!=0:
        list=blogs.find_all_all_blogs()
        return render_template("all_my_blogs.html",list=list,commu1=commu1,
                                commu2=commu2,commu3=commu3,commu4=commu4,
                                time=time,number=number[0])
    userid=blogs.find_userid_by_name(username)
    list=blogs.all_my_blogs(userid[0])
    return render_template("all_my_blogs.html",list=list,commu1=commu1,
                            commu2=commu2,commu3=commu3,commu4=commu4,
                            time=time,number=number[0])
