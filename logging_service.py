from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import hazelcast
import logging

app = FastAPI()

run_node = f"sudo docker run -d\
    -it \
    --rm \
  hazelcast/hazelcast:5.1.1"

subprocess.call(run_node.split())
logging.basicConfig(level=logging.INFO)
app = FastAPI()

client = hazelcast.HazelcastClient()
my_map = client.get_map("my-distributed-map").blocking()





@app.post("/")
async def post(msg_hash, msg):
    my_map.lock(msg_hash)
    try:
        my_map.put(msg_hash, msg)
        print("logging received a message: " + msg)
    finally:
        my_map.unlock(msg_hash)
    return msg


@app.get("/")
async def get():
    return str(list(my_map.values()))
