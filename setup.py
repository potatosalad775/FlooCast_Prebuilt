import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "includes": ["queue"],
    "packages": [],
    "include_files": [
        ("./assets/", "assets"),
        ("./locales/", "locales"),
    ]
}

executables = [
    Executable(
        "main.py",
        base="gui",
        icon="assets/FlooCastApp.ico",
        target_name="FlooCast",
        shortcut_name="FlooCast",
    )
]

if sys.platform == "linux":
    build_exe_options = {
        "excludes": [],
        "includes": ["queue", "Xlib.ext.xfixes", "Xlib.ext.xinput", "Xlib.ext.damage", "Xlib.ext.res"],
        "packages": [],
        "include_files": [
            ("./assets/", "assets"),
            ("./locales/", "locales"),
        ]
    }

    executables = [
        Executable(
            "main.py",
            base="gui",
            icon="assets/FlooCastApp.png",
            target_name="FlooCast",
            shortcut_name="FlooCast",
        )
    ]

bdist_mac_options = {
    "bundle_name": "FlooCast",
    "iconfile": "assets/FlooCastApp.icns"
}
bdist_dmg_options = {
    "applications_shortcut": True,
}

setup(
    name="FlooCast",
    version="1.1.2",
    description="FlooGoo FMA120 Configurator",
    executables=executables,
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
)