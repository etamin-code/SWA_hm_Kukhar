#!/bin/bash

#commands with uvicorn and docker run must be run in different terminals

sudo docker network create hazelcast-network

sudo docker run -p 5701:5701 hazelcast/hazelcast:5.1.1

uvicorn facade_service:app --host=localhost --port=8000
uvicorn message_service:app --host=localhost --port=8001
uvicorn logging_service:app --host=localhost --port=8002
uvicorn logging_service:app --host=localhost --port=8003
uvicorn logging_service:app --host=localhost --port=8004

bash post_requests.sh
bash get_request.sh


