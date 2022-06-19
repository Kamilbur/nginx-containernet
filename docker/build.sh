#/usr/bin/env bash

set -e

docker build -f ./nginx/Dockerfile -t nginxx nginx
docker build -f ./wrk2/Dockerfile -t wrk2 wrk2
docker build -f ./simple-srv/Dockerfile -t flask simple-srv


