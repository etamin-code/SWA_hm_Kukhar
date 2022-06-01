#!/bin/bash

sudo docker network create hazelcast-network

sudo docker run -d\
    -it \
    --network hazelcast-network \
    --rm \
    -e HZ_CLUSTERNAME=my_cluster \
    -p 5701:5701 hazelcast/hazelcast:5.1.1
    
sudo docker run -d\
    -it \
    --network hazelcast-network \
    --rm \
    -e HZ_CLUSTERNAME=my_cluster \
    -p 5702:5701 hazelcast/hazelcast:5.1.1

sudo docker run -d \
    -it \
    --network hazelcast-network \
    --rm \
    -e HZ_CLUSTERNAME=my_cluster \
    -p 5703:5701 hazelcast/hazelcast:5.1.1
    
sudo docker run -d \
    --network hazelcast-network \
    -p 8080:8080 hazelcast/management-center:latest-snapshot
