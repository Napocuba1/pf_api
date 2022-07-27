from typing import List
from app.core.database import db
from app.models.history import TemperaturaHistory
import pymongo
def createTemperaturaHistory(temp: List[TemperaturaHistory]):
    tempDict = []
    for t in temp:
        tempDict.append(t.dict())
    ret = db.history_temperatura.insert_many(tempDict)
    return ret


def getTemperaturaHistoryLast():
    temp = db.history_temperatura.aggregate([
            { "$sort" : { "date_action" : -1 } },
            { "$limit" : 1 }
            ])
    print(temp)
    last = dict()
    for t in temp:
        last = t
    last = TemperaturaHistory(**last)
    return last