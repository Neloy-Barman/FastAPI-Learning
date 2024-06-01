from fastapi import Body
from fastapi import Path
from fastapi import Query
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Body - Multiple Parameters

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    user_name: str
    full_name: str | None = None

# class Importance(BaseModel):
#     importance: int
# Only for one body parameter it's not optimal to declare a class
# In that case, we can use Body()

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., ge=0, le=150),
    # item : Item | None = None,
    # For key-value pair input
    item: Item = Body(..., embed=True),
    q: str = Query("Hello"),
    user: User | None = None,
    importance: int = Body(None)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})
    if user:
        results.update({"user" : user})
    if importance:
        results.update({"importance" : importance})
    return results
