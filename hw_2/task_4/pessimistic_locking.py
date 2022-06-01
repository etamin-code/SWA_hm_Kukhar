import hazelcast
import time

client = hazelcast.HazelcastClient(cluster_name="dev")
  
print("Starting")

my_map = client.get_map("my-distributed-map").blocking()

key = "1"
value = "0"
my_map.put_if_absent(key, value)

for i in range(1000):
    my_map.lock(key)
    try:
        value = my_map.get(key)
        time.sleep(0.01)
        value = str(int(value) + 1)
        my_map.put(key, value)
    finally:
        my_map.unlock(key)

print(f"Finished: Result = {my_map.get(key)}")


client.shutdown()
