from db import db
from sqlalchemy import text


def find_all_school_blogname():
    query = text("SELECT blog_name,id FROM school")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Life_blogname():
    query = text("SELECT blog_name,id FROM life")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_sport_blogname():
    query = text("SELECT blog_name,id FROM sport")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_game_blogname():
    query = text("SELECT blog_name,id FROM game")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def create_school_blog(topic,content,writer):
    sql =text( "INSERT INTO school (blog_name, content,time,writer) VALUES (:topic, :content,NOW(),:writer)")
    result = db.session.execute(sql, {"topic":topic,"content":content,"writer":writer})
    db.session.commit()

def find_text(community,id ):
    if community=="1":
        query = text("SELECT content FROM school WHERE id=:id")
        right_blogs = db.session.execute(query,{"id":id})
        blog=right_blogs.fetchone()
        return blog
    if community=="2":
        query = text("SELECT content FROM life WHERE id=:id")
        right_blogs = db.session.execute(query,{"id":id})
        blog=right_blogs.fetchone()
        return blog
    if community=="3":
        query = text("SELECT content FROM sport WHERE id=:id")
        right_blogs = db.session.execute(query,{"id":id})
        blog=right_blogs.fetchone()
        return blog

    if community=="4":
        query = text("SELECT content FROM game WHERE id=:id")
        right_blogs = db.session.execute(query,{"id":id})
        blog=right_blogs.fetchone()
        return blog

def find_all_school_blog_byname(name):
    query = text("SELECT blog_name FROM school WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Life_blog_byname(name):
    query = text("SELECT blog_name FROM life WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Sport_blog_byname(name):
    query = text("SELECT blog_name FROM sport WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Game_blog_byname(name):
    query = text("SELECT blog_name FROM game WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def add_comment(community,id,content):
    if community=="1":
        query = text(" INSERT INTO school_comment (Blog_id,content) VALUES (:id , :content)")
        right_blogs = db.session.execute(query,{"id":id, "content":content})

def find_comments(community,id):
    if community=="1":
        query = text(" SELECT content FROM school_comment WHERE Blog_id=:id ")
        right_comments = db.session.execute(query,{"id":id})
        comments=right_comments.fetchall()
        return comments
def all_my_blogs(username):
    list=[]
    query1 = text("SELECT * FROM school WHERE writer=:writer")
    right_blogs1 = db.session.execute(query1,{"writer":username})
    query2 = text("SELECT * FROM life WHERE writer=:writer")
    right_blogs2 = db.session.execute(query2,{"writer":username})
    query3 = text("SELECT * FROM sport WHERE writer=:writer")
    right_blogs3 = db.session.execute(query3,{"writer":username})
    query4 = text("SELECT * FROM game WHERE writer=:writer")
    right_blogs4 = db.session.execute(query4,{"writer":username})
    blogs1=right_blogs1.fetchall()
    blogs2=right_blogs2.fetchall()
    blogs3=right_blogs3.fetchall()
    blogs4=right_blogs4.fetchall()
    if len(blogs1)==0:
        list.append([])
    if len(blogs1)!=0:
        list.append(blogs1)
    if len(blogs2)==0:
        list.append([])
    if len(blogs2)!=0:
        list.append(blogs1)
    if len(blogs3)==0:
        list.append([])
    if len(blogs3)!=0:
        list.append(blogs1)
    if len(blogs4)==0:
        list.append([])
    if len(blogs4)!=0:
        list.append(blogs1)
    return list
