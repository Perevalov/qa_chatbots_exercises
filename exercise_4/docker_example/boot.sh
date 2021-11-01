#!/bin/bash

if [ -n $SERVER_PORT ]
then
    echo Starting container $NAME on port $SERVER_PORT
    exec uvicorn $NAME:app --reload --host 0.0.0.0 --port=80
fi