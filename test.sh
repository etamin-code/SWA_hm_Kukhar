#!/bin/bash

curl -X 'GET'   'http://127.0.0.1:8000/'   -H 'accept: application/json'
echo
curl -X 'POST'   'http://127.0.0.1:8000/msg1'   -H 'accept: application/json'   -d ''
echo
curl -X 'POST'   'http://127.0.0.1:8000/msg2'   -H 'accept: application/json'   -d ''
echo
curl -X 'GET'   'http://127.0.0.1:8000/'   -H 'accept: application/json'
