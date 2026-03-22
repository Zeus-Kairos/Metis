[CmdletBinding()]
param(
  [switch]$InstallPyInstaller,
  [switch]$SkipReleaseBuild,
  [switch]$SkipFrontend,
  [switch]$SkipBackend,
  [switch]$NoClean,
  [switch]$SkipCompile,
  [string]$CondaEnvName = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step([string]$Message) {
  Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Get-ScriptRoot {
  if ($PSScriptRoot) { return $PSScriptRoot }
  if ($PSCommandPath) { return Split-Path -Parent $PSCommandPath }
  return Split-Path -Parent $MyInvocation.MyCommand.Definition
}

function Resolve-IsccPath {
  $isccFromPath = Get-Command ISCC.exe -ErrorAction SilentlyContinue
  if ($isccFromPath) {
    return $isccFromPath.Source
  }

  $candidates = @(
    "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe",
    "${env:ProgramFiles}\Inno Setup 6\ISCC.exe"
  )

  foreach ($candidate in $candidates) {
    if ([string]::IsNullOrWhiteSpace($candidate)) { continue }
    if (Test-Path -LiteralPath $candidate) {
      return $candidate
    }
  }

  throw "ISCC.exe not found. Install Inno Setup 6 or add ISCC.exe to PATH."
}

$repoRoot = Get-ScriptRoot
Set-Location $repoRoot

$releaseBuilder = Join-Path $repoRoot "build_release.ps1"
$installerScript = Join-Path $repoRoot "metis_installer.iss"

if (-not (Test-Path -LiteralPath $releaseBuilder)) {
  throw "Missing '$releaseBuilder'."
}
if (-not (Test-Path -LiteralPath $installerScript)) {
  throw "Missing '$installerScript'."
}

if (-not $SkipReleaseBuild) {
  Write-Step "Building release artifacts"
  $releaseArgs = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $releaseBuilder)
  if ($InstallPyInstaller) { $releaseArgs += "-InstallPyInstaller" }
  if ($SkipFrontend) { $releaseArgs += "-SkipFrontend" }
  if ($SkipBackend) { $releaseArgs += "-SkipBackend" }
  if ($NoClean) { $releaseArgs += "-NoClean" }
  if (-not [string]::IsNullOrWhiteSpace($CondaEnvName)) { $releaseArgs += @("-CondaEnvName", $CondaEnvName) }

  & powershell @releaseArgs
  if ($LASTEXITCODE -ne 0) {
    throw "build_release.ps1 failed."
  }
}

if (-not $SkipCompile) {
  Write-Step "Compiling Inno Setup installer"
  $isccPath = Resolve-IsccPath

  & $isccPath $installerScript
  if ($LASTEXITCODE -ne 0) {
    throw "Installer compilation failed."
  }
}

$outputDir = Join-Path $repoRoot "installer_output"
Write-Step "Done"
if (Test-Path -LiteralPath $outputDir) {
  Write-Host "Installer output: $outputDir" -ForegroundColor Green
} else {
  Write-Host "Installer compilation was skipped or output directory not created yet." -ForegroundColor Yellow
}
