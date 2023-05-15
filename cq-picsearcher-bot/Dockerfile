FROM node:16-bullseye-slim

ARG TARGETARCH

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get -qq update && apt-get -qq install gcc g++ python3; \
        fi
# RUN apk add --no-cache --update tzdata && \
#     cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
#     echo "Asia/Shanghai" > /etc/timezone && \
#     apk del tzdata

COPY cq-picsearcher-bot /cq-picsearcher-bot
WORKDIR /cq-picsearcher-bot

RUN yarn --production
RUN cp /cq-picsearcher-bot/config.default.jsonc /cq-picsearcher-bot/config.jsonc
VOLUME /cq-picsearcher-bot/data
VOLUME /cq-picsearcher-bot/config.jsonc

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get -qq remove gcc g++ python3 && apt-get -qq autoremove; \
        fi

EXPOSE 2333

ENTRYPOINT [ "npm", "run", "test" ]
