FROM python:3.9.9-slim-bullseye

ENV TZ Asia/Shanghai

COPY ELF_RSS /app

WORKDIR /app

RUN python3 -m pip install  --use-deprecated=legacy-resolver -r requirements.txt && ls -lah && \
    mv ./.env.dev ./.env.prod

VOLUME ["/app/data", "/app/env.prod"]

EXPOSE 8080

ENTRYPOINT [ "nb", "run" ]
