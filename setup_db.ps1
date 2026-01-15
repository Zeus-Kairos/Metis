<#
PowerShell script to create a PostgreSQL database and enable the vector extension for Metis.
#>

param(
    [string]$DbHost = "localhost",
    [int]$Port = 5432,
    [string]$User = "postgres",
    [string]$Password = "",
    [string]$DatabaseName = "metis_db",
    [switch]$PromptPassword
)

# Set strict mode
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Function to check if psql is available
function Test-PsqlAvailability {
    try {
        $null = Get-Command psql -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

# Check if psql is installed
if (-not (Test-PsqlAvailability)) {
    Write-Error "psql is not installed or not in PATH. Please ensure PostgreSQL client tools are installed and added to your PATH."
    Write-Host "PostgreSQL is usually installed at: C:\Program Files\PostgreSQL\<version>\bin" -ForegroundColor Yellow
    exit 1
}

# Prompt for password if requested
if ($PromptPassword -or [string]::IsNullOrEmpty($Password)) {
    # Read password as plain text string for simplicity
    $Password = Read-Host "Enter PostgreSQL password for user '$User'"
}

# Set PGPASSWORD environment variable
$env:PGPASSWORD = $Password

# Test connection to PostgreSQL server
Write-Host "Testing connection to PostgreSQL server at ${DbHost}:${Port}..." -ForegroundColor Cyan
$testCommand = "psql -h ${DbHost} -p ${Port} -U ${User} -d postgres -c `"\q`""
$testResult = Invoke-Expression -Command $testCommand 2>&1

if (-not $?) {
    Write-Error "Could not connect to PostgreSQL server. Please check your host, port, and credentials."
    exit 1
}

Write-Host "Connected to PostgreSQL server successfully!" -ForegroundColor Green

# Check if database already exists
Write-Host "\nChecking if database '${DatabaseName}' exists..." -ForegroundColor Cyan
$checkDbCommand = "psql -h ${DbHost} -p ${Port} -U ${User} -d postgres -tAc `"SELECT 1 FROM pg_database WHERE datname = '${DatabaseName}'`""
$dbExists = Invoke-Expression -Command $checkDbCommand | Select-String -Pattern "1" -Quiet

if ($dbExists) {
    Write-Host "Database '${DatabaseName}' already exists." -ForegroundColor Yellow
} else {
    Write-Host "Creating database '${DatabaseName}'..." -ForegroundColor Cyan
    $createDbCommand = "psql -h ${DbHost} -p ${Port} -U ${User} -d postgres -c `"CREATE DATABASE ${DatabaseName}`""
    Invoke-Expression -Command $createDbCommand | Out-Null
    Write-Host "Database '${DatabaseName}' created successfully!" -ForegroundColor Green
}

# Enable vector extension
Write-Host "\nEnabling vector extension in database '${DatabaseName}'..." -ForegroundColor Cyan
$enableVectorCommand = "psql -h ${DbHost} -p ${Port} -U ${User} -d ${DatabaseName} -c `"CREATE EXTENSION IF NOT EXISTS vector`""
Invoke-Expression -Command $enableVectorCommand | Out-Null

# Verify vector extension is enabled
Write-Host "Verifying vector extension..." -ForegroundColor Cyan
$verifyVectorCommand = "psql -h ${DbHost} -p ${Port} -U ${User} -d ${DatabaseName} -tAc `"SELECT extname FROM pg_extension WHERE extname = 'vector'`""
$vectorEnabled = Invoke-Expression -Command $verifyVectorCommand | Select-String -Pattern "vector" -Quiet

if ($vectorEnabled) {
    Write-Host "Vector extension is successfully enabled!" -ForegroundColor Green
} else {
    Write-Error "Vector extension is not enabled."
    exit 1
}

# Clean up PGPASSWORD
Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue

Write-Host "\n🎉 Database setup completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Database: ${DatabaseName}" -ForegroundColor Yellow
Write-Host "Host: ${DbHost}" -ForegroundColor Yellow
Write-Host "Port: ${Port}" -ForegroundColor Yellow
Write-Host "User: ${User}" -ForegroundColor Yellow
Write-Host ""
Write-Host "Add this to your .env file:" -ForegroundColor Cyan
Write-Host "DB_URI=postgresql://${User}@${DbHost}:${Port}/${DatabaseName}" -ForegroundColor Yellow
Write-Host ""
if (-not [string]::IsNullOrEmpty($Password)) {
    Write-Host "If you set a password, include it in the DB_URI like:" -ForegroundColor Cyan
    Write-Host "DB_URI=postgresql://${User}:${Password}@${DbHost}:${Port}/${DatabaseName}" -ForegroundColor Yellow
}
