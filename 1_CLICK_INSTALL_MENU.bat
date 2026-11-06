@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Virtuoso Universal AI Toolkit Installer
python install_kit.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo [!] ตรวจสอบว่าได้ติดตั้ง Python ไว้ในเครื่องแล้วหรือยัง
    pause
)
