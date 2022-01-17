FROM python:3.9.9-slim-bullseye

ENV TZ Asia/Shanghai

COPY ELF_RSS /app

WORKDIR /app

RUN sed 's/nonebot2==2.0.0a15/nonebot2==2.0.0b1/g' -i requirements.txt && python3 -m pip install  --use-deprecated=legacy-resolver -r requirements.txt && ls -lah && \
    mv ./.env.dev ./.env.prod

VOLUME ["/app/data", "/app/env.prod"]

EXPOSE 8080

ENTRYPOINT [ "nb", "run" ]
