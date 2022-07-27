from typing import List
from app.core.database import db
from app.models.history import PhHistory

def createPhHistory(temp: List[PhHistory]):
    phDict = []
    for t in temp:
        phDict.append(t.dict())
    ret = db.history_ph.insert_many(phDict)
    return ret

def getPhHistoryLast():
    temp = db.history_ph.aggregate([
            { "$sort" : { "date_action" : -1 } },
            { "$limit" : 1 }
            ])
    last = dict()
    for t in temp:
        last = t
    last = PhHistory(**last)
    return last