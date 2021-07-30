FROM tiangolo/uvicorn-gunicorn-fastapi:latest

# RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

RUN apk add --no-cache --update tzdata libxml2 libxslt && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY ELF_RSS /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt && ls -lah && \
    mv ./.env.dev ./.env.prod

VOLUME ["/app/data", "/app/env.prod"]

EXPOSE 8080

ENTRYPOINT [ "nb", "run" ]
