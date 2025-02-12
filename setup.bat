@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

REM Название виртуального окружения
set VENV_DIR=venv
set REQ_FILE=req.txt

REM Проверка наличия Python
where python >nul 2>nul
if %errorlevel% NEQ 0 (
    echo [!] Python не найден. Установите Python и добавьте его в PATH.
)

REM Устанавливаем кодировку UTF-8
set PYTHONUTF8=1

REM Проверка установки модуля venv
python -c "import venv" 2>nul
if %errorlevel% NEQ 0 (
    echo [*] venv не установлен. Устанавливаем...
    python -m pip install --upgrade pip
    python -m pip install virtualenv
    if %errorlevel% NEQ 0 (
        echo [!] Ошибка при установке venv.
    )
)

REM Проверка наличия виртуального окружения
if not exist "%VENV_DIR%\\Scripts\\activate.bat" (
    echo [*] Виртуальное окружение не найдено. Создаём новое...
    python -m venv %VENV_DIR%
    if %errorlevel% NEQ 0 (
        echo [!] Ошибка при создании виртуального окружения.
    )
) else (
    echo [*] Виртуальное окружение уже существует.
)

REM Активация виртуального окружения
call %VENV_DIR%\\Scripts\\activate.bat

REM Проверка наличия файла req.txt
if not exist %REQ_FILE% (
    echo [!] Файл %REQ_FILE% не найден в текущей директории.
)

echo [*] Проверка установленных библиотек...

REM Проверка и установка зависимостей
pip check >nul 2>&1
if %errorlevel% NEQ 0 (
    echo [!] Ошибка при проверке зависимостей, но продолжаю выполнение...
)
if %errorlevel% NEQ 0 (
    echo [!] Обнаружены проблемы с установленными пакетами. Установка/обновление зависимостей...
    pip install --upgrade pip
    pip install -r %REQ_FILE%
    if %errorlevel% NEQ 0 (
        echo [!] Ошибка при установке зависимостей.
    )
    echo [*] Зависимости успешно установлены.
) else (
    echo [*] Все зависимости установлены корректно.
)

pre-commit install

echo [*] Установка завершена.
endlocal