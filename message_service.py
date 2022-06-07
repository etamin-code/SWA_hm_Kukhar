from fastapi import FastAPI
import hazelcast

app = FastAPI()
client = hazelcast.HazelcastClient()
q = client.get_queue("my_queue").blocking()
messages = []

    
@app.get("/")
async def get():
    while not q.is_empty():
        value = q.take()
        if not value:
            continue
        messages.append(value)
        print(f"messages_service get {value}")
    return ', '.join(messages)
