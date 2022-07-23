from ast import Str
from typing import List, Optional
from fastapi import APIRouter, Depends
from app.token import get_api_key
import random
router = APIRouter()


temp = False

@router.get("/toogle/temperatura", response_model=bool, dependencies=[Depends(get_api_key)])
async def toogle_temperatura(sw: bool):
    temp = not sw
    return not sw
@router.get("/toogle/temperatura/actual", response_model=bool, dependencies=[Depends(get_api_key)])
async def toogle_temperatura():
    return bool(random.getrandbits(1))
