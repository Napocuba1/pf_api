from typing import List
from app.core.database import db
from app.models.history import LuzHistory

def createLuzHistory(temp: List[LuzHistory]):
    luzDict = []
    for t in temp:
        luzDict.append(t.dict())
    ret = db.history_luz.insert_many(luzDict)
    return ret

def getLuzHistoryLast():
    temp = db.history_luz.aggregate([
            { "$sort" : { "date_action" : -1 } },
            { "$limit" : 1 }
            ])
    last = dict()
    for t in temp:
        last = t
    last  = LuzHistory(**last)
    return last