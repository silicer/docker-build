FROM alpine/git:latest AS fetcher

RUN git clone --depth 1 https://github.com/Quan666/ELF_RSS.git /ELF_RSS

FROM python:3.9-slim

ENV TZ Asia/Shanghai

ARG TARGETARCH

COPY --from=fetcher /ELF_RSS /app

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get -qq update && apt-get -qq install gcc g++; \
        fi

WORKDIR /app

RUN python3 -m pip install --no-cache-dir -r requirements.txt && ls -lah && \
    mv ./.env.dev ./.env.prod

RUN if [ "${TARGETARCH}" = "arm64" ]; then \
            apt-get -qq remove gcc g++ && apt-get -qq autoremove; \
        fi

VOLUME ["/app/data", "/app/env.prod"]

EXPOSE 8080

ENTRYPOINT [ "nb", "run" ]
