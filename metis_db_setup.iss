; Metis Database Setup Inno Script
; Checks if PostgreSQL is installed and configures the database using PostgreSQL command line tools

[Setup]
AppId={{5A2E4F5D-1234-4567-89AB-CDEF01234567}}
AppName=Metis Database Setup
AppVersion=0.0.1
DefaultDirName={pf}\Metis
DefaultGroupName=Metis
OutputBaseFilename=metis-db-setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
WizardStyle=modern

[Files]
; No files to install - using existing PostgreSQL tools

[Registry]
; No registry entries needed

[Code]
var
  PostgreSQLBinPath: string;
  PostgresPassword: string;

// Configuration: Set your PostgreSQL postgres user password here
// This will be used for database creation and configuration
procedure InitializePostgresPassword;
begin
  // Change this to your actual PostgreSQL postgres user password
  PostgresPassword := 'postgres';
end;

function GetPostgreSQLInstallPath: string;
var
  RegPath: string;
  Names: TArrayOfString;
  I: Integer;
begin
  Result := '';
  RegPath := 'SOFTWARE\PostgreSQL\Installations';

  // Use HKLM64 to access the 64-bit registry area where 64-bit Postgres lives
  if RegKeyExists(HKLM64, RegPath) then
  begin
    if RegGetSubkeyNames(HKLM64, RegPath, Names) then
    begin
      for I := 0 to GetArrayLength(Names) - 1 do
      begin
        if RegQueryStringValue(HKLM64, RegPath + '\' + Names[I], 'Base Directory', Result) then
        begin
          Result := AddBackslash(Result) + 'bin';
          exit;
        end;
      end;
    end;
  end;

  // Check 32-bit registry area (standard HKLM for 32-bit apps)
  if RegKeyExists(HKEY_LOCAL_MACHINE, RegPath) then
  begin
    if RegGetSubkeyNames(HKEY_LOCAL_MACHINE, RegPath, Names) then
    begin
      for I := 0 to GetArrayLength(Names) - 1 do
      begin
        if RegQueryStringValue(HKEY_LOCAL_MACHINE, RegPath + '\' + Names[I], 'Base Directory', Result) then
        begin
          Result := AddBackslash(Result) + 'bin';
          exit;
        end;
      end;
    end;
  end;
end;

function IsPostgreSQLInstalled: Boolean;
begin
  PostgreSQLBinPath := GetPostgreSQLInstallPath;
  Result := (PostgreSQLBinPath <> '') and FileExists(PostgreSQLBinPath + '\psql.exe');
end;

function GetPostgreSQLBinPath(Param: string): string;
begin
  Result := PostgreSQLBinPath;
end;

function GetPostgresPassword(Param: string): string;
begin
  Result := PostgresPassword;
end;

procedure InitializeWizard;
begin
  if not IsPostgreSQLInstalled then
  begin
    // Debug message to show what path was detected
    MsgBox('PostgreSQL not detected.' + #13#10 + 'Detected path: ' + PostgreSQLBinPath + #13#10 + 'Please install PostgreSQL 13.x or higher and try again.', mbError, MB_OK);
    WizardForm.Close;
  end else
  begin
    // Initialize PostgreSQL password
    InitializePostgresPassword;
    
    // Show detected path for debugging
    MsgBox('PostgreSQL detected at: ' + PostgreSQLBinPath + #13#10 + 'Using postgres password: ' + PostgresPassword, mbInformation, MB_OK);
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  EnvContent: string;
  AppDataDir: string;
  BackendDir: string;
  SecretKey: string;
  I: Integer;
  Chars: string;
  RandomChar: Integer;
begin
  if CurStep = ssDone then
  begin
    // Generate random secret key
    Chars := 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?';
    SecretKey := '';
    for I := 1 to 32 do
    begin
      RandomChar := Random(Length(Chars)) + 1;
      SecretKey := SecretKey + Chars[RandomChar];
    end;
    
    // Create .env file content
    EnvContent := '# Database Configuration' + #13#10 +
      'DB_URI=postgresql://metis_user:metis_password_2026@localhost:5432/metis_db' + #13#10 + #13#10 +
      '# JWT Authentication' + #13#10 +
      'SECRET_KEY=' + SecretKey + #13#10 + #13#10 +
      '# Metis local configuration' + #13#10 +
      'LLM_PROVIDER=ollama' + #13#10 +
      'LLM_API_KEY=your_api_key' + #13#10 +
      'LLM_MODEL=gpt-oss:20b-cloud' + #13#10 +
      'LLM_BASE_URL=http://localhost:11434' + #13#10 +
      'EMBED_PROVIDER=ollama' + #13#10 +
      'EMBED_API_KEY=your_api_key' + #13#10 +
      'EMBED_MODEL=nomic-embed-text:latest' + #13#10 + #13#10 +
      '# File Upload Configuration' + #13#10 +
      'BASE_UPLOAD_DIR=' + ExpandConstant('{localappdata}') + '\Metis\uploads' + #13#10 +
      'SUPPORTED_FORMATS=.txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.csv' + #13#10 +
      'MAX_FILE_SIZE=104857600' + #13#10 +
      'MAX_FILES_PER_UPLOAD=20' + #13#10 + #13#10 +
      '# Logging' + #13#10 +
      'LOG_LEVEL=INFO' + #13#10 + #13#10 +
      '# RAG Configuration' + #13#10 +
      'RAG_TYPE=agentic' + #13#10 +
      'RAG_K=10';
    
    // Create AppData directory structure
    AppDataDir := ExpandConstant('{localappdata}') + '\Metis';
    BackendDir := AppDataDir + '\backend';
    
    // Create directories if they don't exist
    if not DirExists(AppDataDir) then
      CreateDir(AppDataDir);
    if not DirExists(BackendDir) then
      CreateDir(BackendDir);
    if not DirExists(AppDataDir + '\uploads') then
      CreateDir(AppDataDir + '\uploads');
    
    // Write .env file
    SaveStringToFile(BackendDir + '\.env', EnvContent, False);
    
    // Also create .env in the application directory
    if DirExists(ExpandConstant('{app}')) then
      SaveStringToFile(ExpandConstant('{app}') + '\.env', EnvContent, False);
  end;
end;

[Run]
; Create database if it doesn't exist
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -t -c ""SELECT 1 FROM pg_database WHERE datname = 'metis_db'"" | findstr /i ""1"" > nul || ""{code:GetPostgreSQLBinPath|}\createdb.exe"" -h localhost -U postgres metis_db"; Check: IsPostgreSQLInstalled; Flags: runhidden

; Create user if it doesn't exist
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -t -c ""SELECT 1 FROM pg_roles WHERE rolname = 'metis_user'"" | findstr /i ""1"" > nul || ""{code:GetPostgreSQLBinPath|}\createuser.exe"" -h localhost -U postgres metis_user"; Check: IsPostgreSQLInstalled; Flags: runhidden

; Set user password
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -c ""ALTER USER metis_user WITH PASSWORD 'metis_password_2026'"""; Check: IsPostgreSQLInstalled; Flags: runhidden

; Grant privileges on database
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -c ""GRANT ALL PRIVILEGES ON DATABASE metis_db TO metis_user"""; Check: IsPostgreSQLInstalled; Flags: runhidden

; Alter user to have CREATEDB permission
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -c ""ALTER USER metis_user CREATEDB"""; Check: IsPostgreSQLInstalled; Flags: runhidden

; Grant schema privileges
Filename: "cmd.exe"; Parameters: "/c set ""PGPASSWORD={code:GetPostgresPassword}""&&""{code:GetPostgreSQLBinPath|}\psql.exe"" -h localhost -U postgres -d metis_db -c ""GRANT ALL ON SCHEMA public TO metis_user"""; Check: IsPostgreSQLInstalled; Flags: runhidden