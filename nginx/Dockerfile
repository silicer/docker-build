# Based on: https://gist.github.com/hermanbanken/96f0ff298c162a522ddbba44cad31081

FROM nginx:alpine AS builder

# For latest build deps, see https://github.com/nginxinc/docker-nginx/blob/master/mainline/alpine/Dockerfile
RUN apk add --no-cache --virtual .build-deps \
      alpine-sdk \
      bash \
      cmake \
      findutils \
      gcc \
      gd-dev \
      geoip-dev \
      libc-dev \
      libedit-dev \
      libxslt-dev \
      linux-headers \
      make \
      openssl-dev \
      pcre2-dev \
      perl-dev \
      zlib-dev

RUN mkdir -p /usr/src \
    && git clone https://boringssl.googlesource.com/boringssl /usr/src/boringssl \
    && cd /usr/src/boringssl \
    && mkdir -p /usr/src/boringssl/build \
    && cmake -B/usr/src/boringssl/build -S/usr/src/boringssl -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    && make -C/usr/src/boringssl/build -j$(getconf _NPROCESSORS_ONLN) \
    && mkdir -p "/usr/src/boringssl/.openssl/lib" \
    && cd "/usr/src/boringssl/.openssl" \
    && ln -s ../include \
    && cd "/usr/src/boringssl" \
    && cp "build/crypto/libcrypto.a" "build/ssl/libssl.a" ".openssl/lib" \
    && wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O nginx.tar.gz \
    && wget https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/refs/heads/master.tar.gz -O nginx_substitutions_filter.tar.gz \
    && tar -zxC /usr/src -f nginx.tar.gz \
    && tar -zxC /usr/src -f nginx_substitutions_filter.tar.gz  \
    && rm nginx.tar.gz \
    && rm nginx_substitutions_filter.tar.gz \
    && git clone --recurse-submodules -j2 https://github.com/google/ngx_brotli /usr/src/ngx_brotli \
    && git clone --recurse-submodules -j2 https://github.com/arut/nginx-dav-ext-module /usr/src/ngx_dav_ext_module \
    && git clone --recurse-submodules -j2 https://github.com/openresty/headers-more-nginx-module /usr/src/headers_more_nginx_module \
    && cd /usr/src/nginx-$NGINX_VERSION \
    # && bash -c 'set -eux && eval ./configure $(nginx -V 2>&1 | sed -n -e "s/^.*configure arguments: //p") --with-cc-opt="-I/usr/src/boringssl/.openssl/include" --with-ld-opt="-L/usr/src/boringssl/.openssl/lib" --with-cc-opt="-I/usr/src/boringssl/include" --with-ld-opt="-L/usr/src/boringssl/build/ssl -L/usr/src/boringssl/build/crypto" --add-dynamic-module=/usr/src/ngx_http_substitutions_filter_module-master --add-dynamic-module=/usr/src/ngx_brotli --add-dynamic-module=/usr/src/ngx_dav_ext_module --add-dynamic-module=/usr/src/headers_more_nginx_module' \
    && bash -c 'set -eux && eval "./configure $(nginx -V 2>&1 | sed -n -e "s/^.*configure arguments: //p") --with-openssl=\"/usr/src/boringssl\" --with-cc-opt=\"-I/usr/src/boringssl/.openssl/include\" --with-ld-opt=\"-L/usr/src/boringssl/.openssl/lib\" --with-cc-opt=\"-I/usr/src/boringssl/include\" --with-ld-opt=\"-L/usr/src/boringssl/build/ssl -L/usr/src/boringssl/build/crypto\" --add-dynamic-module=/usr/src/ngx_http_substitutions_filter_module-master --add-dynamic-module=/usr/src/ngx_brotli --add-dynamic-module=/usr/src/ngx_dav_ext_module --add-dynamic-module=/usr/src/headers_more_nginx_module"' \
    && make -j$(getconf _NPROCESSORS_ONLN)\
    && make install

FROM nginx:alpine

COPY --from=builder /usr/lib/nginx/modules/* /usr/lib/nginx/modules/

COPY --from=builder /usr/sbin/nginx /usr/sbin/nginx

RUN sed -i '1iload_module /usr/lib/nginx/modules/ngx_http_subs_filter_module.so;\n' /etc/nginx/nginx.conf

EXPOSE 80
STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
