@echo off
setlocal enabledelayedexpansion

REM Получаем текущую ветку
for /f "delims=" %%b in ('git symbolic-ref --short HEAD') do set "branch_name=%%b"

echo 🔍 Проверка ветки: %branch_name%

REM Запрещённые ветки
if "%branch_name%"=="main" (
    echo ❌ Ошибка: Коммиты в ветку "main" запрещены!
    exit /b 1
)

if "%branch_name%"=="develop" (
    echo ❌ Ошибка: Коммиты в ветку "develop" запрещены!
    exit /b 1
)

echo ✅ Коммит разрешён в ветку "%branch_name%".
exit /b 0
