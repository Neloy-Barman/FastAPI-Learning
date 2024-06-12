from fastapi import Header
from fastapi import Cookie
from fastapi import FastAPI

app = FastAPI()

# Cookie and Header Parameters

@app.get("/items")
async def read_items(
    cookie_id: str | None = Cookie(None),
    user_agent: str | None = Header(None),
    accept_encoding: str | None = Header(None),
    accept_language: str | None = Header(None),
    x_token: list[str] | None = Header(None)
):
    return {
        "cookie_id": cookie_id, 
        "Accept-Encoding": accept_encoding, 
        "Accept-Language": accept_language, 
        "User-Agent": user_agent,
        "X-Token values": x_token
    }
# The header parameters such as Accept-Encoding, Accept-Languauge and User-Agent are fetched from Inspect->Network.
'''
    We didn't pass the exact header parameters but with underscores. 
    Still it's converting it to main header parameters and showing the exact results for us.
    If we make convert_underscores in Header is False, then it won't get us the header parameter values in response.
    X-Token values let us to pass multiple values to reqeust.
'''
