@echo off
echo 🔍 Проверка кода линтером...

REM Получаем список изменённых файлов
for /f "delims=" %%f in ('git diff --cached --name-only --diff-filter=ACM ^| findstr /R "\.py$"') do (
    set "files=%%f %files%"
)

REM Если нет Python-файлов, выходим
if not defined files (
    echo ✅ Нет файлов Python для проверки.
    exit /b 0
)

REM Запускаем flake8
flake8 %files%

REM Если flake8 нашел ошибки, запрещаем коммит
if errorlevel 1 (
    echo ❌ Линтер обнаружил ошибки. Исправьте их перед коммитом.
    exit /b 1
)

echo ✅ Линтер не нашёл ошибок. Коммит разрешён.
exit /b 0
