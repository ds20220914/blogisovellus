from db import db
from sqlalchemy import text

def find_all_school_blogname():
    query = text("SELECT Blog_name FROM School")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_Life_blogname():
    query = text("SELECT Blog_name FROM Life")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_sport_blogname():
    query = text("SELECT Blog_name FROM Sport")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def find_all_game_blogname():
    query = text("SELECT Blog_name FROM Game")
    right_blogs = db.session.execute(query)
    blogs=right_blogs.fetchall()
    return blogs

def create_school_blog(topic,content):
    sql =text( "INSERT INTO School (Blog_name, Blog_text) VALUES (:topic, :content)")
    result = db.session.execute(sql, {"topic":topic,"content":content})
    db.session.commit()
