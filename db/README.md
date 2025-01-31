# PostgreSQL Docker & Kubernetes Exercise

## Part 1: Dockerfile Creation and Publishing

### Prerequisites
- Docker installed
- Docker Hub account
- init.sql file (provided)

### Docker Steps
1. Create a new file named `Dockerfile` (no extension)
2. Research and use PostgreSQL 14 Alpine as base image
3. Add command to copy init.sql to /docker-entrypoint-initdb.d/
4. Set these exact environment variables:
   - POSTGRES_DB=demo
   - POSTGRES_USER=postgres
   - POSTGRES_PASSWORD=postgres
5. Expose PostgreSQL default port (5432)

### Build & Push
1. Login to Docker Hub: `docker login`
2. Build image: `docker build -t yourusername/imagename:tag .`
3. Push to Docker Hub: `docker push yourusername/imagename:tag`

## Part 2: Kubernetes Deployment

Create three Kubernetes resource definitions in a single YAML file:

### 1. Persistent Volume Claim
- Define PVC named 'postgres-pvc'
- Request 1GB storage
- Set access mode to ReadWriteOnce

### 2. Deployment
- Name it 'database-deployment'
- Set 1 replica
- Use your Docker Hub image
- Configure labels for app: database
- Set container port to 5432
- Add environment variables for:
  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD
- Mount volume to PostgreSQL data directory
- Link to PVC created above

### 3. Service
- Name it 'database-service'
- Type: ClusterIP
- Target port 5432
- Select pods using appropriate labels

Save all three resources in a single YAML file with correct separators between resources.