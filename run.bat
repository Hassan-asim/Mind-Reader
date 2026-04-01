@echo off
echo ========================================
echo   MIND READER AI - Starting...
echo ========================================
echo.

echo Starting Backend on http://localhost:3001
start "Mind Reader Backend" cmd /k "cd backend && venv\Scripts\activate && python app.py"

timeout /t 3 /nobreak > nul

echo Starting Frontend on http://localhost:3000
start "Mind Reader Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo   Application starting...
echo   Backend: http://localhost:3001
echo   Frontend: http://localhost:3000
echo ========================================
