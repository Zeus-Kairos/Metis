# Metis Deployment Guide

## Overview
This guide provides comprehensive instructions for deploying the full Metis application (backend API + frontend UI) to staging and production environments. Metis is an advanced Retrieval-Augmented Generation (RAG) application that enables users to interact with AI using their own documents.

## Minimum Requirements

### System Requirements
- **CPU**: 2+ cores (4+ cores recommended for production)
- **RAM**: 4GB minimum (8GB+ recommended for production)
- **Disk Space**: 50GB minimum (additional space for document storage)
- **Network**: Stable internet connection for API calls to LLM/embedding services

### Software Requirements
- **Python**: 3.10 - 3.13
- **Node.js**: 16.x - 20.x (for frontend build)
- **PostgreSQL**: 13.x or higher
- **Conda**: 4.10+ (for environment management)
- **Git**: 2.20+ (for repository cloning)
- **Nginx**: 1.18+ (for reverse proxy in production)
- **Gunicorn**: 20.1+ (for WSGI server in production)

## Prerequisites
- Access to the target server (for staging/production)
- PostgreSQL database instance (local or remote)
- Domain name (for production deployment with HTTPS)
- SSL certificate (for production HTTPS)
- API keys for LLM and embedding services (e.g., Ollama, OpenAI, Nomic)

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

### 3. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Frontend Dependencies
```bash
npm install
```

### 5. Configure Environment Variables
Create a `.env` file based on the `.env.example` template:

```bash
cp .env.example .env
```

Edit the `.env` file to set the appropriate values for your environment. Key configuration variables include:

```bash
# Database Configuration
DB_URI=postgresql://username:password@localhost:5432/metis_db

# JWT Authentication
SECRET_KEY=your-secret-key-for-jwt

# File Upload Configuration
BASE_UPLOAD_DIR=uploads
SUPPORTED_FORMATS=.txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.csv
MAX_FILE_SIZE=104857600
MAX_FILES_PER_UPLOAD=20

# Logging
LOG_LEVEL=INFO

# RAG Configuration
RAG_TYPE=fusion
RAG_K=10
```

## Staging Deployment

### Backend Deployment

#### Option 1: Run Backend with Python Directly
```bash
python main.py
```

#### Option 2: Run Backend with Uvicorn (Recommended for Staging)
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Deployment (Staging)
```bash
npm run dev
```

### Verify Deployment
- Backend API: `http://<server-ip>:8000/health` should return `{"status": "ok"}`
- Frontend UI: `http://<server-ip>:5173` should display the Metis login page

## Production Deployment

### Backend Production Setup

#### 1. Use Gunicorn WSGI Server
```bash
pip install gunicorn
```

#### 2. Create a Gunicorn Configuration File (Optional but Recommended)
Create `gunicorn_config.py` in the project root:
```python
bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
threads = 4
timeout = 300
max_requests = 1000
max_requests_jitter = 100
accesslog = "-"
errorlog = "-"
loglevel = "info"
```

#### 3. Set Up Process Management with systemd
Create a systemd service file at `/etc/systemd/system/metis-backend.service`:
```ini
[Unit]
Description=Metis Backend API
After=network.target postgresql.service

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/Metis
ExecStart=/path/to/conda/envs/metis/bin/gunicorn -c gunicorn_config.py src.api.main:app
Restart=always
Environment=PATH=/path/to/conda/envs/metis/bin
EnvironmentFile=/path/to/Metis/.env

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable metis-backend
sudo systemctl start metis-backend
```

### Frontend Production Setup

#### 1. Build the Frontend
```bash
cd src/ui
npm run build
cd ../..
```

#### 2. Deploy with Nginx
Copy the built files to a web server directory:
```bash
sudo mkdir -p /var/www/metis-ui
sudo cp -r src/ui/dist/* /var/www/metis-ui/
sudo chown -R www-data:www-data /var/www/metis-ui/
```

#### 3. Configure Nginx for Both Backend and Frontend
Create or update Nginx configuration at `/etc/nginx/sites-available/metis`:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;
    
    # SSL Configuration
    ssl_certificate /path/to/your/cert.pem;
    ssl_certificate_key /path/to/your/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Frontend Configuration
    location / {
        root /var/www/metis-ui;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
    
    # Backend API Configuration
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300;
        proxy_send_timeout 300;
    }
    
    # Health Check Endpoint
    location /health {
        proxy_pass http://localhost:8000/health;
    }
}
```

Enable the Nginx configuration:
```bash
sudo ln -s /etc/nginx/sites-available/metis /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Database Setup (PostgreSQL)

### 1. Create Database and User
```bash
sudo -u postgres psql

CREATE DATABASE metis_db;
CREATE USER metis_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE metis_db TO metis_user;
ALTER USER metis_user CREATEDB;
\q
```

### 2. Verify Database Connection
```bash
psql -h localhost -U metis_user -d metis_db
\q
```

## Monitoring

### 1. Backend Logs
```bash
sudo journalctl -u metis-backend -f
```

### 2. Nginx Logs
```bash
sudo tail -f /var/log/nginx/access.log /var/log/nginx/error.log
```

### 3. Database Monitoring
Consider using tools like pgAdmin or Grafana with PostgreSQL datasource for database monitoring.

### 4. Application Metrics
Implement Prometheus and Grafana for advanced metrics monitoring:
- Add Prometheus middleware to FastAPI
- Configure Grafana dashboards for key metrics

## Security Hardening

1. **Database Security**
   - Use strong database passwords
   - Restrict database access to specific IPs
   - Enable SSL for database connections

2. **API Security**
   - Implement rate limiting
   - Use secure JWT settings (short expiration times, strong secrets)
   - Enable CORS with specific origins only

3. **Server Security**
   - Keep server OS and software up to date
   - Use a firewall to restrict access to necessary ports only
   - Disable root SSH access
   - Use SSH keys instead of passwords

4. **File Security**
   - Set proper permissions on uploaded files (644 for files, 755 for directories)
   - Implement file type validation
   - Use secure file storage paths to prevent path traversal attacks

## Backup Strategy

### 1. Database Backup
Set up regular PostgreSQL backups:
```bash
# Example: Daily backup at 2 AM
0 2 * * * pg_dump -h localhost -U metis_user -d metis_db | gzip > /path/to/backups/metis_db_$(date +\%Y\%m\%d).sql.gz
```

### 2. File Backup
Back up the uploaded files directory:
```bash
# Example: Daily backup of uploads directory
0 3 * * * tar -czf /path/to/backups/uploads_$(date +\%Y\%m\%d).tar.gz /path/to/Metis/uploads
```

### 3. Configuration Backup
Back up the `.env` file and other configuration files regularly.

## Scaling Considerations

### Horizontal Scaling
- Deploy multiple backend instances behind a load balancer
- Use a shared file system or cloud storage (S3, Azure Blob) for uploaded files
- Use a managed PostgreSQL instance for better scalability

### Vertical Scaling
- Increase server CPU/RAM based on usage
- Adjust Gunicorn worker count: `workers = (2 * CPU cores) + 1`

### Database Scaling
- Consider read replicas for heavy read workloads
- Implement database indexing for frequently queried tables

## Rollback Plan

### 1. Pre-Deployment Backup
Always create backups before deploying updates:
```bash
# Backup codebase
git checkout main
git pull
git tag -a vX.Y.Z -m "Backup before deployment"

# Backup database
pg_dump -h localhost -U metis_user -d metis_db > metis_db_backup_pre_deploy.sql

# Backup uploaded files
tar -czf uploads_backup_pre_deploy.tar.gz uploads/
```

### 2. Rollback Steps
```bash
# 1. Stop current services
sudo systemctl stop metis-backend
sudo systemctl stop nginx

# 2. Restore codebase to previous version
git checkout vX.Y.Z-previous

# 3. Restore database
sudo -u postgres psql metis_db < metis_db_backup_pre_deploy.sql

# 4. Restore uploaded files
tar -xzf uploads_backup_pre_deploy.tar.gz -C /path/to/Metis/

# 5. Restart services
sudo systemctl start metis-backend
sudo systemctl start nginx
```

## Troubleshooting

### Common Backend Issues

1. **Backend Failed to Start**
   - Check logs: `sudo journalctl -u metis-backend -n 100`
   - Verify environment variables in `.env` file
   - Ensure database connection is working
   - Check for port conflicts

2. **File Uploads Failing**
   - Check disk space: `df -h`
   - Verify permissions on upload directory: `ls -la uploads/`
   - Check file size limits in `.env`

3. **LLM/Embedding API Errors**
   - Verify API keys and base URLs in `.env`
   - Check network connectivity to LLM/embedding services
   - Review error logs for specific API error messages

### Common Frontend Issues

1. **Frontend Build Failed**
   - Check npm dependencies: `npm install --legacy-peer-deps` if encountering peer dependency issues
   - Verify Node.js version compatibility

2. **Frontend Can't Connect to Backend**
   - Check CORS settings in FastAPI
   - Verify backend URL in frontend configuration
   - Ensure backend API is running and accessible

3. **Blank Frontend Page**
   - Check browser console for JavaScript errors
   - Verify Nginx configuration for frontend routing
   - Ensure all frontend assets are properly built and served

## Conclusion

By following this guide, you can successfully deploy the Metis application to both staging and production environments. Always test deployments in staging first, and ensure proper monitoring and backups are in place for production environments. Regularly update dependencies and apply security patches to maintain a secure and reliable deployment.
