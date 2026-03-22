[CmdletBinding()]
param(
  [switch]$SkipFrontend,
  [switch]$SkipBackend,
  [switch]$NoClean,
  [switch]$InstallPyInstaller,
  [string]$CondaEnvName = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step([string]$Message) {
  Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Assert-Command([string]$Name, [string]$InstallHint) {
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "Missing required command '$Name'. $InstallHint"
  }
}

function Get-ScriptRoot {
  if ($PSScriptRoot) { return $PSScriptRoot }
  if ($PSCommandPath) { return Split-Path -Parent $PSCommandPath }
  return Split-Path -Parent $MyInvocation.MyCommand.Definition
}

function New-DirectoryIfMissing([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
  }
}

function Test-PyInstallerInstalled {
  Invoke-PythonInBuildEnv -Arguments @("-m", "PyInstaller", "--version") *> $null
  return ($LASTEXITCODE -eq 0)
}

function Test-PythonModuleInstalled([string]$ModuleName) {
  Invoke-PythonInBuildEnv -Arguments @("-c", "import $ModuleName") *> $null
  return ($LASTEXITCODE -eq 0)
}

function Invoke-PythonInBuildEnv([string[]]$Arguments) {
  $pythonArgs = @("-s") + $Arguments
  if ([string]::IsNullOrWhiteSpace($CondaEnvName)) {
    & python @pythonArgs
  } else {
    & conda run -n $CondaEnvName python @pythonArgs
  }
}

function Invoke-FrontendBuild([string]$RepoRoot, [string]$FrontendReleasePath) {
  Write-Step "Building frontend"
  Assert-Command -Name "npm" -InstallHint "Install Node.js (includes npm): https://nodejs.org/en/download"

  $nodeModulesPath = Join-Path $RepoRoot "node_modules"
  if (-not (Test-Path -LiteralPath $nodeModulesPath)) {
    Write-Host "node_modules missing; running npm install..." -ForegroundColor Yellow
    & npm install
    if ($LASTEXITCODE -ne 0) { throw "npm install failed." }
  }

  & npm run build
  if ($LASTEXITCODE -ne 0) { throw "npm run build failed." }

  $distPath = Join-Path $RepoRoot "dist"
  if (-not (Test-Path -LiteralPath $distPath)) {
    throw "Frontend build output not found at '$distPath'."
  }

  New-DirectoryIfMissing -Path $FrontendReleasePath
  Copy-Item -Path (Join-Path $distPath "*") -Destination $FrontendReleasePath -Recurse -Force
}

function Invoke-BackendBuild([string]$RepoRoot, [string]$BackendReleasePath, [bool]$AllowInstallPyInstaller) {
  Write-Step "Packaging backend (PyInstaller)"
  if ([string]::IsNullOrWhiteSpace($CondaEnvName)) {
    Assert-Command -Name "python" -InstallHint "Install Python 3.10+ and add it to PATH."
  } else {
    Assert-Command -Name "conda" -InstallHint "Install Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install"
    Write-Host "Using Conda environment '$CondaEnvName' for backend packaging." -ForegroundColor Yellow
  }

  if (-not (Test-PyInstallerInstalled)) {
    if ($AllowInstallPyInstaller) {
      Write-Host "PyInstaller not found; installing with pip..." -ForegroundColor Yellow
      Invoke-PythonInBuildEnv -Arguments @("-m", "pip", "install", "pyinstaller")
      if ($LASTEXITCODE -ne 0) { throw "Failed to install PyInstaller." }
    } else {
      throw "PyInstaller is not installed in the build environment. Run: python -m pip install pyinstaller (or rerun this script with -InstallPyInstaller)."
    }
  }

  if (-not (Test-PythonModuleInstalled -ModuleName "faiss")) {
    throw "Python module 'faiss' is missing in the packaging environment. Install it in the same interpreter/env used for build: python -m pip install faiss-cpu"
  }
  if (-not (Test-PythonModuleInstalled -ModuleName "pymupdf.layout")) {
    throw "Python module 'pymupdf.layout' is missing in the packaging environment. Install it in the same interpreter/env used for build: python -m pip install pymupdf-layout pymupdf4llm"
  }
  if (-not (Test-PythonModuleInstalled -ModuleName "passlib.handlers.argon2")) {
    throw "Python module 'passlib.handlers.argon2' is missing in the packaging environment. Install it in the same interpreter/env used for build: python -m pip install passlib[argon2] argon2-cffi"
  }
  if (-not (Test-PythonModuleInstalled -ModuleName "magika")) {
    throw "Python module 'magika' is missing in the packaging environment. Install it in the same interpreter/env used for build: python -m pip install magika"
  }
  Invoke-PythonInBuildEnv -Arguments @("-c", "from langchain_core.language_models import LanguageModelInput; from langchain_ollama.chat_models import ChatOllama; from langchain_ollama.embeddings import OllamaEmbeddings")
  if ($LASTEXITCODE -ne 0) {
    throw "langchain_ollama/langchain_core compatibility check failed in the packaging environment. Reinstall these packages in the same env, then rebuild."
  }

  $entryScript = Join-Path $RepoRoot "main.py"
  if (-not (Test-Path -LiteralPath $entryScript)) {
    throw "Backend entry script not found at '$entryScript'."
  }

  $pyiDist = Join-Path $RepoRoot "dist"
  $pyiBuild = Join-Path $RepoRoot "build"
  $specFile = Join-Path $RepoRoot "metis_backend.spec"

  $pyInstallerArgs = @(
    "-m", "PyInstaller",
    "--noconfirm",
    "--clean",
    "--onedir",
    "--name", "metis_backend",
    "--exclude-module", "transformers",
    "--exclude-module", "torch",
    "--paths", $RepoRoot,
    "--collect-submodules", "src",
    "--collect-all", "faiss",
    "--collect-all", "magika",
    "--collect-all", "pymupdf",
    "--collect-all", "pymupdf4llm",
    "--collect-all", "langchain_ollama",
    "--collect-all", "langchain_core",
    "--collect-submodules", "passlib.handlers",
    "--hidden-import", "faiss",
    "--hidden-import", "passlib.handlers.argon2",
    "--hidden-import", "src.api.main",
    "--hidden-import", "langchain_openai",
    "--hidden-import", "langchain_huggingface",
    "--hidden-import", "langchain_ollama.chat_models",
    "--hidden-import", "langchain_ollama.embeddings",
    "--hidden-import", "uvicorn.logging",
    "--hidden-import", "uvicorn.loops.auto",
    "--hidden-import", "uvicorn.protocols.http.auto",
    "--hidden-import", "uvicorn.protocols.websockets.auto",
    "--hidden-import", "uvicorn.lifespan.on",
    $entryScript
  )
  Invoke-PythonInBuildEnv -Arguments $pyInstallerArgs

  if ($LASTEXITCODE -ne 0) { throw "PyInstaller packaging failed." }

  $packagedBackendPath = Join-Path $pyiDist "metis_backend"
  if (-not (Test-Path -LiteralPath $packagedBackendPath)) {
    throw "Packaged backend not found at '$packagedBackendPath'."
  }

  New-DirectoryIfMissing -Path $BackendReleasePath
  Copy-Item -Path (Join-Path $packagedBackendPath "*") -Destination $BackendReleasePath -Recurse -Force

  if (Test-Path -LiteralPath $pyiBuild) {
    Remove-Item -LiteralPath $pyiBuild -Recurse -Force
  }
  if (Test-Path -LiteralPath $specFile) {
    Remove-Item -LiteralPath $specFile -Force
  }
}

$repoRoot = Get-ScriptRoot
Set-Location $repoRoot

$releaseRoot = Join-Path $repoRoot "release"
$backendReleasePath = Join-Path $releaseRoot "backend"
$frontendReleasePath = Join-Path $releaseRoot "frontend"

if ((Test-Path -LiteralPath $releaseRoot) -and (-not $NoClean)) {
  Write-Step "Cleaning existing release directory"
  Remove-Item -LiteralPath $releaseRoot -Recurse -Force
}

New-DirectoryIfMissing -Path $releaseRoot

if (-not $SkipFrontend) {
  Invoke-FrontendBuild -RepoRoot $repoRoot -FrontendReleasePath $frontendReleasePath
}

if (-not $SkipBackend) {
  Invoke-BackendBuild -RepoRoot $repoRoot -BackendReleasePath $backendReleasePath -AllowInstallPyInstaller:$InstallPyInstaller
}

Write-Step "Validating release artifacts"
if (-not $SkipFrontend) {
  $frontendIndex = Join-Path $frontendReleasePath "index.html"
  if (-not (Test-Path -LiteralPath $frontendIndex)) {
    throw "release\frontend\index.html is missing."
  }
}
if (-not $SkipBackend) {
  $backendExe = Join-Path $backendReleasePath "metis_backend.exe"
  if (-not (Test-Path -LiteralPath $backendExe)) {
    throw "release\backend\metis_backend.exe is missing."
  }
}

Write-Step "Release package prepared successfully"
Write-Host "Release folder: $releaseRoot" -ForegroundColor Green
Write-Host "Next: compile installer with metis_installer.iss" -ForegroundColor Yellow
