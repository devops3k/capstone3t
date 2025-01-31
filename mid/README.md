# Spring Boot PostgreSQL Middleware Challenge

## Overview
This project is a Spring Boot application that serves as a middleware layer between clients and a PostgreSQL database. The application uses JPA for database operations and exposes REST endpoints.

## Challenge Description

### Part 1: Containerization
Create a multi-stage Dockerfile following these steps:

Build Stage:
1. Start with Maven base image (research appropriate version for Java 17)
2. Set working directory
3. Copy POM file first (why?)
4. Download dependencies
5. Copy source code
6. Build the application (research Maven commands)

Runtime Stage:
1. Start with minimal JDK base image
2. Set working directory
3. Copy JAR from build stage
4. Set these environment variables:
   - DB_HOST
   - DB_PORT
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - APP_PORT
5. Expose port
6. Set entrypoint to run JAR

### Part 2: Docker Hub Publishing
1. Build image:
   ```
   docker build -t <your-dockerhub-username>/middle:<tag> .
   ```
2. Docker Hub authentication:
   ```
   docker login
   ```
3. Push image:
   ```
   docker push <your-dockerhub-username>/middle:<tag>
   ```

### Part 3: Kubernetes Deployment
Create a deployment manifest with these components:

Deployment:
1. Set API version and kind
2. Define metadata
3. Specify replicas
4. Configure selector and labels
5. Container configuration:
   - Image reference
   - Port configuration
   - Environment variables matching Dockerfile
   - Resource limits (optional)

Service:
1. Set API version and kind
2. Define metadata
3. Choose service type (ClusterIP/NodePort)
4. Configure selector to match deployment
5. Set up port mappings:
   - Service port
   - Target port
   - Node port (if using NodePort)

## Requirements
- Java 17
- Maven
- Docker
- Kubernetes cluster
- Docker Hub account

## Success Criteria
- Container builds successfully
- Image pushes to Docker Hub
- Deployment creates pods
- Service exposes deployment
- Application can connect to database
- Environment variables are properly configured

## Notes
- Application expects PostgreSQL database connection
- Default application port is 8080
- Environment variables must match exactly as specified
- Consider production best practices for container security
- Think about proper resource allocation in Kubernetes
- Consider service discovery within Kubernetes cluster

Your solution should demonstrate understanding of:
- Multi-stage Docker builds
- Environment configuration
- Kubernetes deployment concepts
- Service networking in Kubernetes
- Container registry usage