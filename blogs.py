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


