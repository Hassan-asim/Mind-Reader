@echo off
echo ========================================
echo   MIND READER AI - Setup Script
echo ========================================
echo.

echo [1/3] Setting up Python backend...
cd backend
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate
echo Installing Python dependencies...
pip install -r requirements.txt
cd ..

echo.
echo [2/3] Setting up Node.js frontend...
cd frontend
echo Installing Node.js dependencies...
call npm install
cd ..

echo.
echo [3/3] Setup complete!
echo.
echo ========================================
echo   To run the application:
echo ========================================
echo.
echo   1. Open TWO terminal windows
echo.
echo   2. In first terminal (Backend):
echo      cd backend
echo      venv\Scripts\activate
echo      python app.py
echo.
echo   3. In second terminal (Frontend):
echo      cd frontend
echo      npm run dev
echo.
echo   4. Open browser to http://localhost:3000
echo ========================================
echo.
pause
