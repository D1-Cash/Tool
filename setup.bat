@echo off

REM Install Python packages listed in requirements.txt
pip install -r requirements.txt

REM Check if installation was successful
if %errorlevel% neq 0 (
    echo Installation failed. Check the error messages above.
) else (
    echo Installation successful.
)

REM Pause to view the output
pause
