from typing import List
from app.core.database import db
from app.models.history import LuzHistory

def createLuzHistory(temp: List[LuzHistory]):
    luzDict = []
    for t in temp:
        luzDict.append(t.dict())
    ret = db.history_luz.insert_many(luzDict)
    return ret