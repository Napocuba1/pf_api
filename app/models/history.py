from datetime import datetime
from typing import List, Literal, Optional
from pydantic import BaseModel
from pydantic.fields import Field


class TemperaturaHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    temperatura_ideal: Optional[float]
    temperatura_actual: Optional[float]
    state: Optional[str]
    sync: Optional[bool]

class RiegoHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    interval: Optional[str]
    state: Optional[str]
    flow: Optional[float]
    sync: Optional[bool]