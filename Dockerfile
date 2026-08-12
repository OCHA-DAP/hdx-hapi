FROM public.ecr.aws/unocha/python:3.14-stable

WORKDIR /srv/hapi

COPY . .

RUN apk add \
        envsubst \
        postgresql-dev \
        unit \
        unit-python3 && \
    apk --virtual .build-deps add \
        git \
        build-base \
        py3-wheel \
        python3-dev && \
    mkdir -p \
        /etc/services.d/hapi \
        /var/log/hapi && \
    mv docker/hapi_run /etc/services.d/hapi/run && \
    mkdir -p ~/.config/pip/ && echo -e "[global]\nbreak-system-packages = true" > ~/.config/pip/pip.conf && \
    pip3 --no-cache-dir install --upgrade pip && \
    rm -r /srv/hapi/src/hapi-schema && \
    pip3 install --upgrade -r requirements.txt && \
    pip3 install elastic-apm && \
    apk del .build-deps && \
    rm -rf /var/lib/apk/* && rm -r /root/.cache

EXPOSE 5000

ENTRYPOINT ["/init"]
