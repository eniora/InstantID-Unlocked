@echo off
cd /d "%~dp0"
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist "..\venv\Scripts\activate.bat" (
    call ..\venv\Scripts\activate.bat
) else if exist "..\..\venv\Scripts\activate.bat" (
    call ..\..\venv\Scripts\activate.bat
) else (
    echo Could not find venv folder.
    pause
    exit /b 1
)
python _Theme_downloader.py
echo Downloaded Successfully. Restart InstantID completely for the theme to appear in the dropdown.
pause