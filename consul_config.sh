#!/bin/bash

declare -r HOST="localhost"

consul kv put hz_map_node_1 "${HOST}:5701"
consul kv put hz_map_node_2 "${HOST}:5702"
consul kv put hz_map_node_3 "${HOST}:5703"

consul kv put distributed_map_name "hw5_distributed_map"

consul kv put hz_queue_node_1 "${HOST}:5701"
consul kv put hz_queue_node_2 "${HOST}:5702"

consul kv put message_queue_name "hw5_distributed_queue"
