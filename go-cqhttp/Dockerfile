FROM alpine:latest

ARG TARGETARCH

RUN apk add --no-cache --update --quiet --no-progress tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del --quiet --no-progress tzdata

COPY go-cqhttp.${TARGETARCH} /usr/bin/cqhttp

RUN chmod +x /usr/bin/cqhttp

WORKDIR /data

ENTRYPOINT [ "/usr/bin/cqhttp" ]