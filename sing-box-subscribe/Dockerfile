FROM alpine/git:latest as fetcher

RUN git clone --depth 1 https://github.com/Toperlock/sing-box-subscribe.git /sing-box-subscribe

FROM python:3.11-slim
COPY --from=fetcher /sing-box-subscribe /sing-box-subscribe
WORKDIR /sing-box-subscribe
RUN \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "api/app.py"]