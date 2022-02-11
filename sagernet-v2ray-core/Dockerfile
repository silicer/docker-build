FROM alpine:latest

ARG TARGETARCH
ENV V2RAY_LOCATION_ASSET /usr/local/share/v2ray
WORKDIR /root

RUN apk add --no-cache --update --quiet --no-progress tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del --quiet --no-progress tzdata && \
    mkdir -p /etc/v2ray /usr/local/share/v2ray /var/log/v2ray

COPY ${TARGETARCH}/* .

RUN chmod +x v2ray && \
    mv v2ray /usr/bin/ && \
    mv geosite.dat geoip.dat geoip-only-cn-private.dat /usr/local/share/v2ray/ && \
    mv config.json /etc/v2ray/ && \
    rm -rf ./*

VOLUME /etc/v2ray

ENTRYPOINT ["/usr/bin/v2ray", "run", "-config", "/etc/v2ray/config.json"]
