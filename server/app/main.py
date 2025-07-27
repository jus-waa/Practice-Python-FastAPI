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

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None, sample: bool = False):
    item = {"item_id": item_id}
    item.update({"q": q})
    return {item}

