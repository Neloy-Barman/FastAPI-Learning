from enum import Enum
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_base_route():
    return {"message": "Base route path"}


# Path parameters
@app.get("/items")
async def list_items():
    return {"message": "List items route."}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
# If we pass data of any other type, then it will throw error.


# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"message": f"{user_id}"}
#
#
# @app.get("/users/me")
# async def current_user():
#     return {"message": "This is the current user."}

"""
    We want to pass me as the parameter and want the current_user function.
    But if we pass like this, then the me is considered as user_id and is called the get_user_route,
    as the fastapi checks routes in first to last order.
    That's why we have to kee the current_user before the get_user route. 
"""


@app.get("/users/me")
async def current_user():
    return {"message": "This is the current user."}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"message": f"{user_id}"}


# Using specific inputs for path parameter
class FoodEnum(str, Enum):
    fruits = "fru"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):

    print(food_name.fruits.name)

    print(f"Name: {food_name.name}")
    print(f"Value: {food_name.value}")

    if food_name.value == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You are healthy."}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "You are healthy, but like more sweets."
        }

    return {"food_name": food_name, "message": "I like chocolate milk."}



