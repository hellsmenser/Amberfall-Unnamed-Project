@echo off
setlocal

REM Название виртуального окружения
set VENV_DIR=venv

REM Проверка наличия виртуального окружения
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [*] Виртуальное окружение не найдено. Создание нового...
    python -m venv %VENV_DIR%
    if errorlevel 1 (
        echo [!] Ошибка при создании виртуального окружения.
        exit /b 1
    )
) else (
    echo [*] Виртуальное окружение уже существует.
)

REM Активация виртуального окружения
call %VENV_DIR%\Scripts\activate.bat

REM Установка зависимостей
if exist req.txt (
    echo [*] Установка зависимостей из req.txt...
    pip install --upgrade pip
    pip install -r req.txt
    if errorlevel 1 (
        echo [!] Ошибка при установке зависимостей.
        exit /b 1
    )
    echo [*] Зависимости успешно установлены.
) else (
    echo [!] Файл req.txt не найден.
)

REM Деактивация виртуального окружения
deactivate

echo [*] Установка завершена.
endlocal
