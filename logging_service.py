from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
messages = {}


@app.post("/")
async def post(msg_hash, msg):
    messages[msg_hash] = msg
    print("logging received a message: " + msg)
    return msg


@app.get("/")
async def get():
    return ', '.join([msg for msg in messages.values()])
