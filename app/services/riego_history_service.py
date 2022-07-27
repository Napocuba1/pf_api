from typing import List
from app.core.database import db
from app.models.history import RiegoHistory

def createRiegoHistory(temp: List[RiegoHistory]):
    riegoDict = []
    for t in temp:
        riegoDict.append(t.dict())
    ret = db.history_riego.insert_many(riegoDict)
    return ret


def getRiegoHistoryLast():
    temp = db.history_riego.aggregate([
            { "$sort" : { "date_action" : -1 } },
            { "$limit" : 1 }
            ])
    last = dict()
    for t in temp:
        last = t
    last  = RiegoHistory(**last)
    return last