# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
import sys

block_cipher = None

# Collect all submodules for the required packages
hidden_imports = []
hidden_imports += collect_submodules('tkinter')
hidden_imports += collect_submodules('pyserial')
hidden_imports += collect_submodules('pystray')
hidden_imports += collect_submodules('serial_tool')
hidden_imports += collect_submodules('notify-py')
hidden_imports += collect_submodules('certifi')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('FlooCastApp.gif', '.'),
        ('FlooCastApp.ico', '.'),
        ('FlooCastHeader.png', '.'),
        ('onS.png', '.'),
        ('offS.png', '.'),
        ('locales', 'locales'),
    ],
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

if sys.platform == 'darwin':
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='FlooCast',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        icon='FlooCastApp.ico',
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='FlooCast'
    )
    app = BUNDLE(
        coll,
        name='FlooCast.app',
        icon='FlooCastApp.ico',
        bundle_identifier=None,
        info_plist={
            'NSHighResolutionCapable': 'True'
        },
    )
else:
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='FlooCast',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon='FlooCastApp.ico',
    )