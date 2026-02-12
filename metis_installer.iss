; Metis Installer Script
; Generated with Inno Setup

#define MyAppName "Metis"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Metis Team"
#define MyAppURL "https://github.com/Zeus-Kairos/Metis"
#define MyAppExeName "run_metis.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{12345678-1234-1234-1234-123456789012}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
PrivilegesRequired=lowest
DefaultDirName={userappdata}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=LICENSE
OutputDir=.\installer_output
OutputBaseFilename=metis_setup_{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1
Name: "downloadpython"; Description: "Download and install Python 3.13.12"; GroupDescription: "Prerequisites"; Flags: unchecked
Name: "downloadpostgres"; Description: "Download and install PostgreSQL 18.0"; GroupDescription: "Prerequisites"; Flags: unchecked

[Files]

; Backend files
Source: "packaged_backend\*"; DestDir: "{app}\backend"; Flags: recursesubdirs ignoreversion; Excludes: "*.pyc"

; Frontend files
Source: "dist\*"; DestDir: "{app}\frontend"; Flags: recursesubdirs ignoreversion

; PostgreSQL setup script
Source: "setup_postgres.ps1"; DestDir: "{app}"; Flags: ignoreversion

; Run script
Source: "run_metis.bat"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\run_metis.bat"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\run_metis.bat"; Tasks: desktopicon

[Run]
; Download and install Python
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -Command Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe' -OutFile '{tmp}\python-3.13.12-amd64.exe'; & '{tmp}\python-3.13.12-amd64.exe' /quiet InstallAllUsers=1 PrependPath=1"; Description: "Downloading and installing Python..."; Tasks: downloadpython; Flags: runascurrentuser waituntilterminated

; Download and install PostgreSQL
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -Command Invoke-WebRequest -Uri 'https://get.enterprisedb.com/postgresql/postgresql-18.0-2-windows-x64.exe' -OutFile '{tmp}\postgresql-18.0-2-windows-x64.exe'; & '{tmp}\postgresql-18.0-2-windows-x64.exe' --mode unattended --superpassword postgres --serverport 5432"; Description: "Downloading and installing PostgreSQL..."; Tasks: downloadpostgres; Flags: runascurrentuser waituntilterminated

; Set up PostgreSQL database
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File ""{app}\setup_postgres.ps1"""; Description: "Setting up PostgreSQL database..."; Flags: runasoriginaluser waituntilterminated

; Start Metis application
Filename: "{app}\run_metis.bat"; Description: "Starting Metis application..."; Flags: nowait postinstall shellexec

[UninstallDelete]
Type: filesandordirs; Name: "{app}\backend"
Type: filesandordirs; Name: "{app}\frontend"
Type: files; Name: "{app}\setup_postgres.ps1"
Type: files; Name: "{app}\run_metis.bat"
Type: files; Name: "{app}\.env"
Type: filesandordirs; Name: "{app}\uploads"
