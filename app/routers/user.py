from ast import Str
from typing import Optional
from fastapi import APIRouter, Depends

from app.token import get_api_key
router = APIRouter()


@router.get("/me", response_model=str, dependencies=[Depends(get_api_key)])
async def get_me():
    return "user"