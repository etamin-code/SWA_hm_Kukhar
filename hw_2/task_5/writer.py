import time
import hazelcast

client = hazelcast.HazelcastClient(cluster_name="dev")

print("Starting")

q = client.get_queue("my_queue").blocking()



for i in range(1000):
    print(f"Put {i}")
    res = q.put(i)
    if res:
        print(res.result())
    time.sleep(0.01)


client.shutdown()
