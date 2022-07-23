from typing import List
from app.core.database import db
from app.models.token import Token
def search(token: str):
    print (token)
    ret = db.token.find_one({"token": token})
    if ret is not None:
        token = Token(_id=ret["_id"],token=ret["token"])
        return token
    else:
        return ret