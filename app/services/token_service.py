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

def getAnyToken():
    ret = db.token.find()
    token = None
    for tok in ret:
        token = tok
    token = Token(_id=token["_id"],token=token["token"])
    return token