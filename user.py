from db import db
from sqlalchemy import text

def login(username1,password1):
    query = text("SELECT * FROM users WHERE username=:username1 AND password=:password1")
    right_user = db.session.execute(query, {"username1": username1, "password1": password1})
    number=right_user.fetchall()
    sign_in=False
    if len(number)==0:
        return False
    if len(number)!=0:
        return True


