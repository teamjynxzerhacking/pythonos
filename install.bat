@echo off
:menu
cls
echo                      __             ___    ___      
echo  __                 /\ \__         /\_ \  /\_ \     
echo /\_\    ___     ____\ \ ,_\    __  \//\ \ \//\ \    
echo \/\ \ /' _ `\  /',__\\ \ \/  /'__`\  \ \ \  \ \ \   
echo  \ \ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_ \_\ \_ \_\ \_ 
echo   \ \_\ \_\ \_\/\____/ \ \__\ \__/.\_\/\____\/\____\
echo    \/_/\/_/\/_/\/___/   \/__/\/__/\/_/\/____/\/____/
echo.
echo ====================================================
echo 1 - Install pygame
echo 2 - Cancel / Exit
echo 3 - Open pythonos (not working)
echo ====================================================
set /p input=Enter your choice: 

if "%input%"=="1" goto install
if "%input%"=="2" goto cancel
if "%input%"=="3" goto pythonos
goto menu

:install
echo Installing pygame...
pip install pygame
msg * Installation successful
echo Press any key to return to menu.
pause >nul
goto menu

:cancel
echo Exiting...
exit

:pythonos
if exist pythonos.py (
    start python pythonos.py
) else (
    echo File "pythonos.py" not found!
    pause
)
goto menu
