@echo off
title Talon Trader Funding - Account Server
echo ============================================
echo   TALON TRADER FUNDING - Account Server
echo   Dashboard: http://localhost:5100
echo ============================================
echo.

REM Check if talon_config.json exists and is filled
if not exist talon_config.json (
    echo ERROR: talon_config.json not found!
    echo Please create talon_config.json with your Rithmic credentials.
    pause
    exit /b 1
)

REM Install dependencies if needed
pip show flask-socketio >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install flask flask-socketio cryptography async-rithmic
)

echo Starting server...
echo.
python talon_server.py

pause
