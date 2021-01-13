from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/test/route1")
async def test_route_1():
    return {
        "message": "route_1 Stub!"
    }


@app.get("/test/route2/{path_param_one}")
async def test_route_2(path_param_one: str, query_param_one: Optional[int] = None):
    return {
        "message": {
            "path_param_one": path_param_one,
            "query_param_one": query_param_one
        }
    }