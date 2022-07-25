from typing import Optional
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

class Petition(BaseModel):
    _id: Optional[str]
    types: Optional[str] # "luz", "temperatura", "riego"
    action: Optional[bool] = False
    state: Optional[int] # 1: Pendiente, 2: Ejecutado, 3:Cancelado, 4:Perdido
    date_action: datetime = datetime.now()
    ttl: int = 300 #300 segundos de vida
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }