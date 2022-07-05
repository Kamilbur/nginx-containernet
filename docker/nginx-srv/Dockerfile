ARG version=open

FROM nginx-${version}-base:1.0.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY matrix-srv/requirements.txt  /root/matrix-srv/requirements.txt

RUN python3 -m pip install -r /root/matrix-srv/requirements.txt

COPY matrix-srv  /root/matrix-srv
COPY nginx-conf /root/nginx-conf



#ENTRYPOINT /docker-entrypoint.sh /bin/sh -c /bin/bash
