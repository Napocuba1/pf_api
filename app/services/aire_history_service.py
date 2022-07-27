from typing import List
from app.core.database import db
from app.models.history import AireHistory

def createAireHistory(temp: List[AireHistory]):
    aireDict = []
    for t in temp:
        aireDict.append(t.dict())
    ret = db.history_aire.insert_many(aireDict)
    return ret

def getAireHistoryLast():
    temp = db.history_aire.aggregate([
            { "$sort" : { "date_action" : -1 } },
            { "$limit" : 1 }
            ])
    last = dict()
    for t in temp:
        last = t
    last = AireHistory(**last)
    return last