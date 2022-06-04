import hazelcast


client = hazelcast.HazelcastClient(cluster_name="dev")
                                   
my_map = client.get_map("my-distributed-map").blocking()

for i in range(1000):
    my_map.put(f"key-{i}", f"value-{i}")
client.shutdown()
print("done")

