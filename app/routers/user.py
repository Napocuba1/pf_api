from ast import Str
from typing import Optional
from fastapi import APIRouter, Depends

from app.models.user import User
from app.models.result import Result
from passlib.context import CryptContext
from app.token import get_api_key
from app.services.user_service import searchUser, registerUser
from app.services.token_service import getAnyToken
router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/me", response_model=str, dependencies=[Depends(get_api_key)])
async def get_me():
    return "user"

@router.post("/login", response_model=Result)
async def login(email: str, password: str):
    user = searchUser(email)
    if user is None:
        return Result(code=0, message="Usuario no encontrado")
    if not pwd_context.verify(password, user.password):
        return Result(code=0, message="Contraseña o usuario no válido")
    token = getAnyToken()
    if token is None:
        return Result(code=0, message="Token de sistema no encontrado")
    else:
        return Result(code=1, message=token.token)

@router.post("/register", response_model=Result)
async def register(name: str, email: str, password: str):
    user = searchUser(email)
    if user is not None:
        return Result(code=0, message="Usuario ya existente")
    hashed = pwd_context.hash(password)
    newUser = User(name=name, email=email, password=hashed)
    registerUser(newUser)
    return Result(code=1, message="Usuario Registrado")