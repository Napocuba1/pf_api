from typing import Union

from fastapi import FastAPI
from app.routers import user, sync, actions
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(sync.router, prefix="/fisico", tags=["Dispositivo Fisico"])
app.include_router(actions.router, prefix="/remote", tags=["Dispositivo Fisico"])