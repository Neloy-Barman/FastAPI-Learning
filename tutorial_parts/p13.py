from typing import Literal
from fastapi import FastAPI
from pydantic import EmailStr
from pydantic import BaseModel


app = FastAPI()

# Response Model


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    # tax: float | None = None
    tax: float = 10.5
    tags: list[str] = []


# @app.post("/items")
@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item

'''
    As we are not telling fastapi, what the respnse model is, 
    it's just showing string in the example or schema in swagger documentation.
'''

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user
'''
    We are passing the password to the response, which should not be.
    That's why this should be handled.
'''
class UserBase(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
'''
    As we passed the basemodel as the response_model parameter in the route, 
    now we can see the schema or example value in the fastapi documentation.
'''

items = {
    "foo": {
        "name": "Foo",
        "price": 50.2
    },
     "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2
    },
     "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": []
    },
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["foo", "bar", "baz"]):
# Literal means the parameter has to be from one of these items.
    return items[item_id]

'''
    If we set response_model_exclude_unset = True, then it will only show the passed
    attributes in the response. If it's set False, then it will show all the attributes
    from the base model.
'''

@app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]

'''
    If we want to include or exclude fields from the response model, then
    we can set response_model_include, response_model_exclude True or False
    according to need.
'''

