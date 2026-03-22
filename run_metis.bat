@echo off

rem Metis Application Startup Script

echo === Starting Metis Application ===
echo.

rem Change to the backend directory
cd "%~dp0backend"

rem Start the backend server
echo Starting backend server...
echo The server will run in a new window.
echo.
if exist "metis_backend.exe" (
    start "Metis Backend" "%~dp0backend\metis_backend.exe"
) else (
    rem Fallback for development mode
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERROR: Neither metis_backend.exe nor Python is available.
        echo Please rebuild release backend or install Python 3.10+.
        pause
        exit /b 1
    )
    start "Metis Backend" python main.py
)

rem Wait a few seconds for the server to start
echo Waiting for backend server to start...
timeout /t 5 /nobreak >nul

rem Start frontend web server
echo Starting frontend web server...
echo.
start "Metis Frontend Server" cmd /c "cd "%~dp0frontend" && python -m http.server 5173"

rem Wait a few seconds for the frontend server to start
echo Waiting for frontend server to start...
timeout /t 3 /nobreak >nul

rem Open the frontend in default web browser
echo Opening frontend in web browser...
echo.
start "Metis Frontend" "http://localhost:5173"

echo === Metis Application Started ===
echo.
echo Backend server is running in a separate window.
echo Frontend should open in your default web browser.
echo.
echo To stop the application, close the backend server window.
echo.
pause
