from fastapi import FastAPI
import asyncio
import uvicorn
from pydantic import BaseModel
import requests


logging_url = "http://127.0.0.1:8001/"
messages_url = "http://127.0.0.1:8002/"

app = FastAPI()


@app.get("/")
async def get():
    log_ans = requests.get(logging_url)
    msg_ans = requests.get(messages_url)
    return f"{log_ans.text}, {msg_ans.text}"


@app.post("/{msg}")
async def send_msg(msg: str):
    post_request(logging_url, params={"msg_hash": hash(msg), "msg": msg})
    return msg
    

def post_request(url, params):
    print("sending request to logging")
    return requests.post(url, params=params)

    
    
    
