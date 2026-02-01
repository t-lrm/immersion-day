FROM nginx:alpine
RUN apk add --no-cache bash zip
WORKDIR /app

COPY . /app
COPY docker/fileserver.conf.template /etc/nginx/templates/fileserver.conf.template
COPY docker/entrypoint.sh /docker-entrypoint.d/10-build-assets.sh
RUN chmod +x /docker-entrypoint.d/10-build-assets.sh

