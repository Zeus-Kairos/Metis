#!/usr/bin/env pwsh

# PostgreSQL setup script for Metis application

# Set up logging
$logFile = "$env:TEMP\metis_postgres_setup.log"
"=== Metis PostgreSQL Setup $(Get-Date) ===" | Out-File -FilePath $logFile -Append

Write-Host "=== Metis PostgreSQL Setup ==="

# Check if PostgreSQL is installed
Write-Host "Checking if PostgreSQL is installed..."
"Checking if PostgreSQL is installed..." | Out-File -FilePath $logFile -Append
try {
    $psqlVersion = & psql --version 2>&1
    Write-Host "PostgreSQL version found: $psqlVersion"
    "PostgreSQL version found: $psqlVersion" | Out-File -FilePath $logFile -Append
} catch {
    Write-Host "ERROR: PostgreSQL is not installed or not in PATH."
    Write-Host "Please install PostgreSQL 13.x or higher and add it to your PATH."
    Write-Host "Download PostgreSQL from: https://www.postgresql.org/download/"
    "ERROR: PostgreSQL is not installed or not in PATH." | Out-File -FilePath $logFile -Append
    exit 1
}

# Default values
$defaultDbName = "metis_db"
$defaultDbUser = "metis_user"
$defaultDbPort = "5432"

# Use default values for automated installation
$dbName = $defaultDbName
$dbUser = $defaultDbUser
$dbPort = $defaultDbPort

# Use fixed password for database user
$dbPassword = "metis_password_2026"
Write-Host "Using fixed password for database user"
"Using fixed password for user $dbUser" | Out-File -FilePath $logFile -Append

Write-Host ""
Write-Host "Creating database and user..."
"Creating database and user..." | Out-File -FilePath $logFile -Append

# Execute PostgreSQL commands individually
try {
    # Set PGPASSWORD environment variable to avoid password prompt
    $env:PGPASSWORD = "postgres"
    
    # Check if database exists, create if not
    "Checking if database exists..." | Out-File -FilePath $logFile -Append
    $dbExists = & psql -U postgres -p $dbPort -t -c "SELECT 1 FROM pg_database WHERE datname = '$dbName'" 2>&1
    if (-not $dbExists.ToString().Trim()) {
        "Creating database..." | Out-File -FilePath $logFile -Append
        $output = & psql -U postgres -p $dbPort -c "CREATE DATABASE $dbName" 2>&1
        $output | Out-File -FilePath $logFile -Append
        Write-Host "Database created successfully"
    } else {
        "Database already exists, skipping creation" | Out-File -FilePath $logFile -Append
        Write-Host "Database already exists, skipping creation"
    }
    
    # Check if user exists, create if not
    "Checking if user exists..." | Out-File -FilePath $logFile -Append
    $userExists = & psql -U postgres -p $dbPort -t -c "SELECT 1 FROM pg_roles WHERE rolname = '$dbUser'" 2>&1
    if (-not $userExists.ToString().Trim()) {
        "Creating user..." | Out-File -FilePath $logFile -Append
        $output = & psql -U postgres -p $dbPort -c "CREATE USER $dbUser WITH PASSWORD '$dbPassword'" 2>&1
        $output | Out-File -FilePath $logFile -Append
        Write-Host "User created successfully"
    } else {
        "User already exists, updating password" | Out-File -FilePath $logFile -Append
        $output = & psql -U postgres -p $dbPort -c "ALTER USER $dbUser WITH PASSWORD '$dbPassword'" 2>&1
        $output | Out-File -FilePath $logFile -Append
        Write-Host "Password updated successfully"
    }
    
    # Grant privileges
    "Granting privileges..." | Out-File -FilePath $logFile -Append
    $output = & psql -U postgres -p $dbPort -c "GRANT ALL PRIVILEGES ON DATABASE $dbName TO $dbUser" 2>&1
    $output | Out-File -FilePath $logFile -Append
    Write-Host "Database privileges granted"
    
    # Alter user
    "Altering user..." | Out-File -FilePath $logFile -Append
    $output = & psql -U postgres -p $dbPort -c "ALTER USER $dbUser CREATEDB" 2>&1
    $output | Out-File -FilePath $logFile -Append
    Write-Host "User permissions set"
    
    # Grant schema privileges
    "Granting schema privileges..." | Out-File -FilePath $logFile -Append
    $output = & psql -U postgres -p $dbPort -d $dbName -c "GRANT ALL ON SCHEMA public TO $dbUser" 2>&1
    $output | Out-File -FilePath $logFile -Append
    Write-Host "Schema privileges granted"
    
    # Clear the password from environment
    Remove-Item env:PGPASSWORD
    Write-Host ""
    Write-Host "Successfully configured database and user!"
    "Successfully created database and user!" | Out-File -FilePath $logFile -Append
} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to create database and user."
    Write-Host "Please make sure you have PostgreSQL superuser privileges."
    Write-Host "You may need to run this script as an administrator."
    "ERROR: Failed to create database and user." | Out-File -FilePath $logFile -Append
    $_.Exception.Message | Out-File -FilePath $logFile -Append
    exit 1
}
"Cleaned up temporary script file" | Out-File -FilePath $logFile -Append

# Create .env file with database configuration
Write-Host ""
Write-Host "Creating .env file with database configuration..."
"Creating .env file with database configuration..." | Out-File -FilePath $logFile -Append

# Evaluate the upload directory path
$uploadDir = [System.IO.Path]::Combine($env:LOCALAPPDATA, 'Metis', 'uploads')
"Upload directory: $uploadDir" | Out-File -FilePath $logFile -Append

# Evaluate the secret key
$secretKey = -join ((33..126) | Get-Random -Count 32 | ForEach-Object {[char]$_})
"Generated secret key" | Out-File -FilePath $logFile -Append

$envContent = "# Database Configuration
DB_URI=postgresql://$dbUser`:$dbPassword@localhost`:$dbPort/$dbName

# JWT Authentication
SECRET_KEY=$secretKey

# Metis local configuration
LLM_PROVIDER=ollama
LLM_API_KEY=your_api_key
LLM_MODEL=gpt-oss:20b-cloud
LLM_BASE_URL=http://localhost:11434
EMBED_PROVIDER=ollama
EMBED_API_KEY=your_api_key
EMBED_MODEL=nomic-embed-text:latest

# File Upload Configuration
BASE_UPLOAD_DIR=$uploadDir
SUPPORTED_FORMATS=.txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.csv
MAX_FILE_SIZE=104857600
MAX_FILES_PER_UPLOAD=20

# Logging
LOG_LEVEL=INFO

# RAG Configuration
RAG_TYPE=agentic
RAG_K=10"

# Get the directory where the script is located
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
"Script directory: $scriptDir" | Out-File -FilePath $logFile -Append

# Use AppData directory for .env file to avoid permission issues
$appDataDir = [System.IO.Path]::Combine($env:LOCALAPPDATA, 'Metis')
$backendDir = Join-Path -Path $appDataDir -ChildPath "backend"
"Backend directory: $backendDir" | Out-File -FilePath $logFile -Append

try {
    # Create backend directory if it doesn't exist
    if (-not (Test-Path -Path $backendDir)) {
        New-Item -ItemType Directory -Path $backendDir -Force | Out-Null
        "Created backend directory: $backendDir" | Out-File -FilePath $logFile -Append
    }
    
    $envContent | Out-File -FilePath "$backendDir\.env" -Encoding ASCII
    Write-Host "Created .env file with database configuration at $backendDir\.env"
    "Created .env file with database configuration at $backendDir\.env" | Out-File -FilePath $logFile -Append
    
    # Also create a copy in the original backend directory if possible
    $originalBackendDir = Join-Path -Path $scriptDir -ChildPath "backend"
    if (Test-Path -Path $originalBackendDir) {
        try {
            $envContent | Out-File -FilePath "$originalBackendDir\.env" -Encoding ASCII -ErrorAction SilentlyContinue
            Write-Host "Created .env file in original backend directory"
            "Created .env file in original backend directory" | Out-File -FilePath $logFile -Append
        } catch {
            # Ignore error if we can't write to original directory
            Write-Host "Could not write to original backend directory (permission denied), using AppData instead"
            "Could not write to original backend directory (permission denied), using AppData instead" | Out-File -FilePath $logFile -Append
        }
    }
} catch {
    Write-Host "ERROR: Failed to create .env file."
    "ERROR: Failed to create .env file." | Out-File -FilePath $logFile -Append
    $_.Exception.Message | Out-File -FilePath $logFile -Append
    exit 1
}

Write-Host ""
Write-Host "=== PostgreSQL Setup Complete ==="
Write-Host "Database: $dbName"
Write-Host "User: $dbUser"
Write-Host "Port: $dbPort"
Write-Host ""
Write-Host "The database is now ready for the Metis application."
"=== PostgreSQL Setup Complete ===" | Out-File -FilePath $logFile -Append
"Database: $dbName" | Out-File -FilePath $logFile -Append
"User: $dbUser" | Out-File -FilePath $logFile -Append
"Port: $dbPort" | Out-File -FilePath $logFile -Append
"The database is now ready for the Metis application." | Out-File -FilePath $logFile -Append
Write-Host "Setup log saved to: $logFile"
