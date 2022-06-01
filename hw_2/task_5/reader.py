import time
import hazelcast
import sys

client = hazelcast.HazelcastClient(cluster_name="dev")

print("Starting")

q = client.get_queue("my_queue").blocking()
if len(sys.argv) >= 2:
    reader_id = sys.argv[1]
else:
    reader_id = 0

while True:
    value = q.take()
    if not value:
        continue
    print(f"reader {reader_id} get {value}")
    time.sleep(0.01)


client.shutdown()
