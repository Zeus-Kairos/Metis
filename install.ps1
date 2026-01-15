<#
.SYNOPSIS
  One-command installer for Metis on Windows (PowerShell).

.DESCRIPTION
  - Creates/uses a Conda env (optional) and installs Python deps
  - Installs Node deps
  - Optionally creates the PostgreSQL database + pgvector extension (via setup_db.ps1)
  - Creates a local .env file with sane defaults if it does not exist

.EXAMPLE
  # Recommended (creates DB, creates .env, installs deps)
  .\install.ps1 -DbUser postgres -PromptDbPassword -DatabaseName metis_db

.EXAMPLE
  # Skip DB setup (if you manage DB elsewhere)
  .\install.ps1 -SkipDb
#>

[CmdletBinding()]
param(
  # Where to run the install (repo root). Defaults to the folder containing this script.
  [string]$InstallPath = "",
  [string]$RepoUrl = "https://github.com/Zeus-Kairos/Metis.git",
  [switch]$SkipClone,

  # Conda / Python
  [string]$EnvName = "metis",
  [string]$PythonVersion = "3.13",
  [switch]$SkipConda,

  # Database (PostgreSQL)
  [switch]$SkipDb,
  [string]$DbHost = "localhost",
  [string]$DbPort = "5432",
  [string]$DbUser = "postgres",
  [string]$DbPassword = "",
  [string]$DatabaseName = "metis_db",
  [switch]$PromptDbPassword,

  # Frontend
  [switch]$SkipFrontend,

  # Env file
  [switch]$ForceEnvOverwrite
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step([string]$Message) {
  Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Write-Cmd([string]$CommandLine) {
  Write-Host "    $CommandLine" -ForegroundColor DarkGray
}

function Test-PsqlAvailability {
  try {
    $null = Get-Command psql -ErrorAction Stop
    return $true
  } catch {
    return $false
  }
}
function Assert-Command([string]$Name, [string]$InstallHint) {
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "Missing required command '$Name'. $InstallHint"
  }
}

function Get-ScriptRoot {
  # When invoked from the command line, $PSScriptRoot is the most reliable.
  if ($PSScriptRoot) { return $PSScriptRoot }
  if ($PSCommandPath) { return Split-Path -Parent $PSCommandPath }
  return Split-Path -Parent $MyInvocation.MyCommand.Definition
}

$scriptRoot = Get-ScriptRoot

function New-RandomSecret {
  $bytes = New-Object byte[] 48
  [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
  return [Convert]::ToBase64String($bytes)
}

function Ensure-EnvFile([string]$Path, [string]$DbUri) {
  if ((Test-Path $Path) -and (-not $ForceEnvOverwrite)) {
    Write-Host "Found existing .env; leaving it untouched." -ForegroundColor Yellow
    return
  }

  $secret = New-RandomSecret

  $content = @"
# Metis local configuration

# Database
DB_URI=$DbUri

# Auth
SECRET_KEY=$secret

# Backend server
API_HOST=127.0.0.1
API_PORT=8000

# Logging
LOG_LEVEL=INFO

# RAG
RAG_TYPE=fusion
RAG_K=10

# Uploads
BASE_UPLOAD_DIR=uploads
SUPPORTED_FORMATS=.txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.csv
MAX_FILE_SIZE=104857600
MAX_FILES_PER_UPLOAD=20
"@

  Set-Content -Path $Path -Value $content -Encoding UTF8
  Write-Host "Wrote $Path" -ForegroundColor Green
}

# Decide repo root
if ([string]::IsNullOrWhiteSpace($InstallPath)) {
  $repoRoot = $scriptRoot
} else {
  # If InstallPath doesn't exist, create it.
  if (-not (Test-Path -Path $InstallPath)) {
    New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
  }
  $repoRoot = (Resolve-Path -Path $InstallPath).Path
}

# If user pointed at an empty/non-repo folder, optionally clone into it.
if (-not (Test-Path (Join-Path $repoRoot "requirements.txt")) -or -not (Test-Path (Join-Path $repoRoot "package.json"))) {
  if ($SkipClone) {
    throw "InstallPath '$repoRoot' does not look like the Metis repo root (missing requirements.txt and/or package.json). Remove -SkipClone to allow cloning, or point InstallPath at the repo root."
  }
  Write-Step "Cloning Metis into '$repoRoot'"
  Assert-Command -Name "git" -InstallHint "Install Git: https://git-scm.com/download/win"

  if (-not (Test-Path $repoRoot)) {
    New-Item -ItemType Directory -Path $repoRoot | Out-Null
  }

  # Clone into the directory itself (repoRoot)
  & git clone $RepoUrl $repoRoot | Out-Host
}

Set-Location $repoRoot

Write-Step "Checking prerequisites"
Assert-Command -Name "npm" -InstallHint "Install Node.js (includes npm): https://nodejs.org/en/download"

if (-not $SkipConda) {
  Assert-Command -Name "conda" -InstallHint "Install Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install"
}

Write-Step "Preparing .env"
if ($PromptDbPassword -or [string]::IsNullOrWhiteSpace($DbPassword)) {
  if (-not $SkipDb) {
    $DbPassword = Read-Host "Enter PostgreSQL password for user '$DbUser'"
  }
}

$dbUriUserPart = $DbUser
if (-not [string]::IsNullOrWhiteSpace($DbPassword)) {
  # Encode a few characters that commonly break URLs
  $encodedPw = [System.Uri]::EscapeDataString($DbPassword)
  $dbUriUserPart = "$DbUser`:$encodedPw"
}
$dbUri = "postgresql://$dbUriUserPart@$DbHost`:$DbPort/$DatabaseName"
Ensure-EnvFile -Path (Join-Path $repoRoot ".env") -DbUri $dbUri

if (-not $SkipConda) {
  Write-Step "Creating/using Conda env '$EnvName' (Python $PythonVersion)"
  $envList = & conda env list 2>$null
  $envExists = $false
  if ($envList) {
    $match = $envList | Select-String -SimpleMatch " $EnvName " -ErrorAction SilentlyContinue
    $envExists = $null -ne $match
  }
  if (-not $envExists) {
    & conda create -n $EnvName "python=$PythonVersion" -y | Out-Host
  } else {
    Write-Host "Conda env '$EnvName' already exists." -ForegroundColor Yellow
  }

  Write-Step "Installing backend dependencies (pip)"
  $pipVerbosity = @()
  if ($PSBoundParameters.ContainsKey('Verbose')) { $pipVerbosity = @("-v") }

  Write-Cmd "conda run -n $EnvName python -m pip install --upgrade pip $($pipVerbosity -join ' ')"
  & conda run -n $EnvName python -m pip install --upgrade pip @pipVerbosity | Out-Host

  $reqPath = (Join-Path $repoRoot "requirements.txt")
  Write-Cmd "conda run -n $EnvName python -m pip install -r `"$reqPath`" $($pipVerbosity -join ' ')"
  & conda run -n $EnvName python -m pip install -r $reqPath @pipVerbosity | Out-Host
} else {
  Write-Step "Installing backend dependencies (system Python)"
  Assert-Command -Name "python" -InstallHint "Install Python 3.10+ or use Conda (recommended)."
  $pipVerbosity = @()
  if ($PSBoundParameters.ContainsKey('Verbose')) { $pipVerbosity = @("-v") }

  Write-Cmd "python -m pip install --upgrade pip $($pipVerbosity -join ' ')"
  & python -m pip install --upgrade pip @pipVerbosity | Out-Host

  $reqPath = (Join-Path $repoRoot "requirements.txt")
  Write-Cmd "python -m pip install -r `"$reqPath`" $($pipVerbosity -join ' ')"
  & python -m pip install -r $reqPath @pipVerbosity | Out-Host
}

if (-not $SkipFrontend) {
  Write-Step "Installing frontend dependencies (npm)"
  & npm install | Out-Host
}

if (-not $SkipDb) {
  Write-Step "Setting up PostgreSQL database (inline)"

  if (-not (Test-PsqlAvailability)) {
    throw "psql is not installed or not in PATH. Please ensure PostgreSQL client tools are installed and added to your PATH. Typical Windows path: 'C:\Program Files\PostgreSQL\<version>\bin'"
  }

  # Use the same password we already gathered for .env
  if ($PromptDbPassword -or ([string]::IsNullOrWhiteSpace($DbPassword) -and -not $SkipDb)) {
    $DbPassword = Read-Host "Enter PostgreSQL password for user '$DbUser'"
  }

  # Set PGPASSWORD for psql child processes
  if (-not [string]::IsNullOrEmpty($DbPassword)) {
    $env:PGPASSWORD = $DbPassword
  }

  $psqlBase = "psql -h $DbHost -p $DbPort -U $DbUser"

  Write-Cmd "$psqlBase -d postgres -c '\q'"
  Invoke-Expression -Command "$psqlBase -d postgres -c `"\q`"" 2>&1 | Out-Null
  if (-not $?) {
    Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
    $hostPort = "$DbHost`:$DbPort"
    throw "Could not connect to PostgreSQL server at $hostPort as user $DbUser. Check host, port, and credentials."
  }

  Write-Host "Connected to PostgreSQL server successfully!" -ForegroundColor Green

  Write-Host "`nChecking if database '$DatabaseName' exists..." -ForegroundColor Cyan
  $checkDbCmd = "$psqlBase -d postgres -tAc `"SELECT 1 FROM pg_database WHERE datname = '$DatabaseName'`""
  Write-Cmd $checkDbCmd
  $dbExists = Invoke-Expression -Command $checkDbCmd | Select-String -Pattern "1" -Quiet

  if ($dbExists) {
    Write-Host "Database '$DatabaseName' already exists." -ForegroundColor Yellow
  } else {
    Write-Host "Creating database '$DatabaseName'..." -ForegroundColor Cyan
    $createDbCmd = "$psqlBase -d postgres -c `"CREATE DATABASE $DatabaseName`""
    Write-Cmd $createDbCmd
    Invoke-Expression -Command $createDbCmd | Out-Host
    Write-Host "Database '$DatabaseName' created successfully!" -ForegroundColor Green
  }

  Write-Host "`nEnabling vector extension in database '$DatabaseName'..." -ForegroundColor Cyan
  $enableVectorCmd = "$psqlBase -d $DatabaseName -c `"CREATE EXTENSION IF NOT EXISTS vector`""
  Write-Cmd $enableVectorCmd
  Invoke-Expression -Command $enableVectorCmd | Out-Host

  Write-Host "Verifying vector extension..." -ForegroundColor Cyan
  $verifyVectorCmd = "$psqlBase -d $DatabaseName -tAc `"SELECT extname FROM pg_extension WHERE extname = 'vector'`""
  Write-Cmd $verifyVectorCmd
  $vectorEnabled = Invoke-Expression -Command $verifyVectorCmd | Select-String -Pattern "vector" -Quiet

  if ($vectorEnabled) {
    Write-Host "Vector extension is successfully enabled!" -ForegroundColor Green
  } else {
    Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
    throw "Vector extension is not enabled."
  }

  Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
}

Write-Step "Done"
Write-Host "Next:" -ForegroundColor Green
Write-Host "  - Backend: python main.py (or: conda activate $EnvName; python main.py)" -ForegroundColor Yellow
Write-Host "  - Frontend: npm run dev" -ForegroundColor Yellow
