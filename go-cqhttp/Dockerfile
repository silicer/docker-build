ARG TARGETARCH

FROM alpine:latest AS fetcher

RUN wget -q https://github.com/Mrs4s/go-cqhttp/releases/latest/download/go-cqhttp_linux_${TARGETARCH}.tar.gz \
    && tar -xzf go-cqhttp_linux_${TARGETARCH}.tar.gz go-cqhttp -O > /go-cqhttp

FROM alpine:latest

RUN apk add --no-cache --update --quiet --no-progress tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del --quiet --no-progress tzdata

COPY --from=fetcher /go-cqhttp /usr/bin/cqhttp

RUN chmod +x /usr/bin/cqhttp

WORKDIR /data

ENTRYPOINT [ "/usr/bin/cqhttp" ]