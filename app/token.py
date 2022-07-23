from fastapi import Depends, HTTPException, Security, status

from fastapi.security.api_key import APIKeyHeader
from fastapi.security import OAuth2PasswordBearer
from app.services import token_service

API_KEY_NAME = "Authorization"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)
async def get_api_key(api_key: str = Security(api_key_header)):
    api_key = api_key.replace("Bearer ","",1)
    token = token_service.search(api_key)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )