import argparse
import hazelcast
import consul
import threading
from fastapi import FastAPI
import uvicorn


app = FastAPI()
messages = []


@app.get('/message_service')
def get():
    if len(messages) == 0:
        return "messages service has no messages"
    else:
        return "[" + ", ".join(messages) + "]"


def initialize_queue(consul_service, hz_client):
    distributed_queue_name = consul_service.kv.get(key='message_queue_name', index=None)[1]['Value'].decode('utf-8')
    distributed_queue = hz_client.get_queue(distributed_queue_name).blocking()
    return distributed_queue

def post_messages(consul_service, hz_client):
    distributed_queue = initialize_queue(consul_service, hz_client)
    while True:
        message = distributed_queue.take()
        print(f"posted {message}")
        messages.append(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process port number')
    parser.add_argument('--port', type=int)
    args = parser.parse_args()
    port = args.port

    host = "localhost"
    service_name = "message_service"
    consul_service = consul.Consul(host='localhost', port=8500)
    consul_service.agent.service.register(name=service_name, service_id=service_name + ":" + str(port),
                                          address=host, port=port)

    nodes = ['hz_queue_node_1', 'hz_queue_node_2']
    cluster_members = []
    for node in nodes:
        cluster_members.append(consul_service.kv.get(key=node, index=None)[1]['Value'].decode('utf-8'))
    hz_client = hazelcast.HazelcastClient(cluster_members=cluster_members)

    threading.Thread(target=post_messages, args=(consul_service, hz_client), daemon=True).start()

    uvicorn.run(app, host=host, port=port)
