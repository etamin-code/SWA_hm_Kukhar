consul agent -dev

bash consul_config.sh

sudo docker network create hazelcast-network
sudo docker run -p 5701:5701 hazelcast/hazelcast:5.1.1

python3 facade_controller.py --port 8000
python3 facade_controller.py --port 8001

python3 logging_service.py --port 8002
python3 logging_service.py --port 8003

python3 messages_service.py --port 8004
python3 messages_service.py --port 8005

bash post_requests.sh
bash get_request.sh