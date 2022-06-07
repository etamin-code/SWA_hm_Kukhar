# SWA_hm_Kukhar
## usage
### next commands are saved in manual.sh 
```
sudo docker network create hazelcast-network 
sudo docker run -p 5701:5701 hazelcast/hazelcast:5.1.1

uvicorn facade_service:app --host=localhost --port=8000 # on another terminal window 
uvicorn message_service:app --host=localhost --port=8001 # on another terminal window 
uvicorn logging_service:app --host=localhost --port=8002 # on another terminal window 
uvicorn logging_service:app --host=localhost --port=8003 # on another terminal window 
uvicorn logging_service:app --host=localhost --port=8004 # on another terminal window 

bash post_requests.sh
bash get_request.sh
```
![Screenshot from 2022-06-06 19-00-41](https://user-images.githubusercontent.com/70692373/172375097-d9e88c7b-0260-4e95-a4a7-b13e30b71d34.png)

logs from port 8002:

![Screenshot from 2022-06-06 18-54-52](https://user-images.githubusercontent.com/70692373/172375212-d93ef13a-0b4b-4348-b1df-46342a5ee8a1.png)

logs from port 8003:

![Screenshot from 2022-06-06 18-56-14](https://user-images.githubusercontent.com/70692373/172375230-3991d71b-29e9-46b6-a1d1-306752138f01.png)

logs from port 8004:

![Screenshot from 2022-06-06 18-56-52](https://user-images.githubusercontent.com/70692373/172375240-20d473cd-959a-4b45-8ea0-e22bf500b835.png)


to post or to get request facade service randomly choose one of the logging ports, so  after stopping some logging service, facade must find still working one.
After stopping ports 8004 and 8003
return:

![Screenshot from 2022-06-06 19-46-04](https://user-images.githubusercontent.com/70692373/172375772-dbc35da1-2d69-4e89-b0cf-0b606246bc9c.png)
as we see all messages are present.

facade logs:

![Screenshot from 2022-06-06 19-43-34](https://user-images.githubusercontent.com/70692373/172375811-2fcdd911-d8a7-4cfe-bb7e-28900276d8da.png)


