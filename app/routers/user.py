from ast import Str
from typing import Optional
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/me", response_model=str)
async def get_me():
    return "user"