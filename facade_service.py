import requests
import random
import json


logging_service_name = "logging_service"
message_service_name = "message_service"
HTTP_START = "http://"


def get_service_address(consul_service, service_name):
    registered_servers = consul_service.agent.services()
    registered_servers_names = [key for key in registered_servers.keys()]
    services_names = [server for server in registered_servers_names if server.startswith(service_name)]
    random_service = random.choice(services_names)
    service_address = HTTP_START + registered_servers[random_service]['Address'] + \
                      ":" + str(registered_servers[random_service]['Port']) + "/" + service_name
    return service_address


def get_data(consul_service):
    try:
        logging_url = get_service_address(consul_service, logging_service_name)
        messages_url = get_service_address(consul_service, message_service_name)
        print(f"cur_logging_service: {logging_url}")
        print(f"cur_messages_service: {messages_url}")

        log_ans = requests.get(logging_url).text

        msg_ans = requests.get(messages_url).text
        data = f"Logging messages: {log_ans} \n" \
               f"Messages service messages: {msg_ans}"
        return data
    except requests.exceptions.ConnectionError:
        return "Error occurred"


def post_messages_logging(logging_service, data):
    response = requests.post(url=logging_service, data=json.dumps(data),
                             headers={"Content-Type": "application/json"})
    return response


def post_message(consul_service, q, msg):

    logging_url = get_service_address(consul_service, logging_service_name)
    print(f"logging_url: {logging_url}\n")
    response_logging = post_request(logging_url, params={"msg_hash": hash(msg), "msg": msg})
    msg_code = 200
    try:
        print("try put message")
        q.put(msg)
    except:
        msg_code = 404
    return {
        "statusCode": [response_logging.status_code, msg_code]
    }


def post_request(url, params):
    print("sending request to logging")
    return requests.post(url, params=params)


