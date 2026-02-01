FROM nginx:alpine
RUN apk add --no-cache bash zip
WORKDIR /app

COPY . /app
COPY fileserver.conf.template /etc/nginx/templates/fileserver.conf.template

COPY docker_entrypoint.sh /docker-entrypoint.d/10-build-assets.sh
RUN chmod +x /docker-entrypoint.d/10-build-assets.sh
