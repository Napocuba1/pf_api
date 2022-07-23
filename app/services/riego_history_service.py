from typing import List
from app.core.database import db
from app.models.history import RiegoHistory
from datetime import datetime
from pymongo.collection import ReturnDocument

def create(temp: List[RiegoHistory]):
    for t in temp:
        ret = db.history_riego.insert_one(t.dict())
    return ret