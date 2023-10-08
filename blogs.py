from db import db
from sqlalchemy import text

def find_all_school_blogname():
    query = text("SELECT Blog_name,id FROM School")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Life_blogname():
    query = text("SELECT Blog_name,id FROM Life")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_sport_blogname():
    query = text("SELECT Blog_name,id FROM Sport")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_game_blogname():
    query = text("SELECT Blog_name,id FROM Game")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def create_school_blog(topic,content):
    sql =text( "INSERT INTO School (Blog_name, Blog_text) VALUES (:topic, :content)")
    result = db.session.execute(sql, {"topic":topic,"content":content})
    db.session.commit()

def find_text(community,id ):
    if community=="1":
        query = text("SELECT Blog_text FROM School WHERE id=:id")
        right_blogs = db.session.execute(query,{"id":id})
        blog=right_blogs.fetchone()
        return blog

def find_all_school_blog_byname(name):
    query = text("SELECT Blog_name FROM School WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Life_blog_byname(name):
    query = text("SELECT Blog_name FROM Life WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Sport_blog_byname(name):
    query = text("SELECT Blog_name FROM Sport WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Game_blog_byname(name):
    query = text("SELECT Blog_name FROM Game WHERE Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"Blog_name":name})
    blogs=right_blogs.fetchall()
    return blogs

def add_comment(community,id,content):
    if community=="1":
        query = text(" INSERT INTO School_comment (Blog_id,content) VALUES (:id , :content)")
        right_blogs = db.session.execute(query,{"id":id, "content":content})

def find_comments(community,id):
    if community=="1":
        query = text(" SELECT content FROM School_comment WHERE Blog_id=:id ")
        right_comments = db.session.execute(query,{"id":id})
        comments=right_comments.fetchall()
        return comments
