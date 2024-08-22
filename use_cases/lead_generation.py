from fastapi import FastAPI
from  typing import Optional
from pydantic import BaseModel

app = FastAPI()

class LeadData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

@app.post("/", description="Lead Generation Endpoint")
async def post_data(lead_data: LeadData):

    data_dict = lead_data.model_dump()
    
    return {
        "message": "Data added.", 
        "Data": data_dict
    }