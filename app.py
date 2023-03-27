from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

class Item(BaseModel):
    id: int
    name: str

items = []

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
