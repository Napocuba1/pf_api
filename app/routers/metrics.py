from typing import List, Optional
from fastapi import APIRouter, Depends

from app.models.history import SensoresDataHistory 
from app.services.temperatura_history_service import getTemperaturaHistoryLast
from app.services.riego_history_service import getRiegoHistoryLast
from app.services.luz_history_service import getLuzHistoryLast

from app.services.ph_history_service import getPhHistoryLast
from app.services.aire_history_service import getAireHistoryLast
from app.token import get_api_key
router = APIRouter()


@router.get("/data", response_model=SensoresDataHistory, dependencies=[Depends(get_api_key)])
async def get_sensores_data_history():
    sensores = SensoresDataHistory(
        temperatura= getTemperaturaHistoryLast(),
        riego= getRiegoHistoryLast(),
        luz= getLuzHistoryLast(),
        ph= getPhHistoryLast(),
        aire= getPhHistoryLast(),
    )
    return sensores