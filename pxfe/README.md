# Frontend Service Containerization Challenge

## Project Overview
This is a Python Flask frontend service that provides a web interface to interact with a middle-tier service. The app displays a Bootstrap-styled page with buttons to fetch data from the middle service endpoints.

Key features:
- Flask web server running on port 5000 
- Makes HTTP calls to a middle service using MID_HOST and MID_PORT env vars
- Serves a Bootstrap UI with AJAX functionality
- Two main endpoints: /fetchHello and /fetchPeople

## Challenge 1: Multi-Stage Dockerfile

Create a multi-stage Dockerfile following these steps:

1. Build Stage:
   - Use python:3.9-slim as base image
   - Set /app as working directory
   - Copy only requirements.txt first (optimization for caching)
   - Install dependencies from requirements.txt
   - Copy remaining application code (app.py, templates/)

2. Final Stage:
   - Use python:3.9-slim again
   - Set /app as working directory 
   - Copy built artifacts from build stage
   - Expose port 5000
   - Configure startup command with python app.py

3. Build and Push:
   - Build with tag format: yourusername/pxfe:0.1
   - Create public Docker Hub repository
   - Push tagged image to Docker Hub

## Challenge 2: Kubernetes Manifest

Create a manifest with these components:

1. Deployment:
   ```yaml
   # Structure (fill in the details):
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: # name
   spec:
     replicas: # number
     selector: # labels
     template:
       spec:
         containers:
           - name: # container name
             image: # your image
             env: # MID_HOST & MID_PORT
             ports: # container port
   ```

2. Service:
   ```yaml
   # Structure (fill in the details):
   apiVersion: v1
   kind: Service
   metadata:
     name: # service name
   spec:
     type: NodePort
     ports:
       - port: # service port
         targetPort: # container port
         nodePort: # external port
   ```

Key Requirements:
- Environment Variables:
  - MID_HOST: points to middle service
  - MID_PORT: middle service port
- Container Port: 5000
- NodePort Service: Accessible externally
- Container Security: Non-root user
- Resource Limits: Define appropriate requests/limits

## Success Criteria
- Multi-stage build reduces final image size
- Container runs as non-root user
- Application successfully connects to middle service
- Web UI accessible through NodePort
- All environment variables properly configured

## Notes
- Focus on security best practices
- Optimize for small image size
- Ensure proper error handling
- Consider production readiness