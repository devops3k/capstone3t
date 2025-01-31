# Use Maven to build (pick a known existing version)
FROM maven:3.9.9-eclipse-temurin-17 AS builder
WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline

COPY src ./src
# RUN mvn clean package -DskipTests
RUN mvn clean package spring-boot:repackage -DskipTests


# Create a lightweight runtime image
FROM openjdk:17-jdk-slim
WORKDIR /app

COPY --from=builder /app/target/middle-1.0.0.jar app.jar

ENV DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=demo \
    DB_USER=postgres \
    DB_PASSWORD=postgres \
    APP_PORT=8080

EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
