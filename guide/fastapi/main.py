#f - is field
#m - is method
from typing import  Union
from fastapi import FastAPI
from pydantic import BaseModel

from src.app.services import data_capturer
from src.app.services.data_capturer import URLS


app = FastAPI()
# one post of url and way of capturing to update and fill db
# one get to take field from db
class Metric(BaseModel):
    Name: str
    Descritpion: str
    Value: int

#main domain (no endpoint)
@app.get("/")
def read_root():
    return{"Hello": "This is main metrics page"}

@app.get("/metrics/{item_id}")
def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}

@app.post("/metrics")
async def capture_metrics(url: str):
    data_capturer.URLS = url
    return
#COMMENT



