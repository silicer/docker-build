FROM python:3.9-slim

ENV TZ Asia/Shanghai

ARG TARGETARCH

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get -qq update && apt-get -qq install gcc -y;
        fi

COPY ELF_RSS /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt && ls -lah && \
    mv ./.env.dev ./.env.prod

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get remove gcc -y && apt-get autoremove -y

VOLUME ["/app/data", "/app/env.prod"]

EXPOSE 8080

ENTRYPOINT [ "nb", "run" ]
