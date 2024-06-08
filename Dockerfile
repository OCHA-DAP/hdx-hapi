FROM python:3.12-alpine

WORKDIR /srv/hapi

COPY . .

RUN apk add \
        postgresql-dev \
        unit \ 
        unit-python3 && \
    apk --virtual .build-deps add \
        git \
        build-base \
        python3-dev && \
    mkdir -p \
        /etc/services.d/hapi \
        /var/log/hapi && \
    mv docker/hapi_run /etc/services.d/hapi/run && \
    pip3 --no-cache-dir install --upgrade \
        pip \
        wheel && \
    pip3 install --upgrade -r requirements.txt && \
    pip3 install elastic-apm && \
    apk del .build-deps && \
    rm -rf /var/lib/apk/* && rm -r /root/.cache

EXPOSE 5000
