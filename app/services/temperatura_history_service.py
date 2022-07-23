from typing import List
from app.core.database import db
from app.models.history import TemperaturaHistory
from datetime import datetime
from pymongo.collection import ReturnDocument

def create(temp: List[TemperaturaHistory]):
    for t in temp:
        ret = db.history_temperatura.insert_one(t.dict())
    return ret