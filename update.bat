@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

REM Название виртуального окружения
set VENV_DIR=venv

REM Проверка наличия виртуального окружения
if not exist "%VENV_DIR%\\Scripts\\activate" (
    echo [!] Виртуальное окружение не найдено. Пожалуйста, создайте его с помощью setup_env.bat
    exit /b 1
)

REM Активация виртуального окружения
call %VENV_DIR%\\Scripts\\activate.bat

REM Проверка наличия файла req.txt
if not exist req.txt (
    echo [!] Файл req.txt не найден в текущей директории.
    exit /b 1
)

echo [*] Проверка установленных библиотек...

REM Проверка установленных зависимостей
pip check > nul 2>&1
if %errorlevel% NEQ 0 (
    echo [!] Обнаружены проблемы с установленными пакетами. Установка/обновление зависимостей...
    pip install --upgrade pip
    pip install -r req.txt
    if %errorlevel% NEQ 0 (
        echo [!] Ошибка при установке зависимостей.
        exit /b 1
    )
    echo [*] Зависимости успешно установлены и обновлены.
) else (
    echo [*] Все зависимости установлены корректно.
)

echo 🔄 Обновление pre-commit хуков...
pre-commit uninstall
pre-commit install
pre-commit run --all-files
echo ✅ Pre-commit хуки обновлены.


REM Деактивация виртуального окружения
deactivate

echo [*] Проверка завершена.
endlocal
