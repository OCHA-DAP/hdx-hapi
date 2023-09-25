FROM public.ecr.aws/unocha/python:3

WORKDIR /srv/hapi

COPY . .

RUN apk add \
        unit \ 
        unit-python3 && \
    apk --virtual .build-deps add \
        git \
        build-base \
        python3-dev \ 
        postgresql-dev && \
    mkdir -p \
        /etc/services.d/hapi \
        /var/log/hapi && \
    mv docker/hapi_run /etc/services.d/hapi/run && \
    pip3 --no-cache-dir install --upgrade \
        pip \
        wheel && \
    pip3 install --upgrade -r requirements.txt && \
    apk del .build-deps && \
    rm -rf /var/lib/apk/* && rm -r /root/.cache

EXPOSE 5000
