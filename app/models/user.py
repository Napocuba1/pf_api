from typing import Optional
from bson import ObjectId
from pydantic import BaseModel

class User(BaseModel):
    _id: Optional[str]
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }