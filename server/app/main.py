from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name: int
    description: int = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/")
def 