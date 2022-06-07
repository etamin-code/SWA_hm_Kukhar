from fastapi import FastAPI
import asyncio
import uvicorn
from pydantic import BaseModel
import requests
from random import choice


messages_url = "http://localhost:8001/"
logging_urls = ["http://localhost:8002/", "http://localhost:8003/", "http://localhost:8004/"]

app = FastAPI()


@app.get("/")
async def get():
    ok = 0
    while not ok:
        try:
            logging_url = choice(logging_urls)
            print(f"trying {logging_url}")
            log_ans = requests.get(logging_url)
            if log_ans.ok:
                ok = 1
            
        except:
            print(f"{logging_url} is disable, trying another")
    msg_ans = requests.get(messages_url)
    return f"{log_ans.text}, {msg_ans.text}"


@app.post("/{msg}")
async def send_msg(msg: str):
    logging_url = choice(logging_urls)
    post_request(logging_url, params={"msg_hash": hash(msg), "msg": msg})
    return msg
    

def post_request(url, params):
    print("sending request to logging")
    return requests.post(url, params=params)

    
    
    
