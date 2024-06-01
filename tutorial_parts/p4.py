from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Request Body

# We can think of this as a dictionary or the class. We just have to declare the attributes for the class.
class Item(BaseModel):
    name: str
    # We want to make the dictionary and tax optional. There are 2 ways of doing this.
    description: Optional[str] = None
    price: int
    tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     return item

# If we have a trailing comma in the json file, then it's invalid.

@app.post("/items")
async def create_item(item: Item):
    # Converting the model to a dictionary
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict    

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result =  {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result