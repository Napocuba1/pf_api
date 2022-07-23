from ast import Str
from typing import List, Optional
from fastapi import APIRouter, Depends

from app.models.history import RiegoHistory, TemperaturaHistory
from app.services.temperatura_history_service import create as create_temp
from app.services.riego_history_service import create as create_riego

from app.token import get_api_key
router = APIRouter()


@router.post("/temperatura/data", response_model=str, dependencies=[Depends(get_api_key)])
async def upload_online( item: List[TemperaturaHistory]):
    print (item)
    result = create_temp(item)
    return str(result)
    
@router.post("/riego/data", response_model=str, dependencies=[Depends(get_api_key)])
async def upload_online( item: List[RiegoHistory]):
    print (item)
    result = create_riego(item)
    return str(result)