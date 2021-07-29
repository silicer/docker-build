FROM node:lts-alpine

# 设置时区
RUN apk add --no-cache --update tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

# 安装依赖
RUN apk add --update --no-cache build-base g++ cairo-dev jpeg-dev pango-dev giflib-dev

COPY /home/runner/work/docker-cq-picsearcher-bot/docker-cq-picsearcher-bot /
WORKDIR /cq-picsearcher-bot

RUN yarn
VOLUME /cq-picsearcher-bot/data
VOLUME /cq-picsearcher-bot/config.jsonc

EXPOSE 2333

ENTRYPOINT [ "npm", "run", "test" ]
