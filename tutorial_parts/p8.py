from fastapi import Body
from fastapi import Path
from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Body - Field
# Using field we can view the basemodel schema in the documentation

class Item(BaseModel):
    name: str
    description: str | None = Field(None, 
                                    description = "The description of the item", 
                                    max_length = 300
                                    )
    price: float = Field(..., 
                         gt=0, 
                         description="The  price must be greater than zero."
                         )
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., ge=0, le=150),
    item: Item = Body(..., embed=True)
):
    results = {"item_id": item_id, "item": item}
    return results
