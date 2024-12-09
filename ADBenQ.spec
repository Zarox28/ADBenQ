# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import get_package_paths

if sys.platform == "win32":
    icon_file = "src/icons/windows.ico"
elif sys.platform == "darwin":
    icon_file = "src/icons/macos.icns"
else:  # Assuming Linux or other Unix-like OS
    icon_file = "src/icons/linux.png"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
      ('components/*', 'components'),
      ('ui/*', 'ui'),
      ('src/*', 'src'),
      ('device.py', '.'),
      ('connection.py', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ADBenQ - v0.1.6-alpha',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ADBenQ',
)