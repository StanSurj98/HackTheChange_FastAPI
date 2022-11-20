import requests
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

    # Parsing the "text" string from OpenAI
    text = required_response[0]["text"].replace("\n\n", "")
    list = text.split("|")
    list_stripped = [item.strip() for item in list]

    # Creating JSON object for Express API server
    description = {
        "method": list_stripped[0],
        "feeling": list_stripped[1],
        "sentiment": list_stripped[2], 
        "reason": list_stripped[3], 
    }

    json_result = { 
        "pollId": req_body["pollId"], 
        "userId": req_body["userId"], 
        "response": req_body["response"], 
        "description": description 
    }
    print(json_result)
    requests.post("http://localhost:3000/api/responses", json = json_result)
    return json_result