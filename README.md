# Three-Tier Application Architecture Example

This repository demonstrates a complete three-tier application architecture using containers and Kubernetes orchestration. It provides working examples of containerization patterns, service discovery, and deployment configurations across all three tiers.

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