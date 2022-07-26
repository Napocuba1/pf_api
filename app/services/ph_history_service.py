from typing import List
from app.core.database import db
from app.models.history import PhHistory

def createPhHistory(temp: List[PhHistory]):
    phDict = []
    for t in temp:
        phDict.append(t.dict())
    ret = db.history_ph.insert_many(phDict)
    return ret