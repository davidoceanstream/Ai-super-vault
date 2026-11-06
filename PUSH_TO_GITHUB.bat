@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Push Universal AI Vault to GitHub

echo =====================================================================
echo    🏛️ UNIVERSAL AI VAULT - 1-CLICK GITHUB UPLOADER
echo =====================================================================
echo.

where git >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] ไม่พบคำสั่ง git บนเครื่องนี้!
    echo กรุณาติดตั้ง Git for Windows หรือเปิดผ่าน GitHub Desktop
    echo.
    pause
    exit /b 1
)

:: Ensure on main branch
git branch -M main

:: Check if remote origin is already set
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [!] ยังไม่ได้เชื่อมต่อ GitHub Repository URL
    echo ตัวอย่าง URL: https://github.com/davidoceanstream/universal-ai-vault.git
    echo.
    set /p REPO_URL="กรุณาวาง URL ของ GitHub Repo ที่คุณเพิ่งสร้างบนเว็บ แล้วกด Enter: "
    if not "%REPO_URL%"=="" (
        git remote add origin %REPO_URL%
    ) else (
        echo [ERROR] คุณไม่ได้ใส่ URL ยกเลิกขั้นตอน
        pause
        exit /b 1
    )
)

echo.
echo [1/3] ตรวจสอบไฟล์และสเตจไฟล์ทั้งหมด...
git add .

echo.
echo [2/3] บันทึกสถานะล่าสุด...
git commit -m "feat: sync universal ai tool vault catalog (142 tools)" >nul 2>&1

echo.
echo [3/3] กำลังอัปโหลด (Push) ขึ้น GitHub...
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo =====================================================================
    echo  [✨ SUCCESS] อัปโหลด Universal AI Vault ขึ้น GitHub เรียบร้อยแล้ว!
    echo =====================================================================
) else (
    echo.
    echo [!] หากติดปัญหาเรื่องสิทธิ์หรือ Permission:
    echo     1. ตรวจสอบว่าสร้าง New Repository บน GitHub ไว้แล้วหรือยัง
    echo     2. ตรวจสอบว่าได้ Login บัญชี GitHub ไว้ใน Windows Credential หรือยัง
    echo     3. หรือเปิด GitHub Desktop แล้วเลือก Add Existing Repository โฟลเดอร์นี้เพื่อ Publish 1-Click
)

echo.
pause
