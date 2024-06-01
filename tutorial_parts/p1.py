from fastapi import FastAPI


app = FastAPI()


@app.get("/", description="This is our first route.", deprecated=True)
async def base_get_route():
    return {"message": "Hello World!!"}


@app.post("/")
async def post():
    return {"message": "Hello from the post route."}


@app.put("/")
async def put():
    return {"message": "Hello from the put route."}