from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Hello World GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# GET endpoint with path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# POST data model
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }
