import hazelcast
import time

client = hazelcast.HazelcastClient(cluster_name="my_cluster")

print("Starting")
    
my_map = client.get_map("my-distributed-map").blocking()

key = "1"
value = "0"
my_map.put_if_absent(key, value)

for i in range(1000):
    while True:
        old_value = my_map.get(key)
        new_value = int(old_value)
        time.sleep(0.01)
        new_value += 1
        if my_map.replace_if_same(key, old_value, str(new_value)):
            break

print(f"Finished: Result = {my_map.get(key)}")


client.shutdown()
