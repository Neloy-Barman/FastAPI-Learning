from fastapi import FastAPI
from fastapi import Path
from fastapi import Query

app = FastAPI()

# Path parameters and Numeric validations

@app.get("/items_validation/{item_id}")
# async def read_items_validation(q: str, item_id: int =  Path(...)):
# * means all the parameters after this are kwrgs
async def read_items_validation(
    *, 
    item_id: int =  Path(..., description="Item id parameter", gt=10, le=100), 
    q : str = "hello",
    size: float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results
