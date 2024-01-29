FROM docker.io/mysql:8.0
COPY ./pfs_stats.sql docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD root_secret_pw
ENV MYSQL_DATABASE pfs_stats
ENV MYSQL_USER pfs_user
ENV MYSQL_PASSWORD pfs_secret_pw