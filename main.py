from datetime import datetime, timedelta
from typing import Optional, List

from fastapi import FastAPI, Query, status, HTTPException
from fastapi.staticfiles import StaticFiles

from models.models import Item, ItemTwo, \
    UserSignupRequest, UserSignupResponse, \
    UserLoginRequest, UserLoginResponse, \
    JwtData
from middlewares.middlewares import init_middlewares

from passlib.context import CryptContext
import jwt

from models.fake_db import FakeDb
from models.constants import JWT_SECRET_KEY, JWT_EXPIRATION_SECONDS_DEFAULT



fakeDb = FakeDb()

app = FastAPI()

# Initialize middlewares
init_middlewares(app)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get(
    "/",
    tags=["Example"]
)
def read_root():
    return {"Hello": "World"}


@app.get(
    "/items/{item_id}",
    tags=["Example"]
)
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put(
    "/items/{item_id}",
    tags=["Example"]
)
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get(
    "/test/route1",
    tags=["Test"]
)
async def test_route_1():
    return {
        "message": "route_1 Stub!"
    }


@app.get("/test/route2/{path_param_one}", tags=["Test"])
async def test_route_2(
    path_param_one: str,
    query_param_one: Optional[int] = 1999
):
    return {
        "message": {
            "path_param_one": path_param_one,
            "query_param_one": query_param_one
        }
    }


@app.post(
    "/test/create-items/",
    tags=["Test"]
)
async def test_create_item(item: ItemTwo):
    return item


@app.get(
    "/test/read-items/",
    tags=["Test"]
)
async def test_read_items(q: Optional[str] = Query(None, max_length=50, title="This is a title", description="This is a description")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get(
    "/test/required-query-param/",
    tags=["Test"]
)
async def test_required_query_param(q: Optional[str] = Query(..., max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.post(
    "/users/signup/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSignupResponse,
    tags=["Test", "Users"]
)
async def users_signup(body: UserSignupRequest):
    # Check if the username already taken.
    # If already taken, raise 409 Conflict "Username already taken".
    if fakeDb.is_username_existed(body.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already taken")
    # If not,
    #   1. Hash the password.
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    password_hash = pwd_context.hash(body.password)
    #   2. Save to database.
    fakeDb.save_user(**body.dict(), password_hash=password_hash)
    #   3. Return 201 create
    return UserSignupResponse(**body.dict())


@app.post(
    "/users/login/",
    response_model=UserLoginResponse,
    tags=["Test", "Users"]
)
async def users_login(body: UserLoginRequest):
    # Check username and password if existed in the records.
    # If not, raise 401 Unauthorized "Incorrect username or password".
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = fakeDb.get_user(body.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    is_password_matched = pwd_context.verify(body.password, user.get("password_hash"))
    if not is_password_matched:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    # If existed, 
    #   1. Create the expiration time, use JWT_EXPIRATION_SECONDS_DEFAULT as default.
    to_encode = user.copy()
    to_encode.pop("password_hash")  # exclude the hash password
    expiration = datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION_SECONDS_DEFAULT)
    to_encode.update({"expiration": expiration.timestamp()})
    #   2. Generate an access token, include the user's data (w/o the hash password) and the expiration.
    access_token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm="HS256")
    #   3. Return the access token data.
    return UserLoginResponse(access_token=access_token, token_type="bearer")


@app.get(
    "/users/usernames/",
    response_model=List[str],
    tags=["Test", "Users"]
)
async def get_users_usernames():
    return [i.get("username") for i in fakeDb.get_users()]
