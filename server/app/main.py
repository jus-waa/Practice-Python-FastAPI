from fastapi import FastAPI
from pydantic import BaseModel
from db_config import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
class Item(BaseModel):
    name: int
    description: int = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"Hello" : "World"}
