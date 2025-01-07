@echo off
:menu
echo ===============================
echo     Gerenciar AutoConfig Wi-Fi
echo ===============================
echo 1. Desabilitar AutoConfig
echo 2. Habilitar AutoConfig
echo 3. Sair
echo ===============================
set /p choice="Escolha uma opção (1/2/3): "

if "%choice%"=="1" (
    netsh wlan set autoconfig enabled=no interface="Wi-Fi"
    echo AutoConfig desabilitado!
    pause
    goto menu
) else if "%choice%"=="2" (
    netsh wlan set autoconfig enabled=yes interface="Wi-Fi"
    echo AutoConfig habilitado!
    pause
    goto menu
) else if "%choice%"=="3" (
    exit
) else (
    echo Opção inválida. Tente novamente.
    pause
    goto menu
)
