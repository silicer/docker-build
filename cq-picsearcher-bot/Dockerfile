FROM node:lts-alpine

# 设置时区
RUN apk add --no-cache --update tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY cq-picsearcher-bot /cq-picsearcher-bot
WORKDIR /cq-picsearcher-bot

RUN yarn
VOLUME /cq-picsearcher-bot/data
VOLUME /cq-picsearcher-bot/config.jsonc

EXPOSE 2333

ENTRYPOINT [ "npm", "run", "test" ]
