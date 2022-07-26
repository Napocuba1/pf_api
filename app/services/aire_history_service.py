from typing import List
from app.core.database import db
from app.models.history import AireHistory

def createAireHistory(temp: List[AireHistory]):
    aireDict = []
    for t in temp:
        aireDict.append(t.dict())
    ret = db.history_aire.insert_many(aireDict)
    return ret