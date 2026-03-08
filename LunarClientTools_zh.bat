@ECHO OFF
chcp 65001 >nul
setlocal EnableDelayedExpansion
  
PUSHD "%~DP0" & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas
echo 成功以管理员身份运行。

@rem LunarClientTools v1.9 by GrushTom
@rem https://github.com/GrushTom/LunarClientTools
@rem 请在 Github 上报告任何问题

@rem MIT License
@rem Copyright (c) 2024 GrushTom ✨

@rem Permission is hereby granted, free of charge, to any person obtaining a copy
@rem of this software and associated documentation files (the "Software"), to deal
@rem in the Software without restriction, including without limitation the rights
@rem to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
@rem copies of the Software, and to permit persons to whom the Software is
@rem furnished to do so, subject to the following conditions:

@rem The above copyright notice and this permission notice shall be included in all
@rem copies or substantial portions of the Software.

@rem THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
@rem IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
@rem FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
@rem AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
@rem LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
@rem OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
@rem SOFTWARE.

@ECHO OFF
TITLE LunarClientTools v1.9

echo [90m###################################################################[0m
echo [90m##[0m                  [96mLunar Client 工具脚本[0m                    [90m##[0m
echo [90m##[0m          [36mhttps://github.com/GrushTom/LunarClientTools[0m          [90m##[0m
echo [90m###################################################################[0m
echo.
echo [92m您想要做什么？[0m
echo.
echo [91m1.[0m [97m清除缓存文件[0m
echo [91m2.[0m [97m导航到 .lunarclient 文件夹[0m
echo [91m3.[0m [97m配置文件管理选项[0m
echo [91m4.[0m [97m切换 LunarClient 的 GPU 为独立/集成显卡[0m
echo [91m5.[0m [97m退出[0m
echo.
set /P M=[96m请输入[0m [91m1-5[0m [96m然后按回车键[0m[91m:[0m
if %M%==1 goto :cache-rem
if %M%==2 goto :lc-folder
if %M%==3 goto :json-menu
if %M%==4 goto :igpu-dgpu
if %M%==5 goto :kill

@ECHO ON
@rem Just to clear the console window and go back to the menu
:cls-menu
cls
goto :menu
@rem Menu for profile management options
:json-menu
cls
echo [90m###################################################################[0m
echo [90m##[0m                  [96mLunar Client 工具脚本[0m                    [90m##[0m
echo [90m##[0m          [36mhttps://github.com/GrushTom/LunarClientTools[0m          [90m##[0m
echo [90m###################################################################[0m
echo.
echo [92m配置文件管理选项[0m
echo.
echo [91m1.[0m [97m从存档导入配置文件[0m
echo [91m2.[0m [97m列出目录中所有现有的配置文件[0m
echo [91m3.[0m [97m自动检测配置文件并替换当前配置文件管理器[0m
echo [91m4.[0m [97m手动配置文件管理器生成器[0m
echo [91m5.[0m [97m导出当前配置文件到桌面[0m
echo [91m6.[0m [97m取消[0m
echo.
set /P M=[96m请输入[0m [91m1-6[0m [96m然后按回车键[0m[91m:[0m
if %M%==1 goto :json-archive
if %M%==2 goto :json-list
if %M%==3 goto :json-auto
if %M%==4 goto :json-manual
if %M%==5 goto :json-backup
if %M%==6 goto :cls-menu
echo.
echo.
echo.
pause >nul
cls
goto :menu
@rem Code to get data.json from LunarClientProfiles repository
:json-archive
@rem Sync with the archive to display present profile
@Echo off
del "%userprofile%"\.lunarclient\.lct-cache\* /Q 2>nul
rmdir /s /q "%userprofile%"\.lunarclient\.lct-cache\ 2>nul
mkdir "%userprofile%"\.lunarclient\".lct-cache"
powershell -Command "$url = 'https://raw.githubusercontent.com/Vaption/LunarClientProfiles/main/profiles/data.json'; $filename = [System.IO.Path]::GetFileName($url); wget -Uri $url -OutFile ('%userprofile%\.lunarclient\.lct-cache\' + $filename)"
Powershell -Nop -C "$profiles = (Get-Content '%userprofile%\.lunarclient\.lct-cache\data.json' | ConvertFrom-Json).profiles; foreach ($profile in $profiles) { $profile.link | Out-File -FilePath ('%userprofile%\.lunarclient\.lct-cache\{0}.txt' -f $profile.name) }"
cls
echo [90m###################################################################[0m
echo [90m##[0m                  [96mLunar Client 工具脚本[0m                    [90m##[0m
echo [90m##[0m          [36mhttps://github.com/GrushTom/LunarClientTools[0m          [90m##[0m
echo [90m###################################################################[0m
echo.
echo [92m正在扫描当前可用的配置文件...[0m
timeout /t 3 /nobreak >nul
set "settingsFolder=%userprofile%\.lunarclient\settings\game"
set /a totalProfiles=0
for /d %%i in ("%settingsFolder%\*") do (
    set /a totalProfiles+=1
)
if %totalProfiles% gtr 7 (
    echo [31m错误：存在超过七个配置文件！[0m
    echo [31m允许的最大配置文件数量为八个，无法导入配置文件。[0m
    echo [31m请导航到 .lunarclient\settings\game 并在运行命令前删除一些配置文件。[0m
    pause >nul
    exit /b
) else (
    goto :json-archive-loader
)
@rem Display available profiles on the archive
:json-archive-loader
@echo off
setlocal EnableDelayedExpansion
set "folderPath=%userprofile%\.lunarclient\.lct-cache"
set /a count=0
for %%F in ("%folderPath%\*.txt") do (
    set "filename=%%~nF"
    if not "!filename!"=="linkDisplay" (
        set /a count+=1
        set "file[!count!]=%%~nF"
    )
)
echo [97m存档中可用的配置文件：[0m
for /l %%N in (1,1,!count!) do (
    echo %%N. !file[%%N]!
)
set /p choice=[96m请输入您要导入的配置文件编号[0m[91m:[0m
if defined file[%choice%] (
    set "fileName=!file[%choice%]!.txt"
    set "filePath=%folderPath%\!fileName!"
    if exist "!filePath!" (
        set "tempFile=%folderPath%\linkDisplay.txt"
        if exist "!tempFile!" del "!tempFile!"
        type "!filePath!" > "!tempFile!"
        set "fileContent="
        for /f "usebackq delims=" %%G in ("!tempFile!") do (
            set "fileContent=%%G"
            goto :json-archive-link-display
        )
        :json-archive-link-display
        for /f "delims=" %%G in ("!fileContent!") do (
            set "downloadLink=%%G"
            goto :json-archive-downloader
        )
    ) else (
        echo [91m所选配置文件不存在。正在退出...[0m
        timeout 3 >nul
        goto :menu
    )
)
@rem Download profiles from the archive and extract it, using powershell
:json-archive-downloader
echo [96m尝试从存档下载配置文件...[0m
timeout 2 >nul
powershell -Command "$url = '!downloadLink!'; $filename = [System.IO.Path]::GetFileName($url); wget -Uri $url -OutFile ('%userprofile%\.lunarclient\settings\game\' + $filename); Expand-Archive -Path ('%userprofile%\.lunarclient\settings\game\' + $filename) -DestinationPath ('%userprofile%\.lunarclient\settings\game\' + [System.IO.Path]::GetFileNameWithoutExtension($filename)) -Force"
echo [32m配置文件导入成功，尝试生成新的 profile_manager.json...[0m
timeout 2 >nul
goto :json-auto
pause >nul
cls
goto :menu
@rem Scan settings folder for user profiles to display a list
:json-list
echo.
@echo off
setlocal
echo [32m正在扫描您的配置文件目录...[0m
timeout /t 4 /nobreak >nul
set "path=%userprofile%\.lunarclient\settings\game"
set count=0

for /d %%G in ("%path%\*") do (
    set /a count+=1
)
echo [92m您总共有 %count%/8 个配置文件：[0m
echo.

for /d %%G in ("%path%\*") do (
    echo - %%~nG
)
echo.
echo.
echo.
endlocal
pause >nul
cls
goto :menu
@rem Scan for available profiles on the user's computer
:json-auto
@echo off
setlocal enabledelayedexpansion
set "settingsFolder=%userprofile%\.lunarclient\settings\game"

if not exist "%settingsFolder%" (
    echo [91m.lunarclient 中不存在设置文件夹[0m
    echo [91mLCT 无法在您的设置目录中检测到任何配置文件。[0m
    pause >nul
    exit /b
)
echo [92m正在扫描设置文件夹...[0m
timeout /t 3 /nobreak >nul
set /a totalProfiles=0
for /d %%i in ("%settingsFolder%\*") do (
    set /a totalProfiles+=1
)
@rem Show an error if the user has more than eight profiles, as that's the limit
if %totalProfiles% gtr 8 (
    echo [31m错误：存在超过八个配置文件！[0m
    echo [31m请导航到 .lunarclient\settings\game 并在运行命令前删除一些配置文件。[0m
    del "%userprofile%"\.lunarclient\.lct-cache\* /Q 2>nul
    rmdir /s /q "%userprofile%"\.lunarclient\.lct-cache\ 2>nul
    pause >nul
    exit /b
) else (
    goto :json-auto-action
)
@rem Automatically generate and replace profile_manager.json based on the profile folder available
:json-auto-action
echo [92m在设置文件夹中找到 %totalProfiles% 个配置文件。[0m
echo [92m正在终止启动器进程...[0m
taskkill /im "Lunar Client.exe" /f 2>nul
timeout /t 2 /nobreak >nul
echo [32m任务完成。[0m
echo [32m正在生成配置文件...[0m
timeout /t 3 /nobreak >nul
set "jsonContent=["

for /d %%i in ("%settingsFolder%\*") do (
    set "folderName=%%~nxi"
    
    set "profileJson={"name":"!folderName!","displayName":"!folderName!","default":false,"active":false,"iconName":"","server":""}"
    
    set "jsonContent=!jsonContent!!profileJson!"
    set /a totalProfiles-=1
    if !totalProfiles! gtr 0 (
        set "jsonContent=!jsonContent!,"
    )
)
set "jsonContent=!jsonContent!]"
    
> "%userprofile%\.lunarclient\settings\game\profile_manager.json" echo !jsonContent!
echo.
echo [32m成功生成并替换 profile_manager.json[0m
echo [32m操作成功。[0m
del "%userprofile%"\.lunarclient\.lct-cache\* /Q 2>nul
rmdir /s /q "%userprofile%"\.lunarclient\.lct-cache\ 2>nul
pause >nul
cls
goto :menu
@rem Generate profile_manager.json based on values given by the user
:json-manual
@echo off
setlocal enabledelayedexpansion

echo [36m请输入要添加的配置文件总数（最大=8）：[0m
set /p totalProfiles=

if %totalProfiles% gtr 8 (
    echo [31m错误：超过最大配置文件数量。请输入 1 到 8 之间的数字。[0m
    pause >nul
    cls
    goto :menu
)

echo [32m正在生成配置文件...[0m
echo.

set "jsonContent=["

for /l %%i in (1, 1, %totalProfiles%) do (
    echo [96m配置文件 %%i[0m
    echo [93m请输入配置文件 %%i 的名称：[0m
    set /p profileName=
    echo [93m请输入配置文件 %%i 的显示名称：[0m
    set /p displayName=
    
    if %%i==1 (
        set "profileJson={"name":"!profileName!","displayName":"!displayName!","default":true,"active":true,"iconName":"","server":""}"
    ) else (
        set "profileJson=,{"name":"!profileName!","displayName":"!displayName!","default":false,"active":false,"iconName":"","server":""}"
    )
    
    set "jsonContent=!jsonContent!!profileJson!"
)
@rem Save the generated profile_manager.json to the user's desktop
set "jsonContent=!jsonContent!]"
    
> "%userprofile%\Desktop\profile_manager.json" echo !jsonContent!
echo.
echo [32m成功在您的桌面上生成 profile_manager.json。[0m
echo.
echo.
pause >nul
cls
goto :menu
@rem Save a copy of the user's profiles, profile_manager.json, saved_skins.json, and waypoints.json on their desktop
:json-backup
echo.
echo.
echo.
choice /N /C YC /M "确定要继续吗？按 Y 继续，按 C 取消"%1
IF ERRORLEVEL==2 goto :menu
IF ERRORLEVEL==1 goto :json-backup-action
:json-backup-action
mkdir "%userprofile%"\Desktop\"LCT-Profiles"
xcopy /s /v "%userprofile%"\.lunarclient\settings\game "%userprofile%"\Desktop\LCT-Profiles /Q > nul
del "%userprofile%"\Desktop\LCT-Profiles\accounts.json
del "%userprofile%"\Desktop\LCT-Profiles\alert_manager.json
del "%userprofile%"\Desktop\LCT-Profiles\features.json
del "%userprofile%"\Desktop\LCT-Profiles\global_options.json
del "%userprofile%"\Desktop\LCT-Profiles\internal.json
del "%userprofile%"\Desktop\LCT-Profiles\knownServers.json
del "%userprofile%"\Desktop\LCT-Profiles\language.json
del "%userprofile%"\Desktop\LCT-Profiles\main_menu_theme_manager.json
del "%userprofile%"\Desktop\LCT-Profiles\metadata_fallback.json
del "%userprofile%"\Desktop\LCT-Profiles\muted_users.json
del "%userprofile%"\Desktop\LCT-Profiles\rule-features.json
del "%userprofile%"\Desktop\LCT-Profiles\statistics.json
del "%userprofile%"\Desktop\LCT-Profiles\version
echo [32m成功将您的配置文件复制到桌面。[0m
echo [92m文件路径："%userprofile%"\Desktop\LCT-Profiles[0m
%SystemRoot%\explorer.exe "%userprofile%\Desktop\LCT-Profiles\"
echo.
echo.
echo.
pause >nul
cls
goto :menu
@rem Delete LunarClient's cache (will be recreated next launch)
:cache-rem
echo.
echo.
echo.
choice /N /C YC /M "确定要继续吗？按 Y 继续，按 C 取消"%1
IF ERRORLEVEL==2 goto :menu
IF ERRORLEVEL==1 goto :cache-rem-action
:cache-rem-action
del "%userprofile%"\.lunarclient\offline\multiver\cache\* /Q > nul
echo [32m成功删除 LunarClient 游戏缓存。[0m
echo.
echo.
echo.
pause >nul
cls
goto :menu
@rem Simply opens the .lunarclient folder
:lc-folder
echo.
echo.
echo.
%SystemRoot%\explorer.exe "%userprofile%\.lunarclient\"
echo [32m成功在新窗口中打开 .lunarclient。[0m
echo.
echo.
echo.
pause >nul
cls
goto :menu
@rem Change if Lunar should use your integrated, or dedicated graphics
:igpu-dgpu
echo.
echo.
echo.
choice /N /C DI /M "您想切换到哪种图形处理器？按 D 选择独立显卡，按 I 选择集成显卡"%1
IF ERRORLEVEL==2 goto :igpu-dgpu-dedicated
IF ERRORLEVEL==1 goto :igpu-dgpu-integrated
@rem Confirm
:igpu-dgpu-integrated
choice /N /C YC /M "确定要继续吗？按 Y 继续，按 C 取消"%1
IF ERRORLEVEL==2 goto :menu
IF ERRORLEVEL==1 goto :igpu-dgpu-action-integrated
:igpu-dgpu-action-integrated
@echo off
set "root_directory=%userprofile%\.lunarclient\jre\"
set "javaw_path="
@rem Find the javaw.exe file
:findjavaw
for /d %%i in ("%root_directory%\*") do (
    if exist "%%i\bin\javaw.exe" (
        set "javaw_path=%%i\bin\"
        goto :validatejavaw
    )
    set "root_directory=%%i"
    goto :findjavaw
)
@rem Change the registry value for javaw.exe to switch the GPU used by LunarClient to Power Saving graphics
:validatejavaw
if defined javaw_path (
    reg Add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v "%javaw_path%javaw.exe" /d "GpuPreference=1;" /f
    color 0A
    echo 成功将 LunarClient 的 GPU 切换到节能模式。
) else (
    color 0C
    echo LCT 无法找到 javaw.exe，请重新启动游戏以下载该文件。
)
echo.
echo.
pause >nul
cls
goto :menu
@rem Confirm (again)
:igpu-dgpu-dedicated
choice /N /C YC /M "确定要继续吗？按 Y 继续，按 C 取消"%1
IF ERRORLEVEL==2 goto :menu
IF ERRORLEVEL==1 goto :igpu-dgpu-action-dedicated
:igpu-dgpu-action-dedicated
@echo off
set "root_directory=C:\Users\%username%\.lunarclient\jre\"
set "javaw_path="
@rem Find the javaw.exe file (again)
:findjavaw
for /d %%i in ("%root_directory%\*") do (
    if exist "%%i\bin\javaw.exe" (
        set "javaw_path=%%i\bin\"
        goto :validatejavaw
    )
    set "root_directory=%%i"
    goto :findjavaw
)
@rem Change the registry value for javaw.exe to switch the GPU used by LunarClient to High Performance graphics
:validatejavaw
if defined javaw_path (
    reg Add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v "%javaw_path%javaw.exe" /d "GpuPreference=2;" /f
    color 0A
    echo 成功将 LunarClient 的 GPU 切换到高性能模式。
) else (
    color 0C
    echo LCT 无法找到 javaw.exe，请重新启动游戏以下载该文件。
)
echo.
echo.
pause >nul
cls
goto :menu
@rem Exit
:kill
exit

@rem Unsupported windows version error
:windows-error
echo [90m#############################[0m [31m错误[0m [90m###############################[0m
echo [90m#[0m                                                                 [90m#[0m
echo [90m#[0m          [91m此脚本仅适用于 Windows 10 及以上版本。[0m           [90m#[0m
echo [90m#[0m         [91m您当前的 Windows 版本不受支持[0m           [90m#[0m
echo [90m#[0m     [91m如果您认为这是一个问题，请在 Github 上打开一个 issue[0m    [90m#[0m
echo [90m###################################################################[0m
echo.
echo.
PAUSE >nul