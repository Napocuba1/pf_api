from typing import List
from app.core.database import db
from app.models.history import RiegoHistory

def createRiegoHistory(temp: List[RiegoHistory]):
    riegoDict = []
    for t in temp:
        riegoDict.append(t.dict())
    ret = db.history_riego.insert_many(riegoDict)
    return ret