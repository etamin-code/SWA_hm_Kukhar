import argparse
import consul
import hazelcast
from fastapi import FastAPI
import uvicorn

from facade_service import get_data, post_message

app = FastAPI()


@app.get('/')
def get():
    return get_data(consul_service)


@app.post('/{msg}')
def post(msg):
    return post_message(consul_service, q, msg)


if __name__ == "__main__":

    print("started facade service")
    parser = argparse.ArgumentParser(description='Process port number')
    parser.add_argument('--port', type=int)
    args = parser.parse_args()
    port = args.port
    host = "localhost"
    service_name = "facade_service"
    consul_service = consul.Consul(host='localhost', port=8500)
    consul_service.agent.service.register(name=service_name, service_id=service_name + ":" + str(port),
                                          address=host, port=port)

    nodes = ['hz_queue_node_1', 'hz_queue_node_2']
    cluster_members = []
    for node in nodes:
        cluster_members.append(consul_service.kv.get(key=node, index=None)[1]['Value'].decode('utf-8'))

    hz_client = hazelcast.HazelcastClient(cluster_members=cluster_members)
    q_name = consul_service.kv.get(key='message_queue_name', index=None)[1]['Value'].decode('utf-8')
    q = hz_client.get_queue(q_name).blocking()

    uvicorn.run(app, host=host, port=port)
