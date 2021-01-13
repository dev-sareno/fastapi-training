from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class ItemTwo(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class UserSignupRequest(BaseModel):
    username: str  # email
    password: str = Field(..., min_length=6)
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)


class UserSignupResponse(BaseModel):
    username: str  # email
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str


class JwtData(BaseModel):
    username: str  # email
    first_name: str
    last_name: str

