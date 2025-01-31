FROM postgres:14-alpine

# Copy the seed script into the container
COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=demo \
    POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=postgres

EXPOSE 5432
