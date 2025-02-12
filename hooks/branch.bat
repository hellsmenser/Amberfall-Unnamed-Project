@echo off
setlocal enabledelayedexpansion

for /f "delims=" %%b in ('git symbolic-ref --short HEAD') do set "branch_name=%%b"

echo 🔍 Проверка ветки: %branch_name%

REM Если это main или develop, коммит разрешён
if "%branch_name%"=="main" exit /b 0
if "%branch_name%"=="develop" exit /b 0

REM Если ветка начинается с feature/, bugfix/, hotfix/ или release/, коммит разрешён
echo %branch_name% | findstr /R "^feature/ ^bugfix/ ^hotfix/ ^release/" >nul
if %errorlevel%==0 exit /b 0

echo ❌ Ошибка: Ветка "%branch_name%" нарушает правила именования! Коммит запрещён.
exit /b 1
