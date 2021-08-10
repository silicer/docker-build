FROM alpine:latest

RUN apk add --no-cache --update tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY go-cqhttp /usr/bin/cqhttp

RUN chmod +x /usr/bin/cqhttp

WORKDIR /data

ENTRYPOINT [ "/usr/bin/cqhttp" ]