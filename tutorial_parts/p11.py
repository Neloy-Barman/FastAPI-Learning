from uuid import UUID
from pydantic import Field
from fastapi import FastAPI
from datetime import datetime
from datetime import timedelta
from pydantic import BaseModel


app = FastAPI()

# Extra Data Types
'''
    There are different kinds of field types in pydantic.
    Check it out all from here: https://docs.pydantic.dev/1.10/usage/types/
'''

class Timing(BaseModel):
    start_date: datetime | None = Field(None)
    end_date: datetime | None = Field(None)
    process_after: timedelta | None = Field(None)


# UUID = b745f314-74e7-4f99-9f7b-8ee1f051c8ec
@app.put("/items/{item_id}")
async def read_items(item_id: UUID, timing: Timing):
    timing_dict = timing.model_dump()
    start_process = timing_dict['start_date'] + timing_dict['process_after']
    duration = timing_dict['end_date'] - start_process
    timing_dict.update({'start_process': start_process, "duration": duration})
    results = {"item_id": item_id, "timing": timing_dict}
    return results