from fastapi import FastAPI
from fastapi import Query
from typing import Optional

app = FastAPI()

# Query Parameters and String Validations

'''
    min_length
    max_length
    regex

'''

# Adding min_length, max_length or regex
# async def read_items(q: str | None = Query(None, min_length=3, max_length=10, regex="^fixedquery$")):

# Defalt value for query
# async def read_items(q: str = Query("fixedquery", min_length=3, max_length=10)):

# Required query
# async def read_items(q: str = Query(..., min_length=3, max_length=10)):

# Multiple query parameters
# async def read_items(q: list[str] | None = Query(None)):

# Default Multiple query parameters
# async def read_items(q: list[str] = Query(['foo', 'bar'])):
# http://127.0.0.1:8000/items?q=aaaaa&q=bbbb&q=ccdfsdf ✅

# Adding title
# async def read_items(q: str | None  = Query(None, title="This is a simple query.", description="This is a simple query.")):

# Aliasing the query parameter
@app.get("/items")
async def read_items(q: str | None  = Query(None, title="This is a simple query.", description="This is a simple query.", alias="item-query")):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results
# http://127.0.0.1:8000/items?item-query=aaaaa ✅
# http://127.0.0.1:8000/items?q=aaaaa ❌


# Hidden query
@app.get("/items/hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}
# http://127.0.0.1:8000/items/hidden?hidden_query=dfasdfads ✅