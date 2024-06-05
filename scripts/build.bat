@echo off
if "%UPX_PATH%" == "" (
    echo Please set UPX_PATH to the path of upx.exe directory
    goto :EOF
)

python -m nuitka --standalone --mingw64 ^
    --plugin-enable=pyside6,upx ^
    --output-dir=dist ^
    --upx-binary=%UPX_PATH% ^
    --windows-icon-from-ico=yolo_ui\resources\icon.ico ^
    --python-flag=no_docstrings,no_asserts ^
    --assume-yes-for-downloads ^
    --disable-console ^
    main.py

@REM python tools/polyfill.py

:EOF
