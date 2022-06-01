import hazelcast
import time

client = hazelcast.HazelcastClient(cluster_name="my_cluster")

print("Starting")

my_map = client.get_map("my-distributed-map")

key = "1"
value = "0"
my_map.put_if_absent(key, value)
	
for i in range(1000):
    value = my_map.get(key)
    time.sleep(0.01)
    value = str(int(value.result()) + 1)
    my_map.put(key, value)

print(f"Finished: Result = {my_map.get(key).result()}")

client.shutdown()
