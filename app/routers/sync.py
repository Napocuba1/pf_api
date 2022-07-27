from typing import List, Optional
from fastapi import APIRouter, Depends

from app.models.history import RiegoHistory, TemperaturaHistory, LuzHistory, PhHistory, AireHistory
from app.services.temperatura_history_service import createTemperaturaHistory
from app.services.riego_history_service import createRiegoHistory
from app.services.luz_history_service import createLuzHistory
from app.services.ph_history_service import createPhHistory
from app.services.aire_history_service import createAireHistory

from app.token import get_api_key
router = APIRouter()


@router.post("/temperatura/data", response_model=str, dependencies=[Depends(get_api_key)])
async def temperatura_upload_online_history( item: List[TemperaturaHistory]):
    print (item)
    result = createTemperaturaHistory(item)
    return str(result)
    
@router.post("/riego/data", response_model=str, dependencies=[Depends(get_api_key)])
async def riego_upload_online_history( item: List[RiegoHistory]):
    print (item)
    result = createRiegoHistory(item)
    return str(result)

@router.post("/luz/data", response_model=str, dependencies=[Depends(get_api_key)])
async def luz_upload_online_history( item: List[LuzHistory]):
    print (item)
    result = createLuzHistory(item)
    return str(result)

@router.post("/ph/data", response_model=str, dependencies=[Depends(get_api_key)])
async def ph_upload_online_history( item: List[PhHistory]):
    print (item)
    result = createPhHistory(item)
    return str(result)

@router.post("/aire/data", response_model=str, dependencies=[Depends(get_api_key)])
async def aire_upload_online_history( item: List[AireHistory]):
    print (item)
    result = createAireHistory(item)
    return str(result)