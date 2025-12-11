# Metis File Upload API Deployment Guide

## Overview
This guide provides instructions for deploying the Metis File Upload API to staging and production environments.

## Prerequisites
- Python 3.13+
- Conda (for environment management)
- Git
- Access to the target server (for staging/production)

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Metis
```

### 2. Create and Activate Conda Environment
```bash
conda create -n metis python=3.13
conda activate metis
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file based on the `.env.example` template:

```bash
cp .env.example .env
```

Edit the `.env` file to set the appropriate values for your environment:

```bash
# File Upload Configuration
BASE_UPLOAD_DIR=uploads
SUPPORTED_FORMATS=.txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.csv
MAX_FILE_SIZE=104857600
MAX_FILES_PER_UPLOAD=20

# Other configuration variables...
```

## Staging Deployment

### Option 1: Direct Deployment

1. **Start the API Server**
   ```bash
   python -m src.api.main
   ```

2. **Verify Deployment**
   ```bash
   curl http://localhost:8000/health
   ```
   Expected response:
   ```json
   {"status": "ok", "message": "File Upload API is running"}
   ```

### Option 2: Using Uvicorn Directly

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Option 3: Using Gunicorn (Recommended for Production-Like Environments)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Start Gunicorn**
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.api.main:app --bind 0.0.0.0:8000
   ```

## Production Deployment

### 1. Use a WSGI Server
For production, it's recommended to use a WSGI server like Gunicorn with multiple workers.

### 2. Configure a Reverse Proxy
Set up a reverse proxy like Nginx or Apache to handle HTTPS and load balancing.

#### Example Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 3. Set Up Process Management
Use a process manager like systemd or supervisor to ensure the API automatically restarts if it crashes.

#### Example systemd Service
```ini
[Unit]
Description=Metis File Upload API
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/Metis
ExecStart=/path/to/conda/envs/metis/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.api.main:app --bind 0.0.0.0:8000
Restart=always
Environment=PATH=/path/to/conda/envs/metis/bin

[Install]
WantedBy=multi-user.target
```

### 4. Configure Logging
Set up proper logging for production monitoring.

### 5. Backup Strategy
Implement a backup strategy for the uploaded files.

## Monitoring

### Health Check
Monitor the `/health` endpoint to ensure the API is running.

### Logs
Monitor the API logs for errors and performance issues.

### Metrics
Consider adding metrics monitoring using tools like Prometheus and Grafana.

## Scaling Considerations

### 1. Horizontal Scaling
- Use multiple instances of the API behind a load balancer
- Ensure file storage is accessible from all instances (e.g., using a shared file system or cloud storage)

### 2. Vertical Scaling
- Increase server resources (CPU, memory)
- Adjust Gunicorn worker count based on available resources

### 3. Storage Scaling
- For large-scale deployments, consider using a cloud storage provider (AWS S3, Azure Blob Storage, Google Cloud Storage)
- Implement proper file lifecycle management

## Security Recommendations

1. **Implement Authentication**
   - Add API key authentication
   - Consider OAuth2 for user-level authentication

2. **Enable HTTPS**
   - Use SSL certificates from a trusted CA
   - Configure the reverse proxy to enforce HTTPS

3. **Input Validation**
   - Ensure all user inputs are properly validated
   - Sanitize filenames to prevent path traversal attacks

4. **Access Control**
   - Restrict file access based on user permissions
   - Implement proper CORS policies

5. **Regular Updates**
   - Keep dependencies up to date
   - Apply security patches promptly

## Rollback Plan

1. **Backup Current Deployment**
   - Backup the current codebase
   - Backup the environment configuration
   - Backup uploaded files

2. **Rollback Steps**
   - Stop the current API server
   - Restore the previous codebase
   - Restore the environment configuration
   - Restart the API server
   - Verify functionality

## Troubleshooting

### Common Issues

1. **API Not Starting**
   - Check the logs for errors
   - Verify environment variables are correctly set
   - Ensure all dependencies are installed

2. **File Uploads Failing**
   - Check file permissions on the upload directory
   - Verify disk space is available
   - Check file size limits in configuration

3. **Performance Issues**
   - Increase Gunicorn worker count
   - Optimize file storage access
   - Consider caching frequently accessed data

## Conclusion

By following this guide, you can successfully deploy the Metis File Upload API to staging and production environments. Ensure to regularly monitor the deployment and apply security updates as needed.
