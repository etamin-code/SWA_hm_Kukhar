# SWA_hm_Kukhar

```
consul agent -dev

bash consul_config.sh

sudo docker network create hazelcast-network 
sudo docker run -p 5701:5701 hazelcast/hazelcast:5.1.1 # run it in another terminal window 

python3 facade_controller.py --port 8000 # run it in another terminal window 
python3 facade_controller.py --port 8001 # run it in another terminal window 

python3 logging_service.py --port 8002 # run it in another terminal window 
python3 logging_service.py --port 8003 # run it in another terminal window 

python3 messages_service.py --port 8004 # run it in another terminal window 
python3 messages_service.py --port 8005 # run it in another terminal window 

bash post_requests.sh
bash get_request.sh
```

results: 
``` bash post_requests.sh ```
this command post 5 messages to one facade service, and 5 messages to another one

if you want to see all messages from messages service you have to run ``` bash get_request.sh ``` a few times, because it select only one messages service per once

![results](https://user-images.githubusercontent.com/70692373/173190966-cc9ffddc-c742-4005-b657-bac38145d794.png)

## logs from all services

### facade 8000
![facade8000](https://user-images.githubusercontent.com/70692373/173191091-4b3abb05-77fa-41fb-af02-d36f20abb61d.png)

### facade 8001
![facade8001](https://user-images.githubusercontent.com/70692373/173191093-6e46f65a-ff50-4017-92ef-490cc22279f3.png)

### logging 8002
![logging8002](https://user-images.githubusercontent.com/70692373/173191099-c4083bd1-02e3-4d21-a280-6aa4e0b04e5e.png)

### logging 8003
![logging8003](https://user-images.githubusercontent.com/70692373/173191102-296fe372-f299-4b17-9afb-929e373f85ea.png)

### messages 8004
![messages8004](https://user-images.githubusercontent.com/70692373/173191107-6a6d3c81-b304-4576-b9bb-54a432c7888b.png)

### messages 8005
![messages8005](https://user-images.githubusercontent.com/70692373/173191112-f594a2b3-4b62-47f0-9d9c-95b6e69f7ef0.png)
