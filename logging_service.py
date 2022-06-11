import argparse
import consul
import hazelcast
from fastapi import FastAPI
import uvicorn



app = FastAPI()


@app.get('/logging_service/')
def get():
    return str(list(messages.values()))


@app.post("/logging_service/")
async def post(msg_hash, msg):
    print(f"logging received a message {msg}")
    messages.put(msg_hash, msg)
    return {"statusCode": 200}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process port number')
    parser.add_argument('--port', type=int)
    args = parser.parse_args()
    port = args.port
    host = "localhost"
    service_name = "logging_service"
    consul_service = consul.Consul(host='localhost', port=8500)
    consul_service.agent.service.register(name=service_name, service_id=service_name + ":" + str(port),
                                          address=host, port=port)

    nodes = ['hz_map_node_1', 'hz_map_node_2', 'hz_map_node_3']
    cluster_members = []
    for node in nodes:
        cluster_member = consul_service.kv.get(key=node, index=None)[1]['Value'].decode('utf-8')
        cluster_members.append(cluster_member)
    hz_client = hazelcast.HazelcastClient(cluster_members=cluster_members)

    distributed_map_name = consul_service.kv.get(key='distributed_map_name', index=None)[1]['Value'].decode('utf-8')
    messages = hz_client.get_map(distributed_map_name).blocking()

    uvicorn.run(app, host=host, port=port)