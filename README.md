# SWA_hm_Kukhar

## usage
### this code is present in manual.sh

```
sudo docker network create hazelcast-network

sudo docker run -p 5701:5701 hazelcast/hazelcast:5.1.1 

uvicorn facade_service:app --host=localhost --port=8000 # you have to run that in another terminal window
uvicorn message_service:app --host=localhost --port=8001 # you have to run that in another terminal window
uvicorn message_service:app --host=localhost --port=8002 # you have to run that in another terminal window
uvicorn logging_service:app --host=localhost --port=8003 # you have to run that in another terminal window
uvicorn logging_service:app --host=localhost --port=8004 # you have to run that in another terminal window
uvicorn logging_service:app --host=localhost --port=8005 # you have to run that in another terminal window

bash post_requests.sh
bash get_request.sh
```

logs from first logging (port 8003)

![Screenshot from 2022-06-07 22-17-07](https://user-images.githubusercontent.com/70692373/172466095-5e64e380-d981-4be1-95d1-884c2d3db17c.png)


logs from second logging (port 8004)

![Screenshot from 2022-06-07 22-17-29](https://user-images.githubusercontent.com/70692373/172466265-2cf7774f-424e-444e-b761-c2f33a6346e1.png)


logs from third logging (port 8005)

![Screenshot from 2022-06-07 22-17-57](https://user-images.githubusercontent.com/70692373/172466289-8766eab7-96a8-4a21-82d3-d4ef5a5990db.png)


logs from first messages service (port 8001)

![Screenshot from 2022-06-07 22-21-55](https://user-images.githubusercontent.com/70692373/172466449-9e67edc5-03e9-4fa5-ba24-f5179c2142f4.png)

here all messages came to 8001, because message service start read messages only after get request, and all waiting messages come to one of the available services.


get request:

![Screenshot from 2022-06-07 22-20-50](https://user-images.githubusercontent.com/70692373/172467056-c9d66dfa-b9ac-41da-b663-d9ebc7bbe5b9.png)
