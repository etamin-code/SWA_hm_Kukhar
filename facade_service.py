from fastapi import FastAPI
import asyncio
import uvicorn
from pydantic import BaseModel
import requests
from random import choice
import hazelcast


logging_urls = ["http://localhost:8003/", "http://localhost:8004/", "http://localhost:8005/"]
messages_urls = ["http://localhost:8001/", "http://localhost:8002/"]


app = FastAPI()

client = hazelcast.HazelcastClient()
q = client.get_queue("my_queue").blocking()


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
    
    ok = 0
    while not ok:
        try:
            messages_url = choice(messages_urls)
            print(f"trying {messages_url}")
            msg_ans = requests.get(messages_url)
            if msg_ans.ok:
                ok = 1    
        except:
            print(f"{messages_url} is disable, trying another")

    return f"{log_ans.text}, {msg_ans.text}"


@app.post("/{msg}")
async def send_msg(msg: str):
    logging_url = choice(logging_urls)
    post_request(logging_url, params={"msg_hash": hash(msg), "msg": msg})
    print("putting message into the queue")
    res = q.put(msg)
    if res:
        print(f"result: {res.result()}.\n")
    return msg
    

def post_request(url, params):
    print("sending request to logging")
    return requests.post(url, params=params)

    
    
    
