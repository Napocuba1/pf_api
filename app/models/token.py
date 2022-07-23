from typing import Optional
from bson import ObjectId
from pydantic import BaseModel

class Token(BaseModel):
    _id: Optional[str]
    token: Optional[str]
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }