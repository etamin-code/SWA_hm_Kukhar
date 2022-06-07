#!/bin/bash

END=10
for ((i=1;i<=END;i++)); do
    curl -X 'POST'   'http://localhost:8000/msg'${i}''   -H 'accept: application/json'   -d ''
done
