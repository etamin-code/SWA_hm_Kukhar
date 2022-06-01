import hazelcast


client = hazelcast.HazelcastClient(cluster_name="dev",
                                   cluster_members=[
                                       "172.18.0.2:5701",
                                       "172.18.0.3:5701",
                                       "172.18.0.4:5701"
                                   ])
                                   
my_map = client.get_map("my-distributed-map").blocking()

for idx in range(1000):
    my_map.put(f"key-{idx}", f"value-{idx}")
client.shutdown()
print("done")

