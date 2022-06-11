#!/bin/bash

END=10
for ((i=1;i<END/2;i++)); do
    curl -X 'POST'   'http://localhost:8000/msg'${i}''   -H 'accept: application/json'   -d ''
done

for ((i=END/2;i<=END;i++)); do
    curl -X 'POST'   'http://localhost:8001/msg'${i}''   -H 'accept: application/json'   -d ''
done
