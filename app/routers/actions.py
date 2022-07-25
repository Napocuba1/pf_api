from ast import Str
from typing import List, Optional
from fastapi import APIRouter, Depends
from app.token import get_api_key
from datetime import datetime
from app.services.petition_service  import insert_petition, get_petitions_fisico
from app.models.result import Result
from app.models.petition import Petition
router = APIRouter()


temp = False

@router.post("/toogle/temperatura", response_model=Result, dependencies=[Depends(get_api_key)])
async def toogle_temperatura(sw: bool):
    petition = Petition( types="temperatura", action=sw, state=1, date_action=datetime.now(), ttl=300)
    insert_petition(petition=petition)
    return Result(code=1, message="Peticion de temperatura registrada")
    
@router.post("/toogle/riego", response_model=Result, dependencies=[Depends(get_api_key)])
async def toogle_riego(sw: bool):
    petition = Petition( types="riego", action=sw, state=1, date_action=datetime.now(), ttl=300)
    insert_petition(petition=petition)
    return Result(code=1, message="Peticion de riego registrada")

@router.post("/toogle/luz", response_model=Result, dependencies=[Depends(get_api_key)])
async def toogle_luz(sw: bool):
    petition = Petition( types="luz", action=sw, state=1, date_action=datetime.now(), ttl=300)
    insert_petition(petition=petition)
    return Result(code=1, message="Peticion de luz registrada")




@router.get("/petitions", response_model=List[Petition], dependencies=[Depends(get_api_key)])
async def obtain_petitions_fisico():
    petitions = get_petitions_fisico()
    return petitions