from typing import List
from app.core.database import db
from app.models.history import TemperaturaHistory

def createTemperaturaHistory(temp: List[TemperaturaHistory]):
    tempDict = []
    for t in temp:
        tempDict.append(t.dict())
    ret = db.history_temperatura.insert_many(tempDict)
    return ret