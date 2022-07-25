from typing import List
from app.core.database import db
from app.models.petition import Petition
from datetime import datetime
from bson.objectid import ObjectId

def insert_petition(petition: Petition):
    actual = db.petition.find_one({"types":petition.types, "state":1})
    if actual is not None:
        db.petition.find_one_and_update({"types":petition.types, "state":1},{"$set":{"state":3}}) # Cancelado
    db.petition.insert_one({"types":petition.types, "state":petition.state, "action": petition.action, "date_action": petition.date_action,  "ttl": petition.ttl}) # Vigentes


def get_petitions_fisico():
    petitions = db.petition.find({"state":1})
    vigentes = []
    fecha_actual = datetime.now()
    for petition in petitions:
        fecha_peticion = petition["date_action"]
        segundos = (fecha_actual - fecha_peticion).total_seconds()
        if (segundos > petition["ttl"]): 
            #Peticion Vencida
            db.petition.find_one_and_update({"_id":ObjectId(petition["_id"])},{"$set":{"state":4}}) # Perdidos
        else:
            #Peticion vigente
            vigentes.append(Petition(**petition))
            db.petition.find_one_and_update({"_id":ObjectId(petition["_id"])},{"$set":{"state":2}}) # Ejecutados
    return vigentes