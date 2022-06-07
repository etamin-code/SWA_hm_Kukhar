import hazelcast


client = hazelcast.HazelcastClient(cluster_name="dev")
                                   
my_map = client.get_map("my-distributed-map").blocking()

for idx in range(1000):
    my_map.put(f"key-{idx}", f"value-{idx}")
client.shutdown()
print("done")

