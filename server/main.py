from fastapi import FastAPI
from  helpers import *
app = FastAPI()

@app.get("/")
async def root():
    payload = "Today I enjoyed using blocks in math class because it made a lot of sense. Math on the white board is boring because I can't see"
    result = query(payload)
    required_response = result["choices"]
    return required_response