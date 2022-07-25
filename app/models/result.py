from typing import Optional
from pydantic import BaseModel

class Result(BaseModel):
    code: Optional[int]
    message: Optional[str]