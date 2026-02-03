#f - is field
#m - is method
from typing import  Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
#COMMENT



