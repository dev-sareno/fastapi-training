from typing import Optional

from fastapi import FastAPI, Query, status

from models.models import Item, ItemTwo, \
    UserSignupRequest, UserSignupResponse, \
    UserLoginRequest, UserLoginResponse, \
    JwtData

from models.fake_db import FakeDb



fakeDb = FakeDb()

app = FastAPI()


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
async def test_route_2(path_param_one: str, query_param_one: Optional[int] = 1999):
    return {
        "message": {
            "path_param_one": path_param_one,
            "query_param_one": query_param_one
        }
    }


@app.post("/test/create-items/")
async def test_create_item(item: ItemTwo):
    return item


@app.get("/test/read-items/")
async def test_read_items(q: Optional[str] = Query(None, max_length=50, title="This is a title", description="This is a description")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/test/required-query-param/")
async def test_required_query_param(q: Optional[str] = Query(..., max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.post("users/signup/", status_code=status.HTTP_201_CREATED, response_model=UserSignupResponse)
async def users_signup(body: UserSignupRequest):
    # Check if the username already taken.
    # If already taken, raise 409 Conflict "Username already taken"
    # If not,
    #   1. Hash the password.
    #   2. Save to database.
    #   3. Return 201 create
    return {}


@app.post("/users/login/", response_model=UserLoginResponse)
async def users_login(body: UserLoginRequest):
    # Check if username existed in the records.
    # If not, raise 401 Unauthorized.
    # If existed, return the token (JwtData).
    return {}
