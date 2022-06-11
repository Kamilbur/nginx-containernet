#/usr/bin/env bash

set -e

docker build -f ./nginx/Dockerfile -t nginxx .
docker build -f ./wrk2/Dockerfile -t wrk2 .

