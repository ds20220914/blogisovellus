from db import db
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def login(username1,password1):
    if len(username1)==0 or len(password1) ==0:
        return False
    query = text("SELECT * FROM users WHERE username=:username1")
    right_user = db.session.execute(query, {"username1": username1})
    number=right_user.fetchone()
    sign_in=False
    if len(number)==0:
        return False
    if len(number)!=0:
        hash_value=number.password
        if check_password_hash(hash_value, password1):
            session["username"]=username1
            return True
    return False

def new_user(username,password):
    if len(password)<5:
        return False
    query = text("SELECT * FROM users WHERE username=:username1")
    right_user = db.session.execute(query, {"username1": username})
    number=right_user.fetchall()
    if len(number)>0:
        return False
    hash_value = generate_password_hash(password)
    query = text("INSERT INTO users (username,password) VALUES (:username,:password)")
    right_user = db.session.execute(query, {"username": username, "password": hash_value})
    db.session.commit()
    return True
