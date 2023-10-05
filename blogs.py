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

def find_text(name,id ):
    query = text("SELECT Blog_text FROM School WHERE id=:id AND Blog_name=:Blog_name")
    right_blogs = db.session.execute(query,{"id":id,"Blog_name":name})
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

