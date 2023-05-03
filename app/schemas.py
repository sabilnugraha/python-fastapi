from pydantic import BaseModel

class Products(BaseModel):
    name: str
    price: int
    inventory: int

class PostCreate(Products):
    pass

class Response(BaseModel):
    name: str
    price: int
    id: int

    class Config:
        orm_mode = True