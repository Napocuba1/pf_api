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
    state: Optional[bool]
    sync: Optional[bool]

class RiegoHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    interval: Optional[str]
    state: Optional[bool]
    flow: Optional[float]
    sync: Optional[bool]

class LuzHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    interval: Optional[str]
    state: Optional[bool]
    sync: Optional[bool]

class PhHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    ph_ideal: Optional[float]
    ph_actual: Optional[float]
    sync: Optional[bool]

class AireHistory(BaseModel):
    _id: Optional[str]
    date_action: datetime
    agent: Optional[str]
    aire_ideal: Optional[float]
    aire_actual: Optional[float]
    sync: Optional[bool]