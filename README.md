# Three-Tier Capstone - Take Home Project

This is a take-home Capstone project for anyone interested in furthering what they learned in the Kubernetes course and the main capstone project. This project takes it further by having you containerize three separate applications of a 3-tier solution. Each tier is its own app. The details for each are located in the relevant repositories.

We recommend you first containerize and run the database (db), followed by the mid tier (mid) followed at last by the front end(pxfe).

## Repository Structure

```
├── frontend/     # User interface tier (Python Flask)
├── middleware/   # Business logic tier (Spring Boot) 
└── database/    # Data persistence tier (PostgreSQL)
```

## Purpose

This project serves as a reference implementation showing:

- Multi-stage container builds
- Inter-service communication patterns
- Environment-based configuration
- Kubernetes deployment strategies
- Persistent data handling
- Service discovery approaches

Each tier contains its own detailed README with specific implementation details and instructions.

## Architecture Flow

1. Frontend service provides the user interface and makes API calls
2. Middleware service handles business logic and data processing
3. Database service provides persistent data storage

## Technology Stack

- Frontend: Python Flask
- Middleware: Spring Boot
- Database: PostgreSQL
- Containerization: Docker
- Orchestration: Kubernetes

See individual component READMEs for detailed implementation specifics.