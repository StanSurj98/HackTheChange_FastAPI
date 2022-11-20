from fastapi import Request, FastAPI
from  helpers import *
app = FastAPI()

@app.post("/{userId}/polls/{pollId}")
async def get_body(request: Request):
    print("Line12 main.py")
    req_body = await request.json()
    payload = req_body["response"]
    result = query(payload)
    required_response = result["choices"]
    #required_response2 = required_response["text"].replace("\n\n", "")
    
    print(required_response[0]["text"])

    return required_response