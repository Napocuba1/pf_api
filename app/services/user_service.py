from typing import List
from app.core.database import db
from app.models.user import User
def searchUser(email: str):
    ret = db.user.find_one({"email": email})
    if ret is not None:
        user = User(_id=ret["_id"],email=ret["email"], name=ret["email"], password=ret["password"])
        return user
    else:
        return None
        
def registerUser(user: User):
    ret = db.user.insert_one({"name": user.name, "password": user.password, "email": user.email})
    print (ret)
    return ret