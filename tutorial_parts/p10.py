from fastapi import Body
from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Declare Request Example Data
'''
    There are many ways to include information about the request body. 
    Let's see one.
'''


class Item(BaseModel):
    name: str 
    description: str | None = None
    price: float
    tax: float | None = None


# # Including one example 
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., example={"name": "foo", "description": "A very nice item.", "price": 16.75, "tax": 1.65})):
#     results = {"item_id": item_id, "item": item}
#     return results


# Including multiple examples 
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        openapi_examples={
            "normal": {
                "summary": "A normal example",
                "description": "A __normal__ item works __correctly__.",
                "value": {
                    "name": "foo", 
                    "description": "A very nice item.", 
                    "price": 16.75, 
                    "tax": 1.65
                }
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically.",
                "value": {
                    "name": "Bar", 
                    "price": "16.75", 
                }
            },
             "Invalid": {
                "summary": "Invalid data gets rejected.",
                "description": "Invalid data throws error.",
                "value": {
                    "name": "Baz", 
                    "price": "Sixteen point two five", 
                }
            }
        }
    )
):
    results = {"item_id": item_id, "item": item}
    return results
