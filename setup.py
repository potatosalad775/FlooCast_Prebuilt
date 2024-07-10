import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "includes": ["queue"],
    "packages": [],
    "include_files": [
      ("./FlooCastApp.ico", "assets"),
      ("./FlooCastApp.gif", "assets"),
      ("./FlooCastApp.png", "assets"),
      ("./FlooCastApp.icns", "assets"),
      ("./FlooCastHeader.png", "assets"),
      ("./offS.png", "assets"),
      ("./onS.png", "assets"),
      ("./locales/", "locales"),
    ]
}

executables = [
    Executable(
        "main.py",
        base="gui",
        icon="FlooCastApp.ico",
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
            ("./FlooCastApp.ico", "assets"),
            ("./FlooCastApp.gif", "assets"),
            ("./FlooCastApp.png", "assets"),
            ("./FlooCastApp.icns", "assets"),
            ("./FlooCastHeader.png", "assets"),
            ("./offS.png", "assets"),
            ("./onS.png", "assets"),
            ("./locales/", "locales"),
        ]
    }

    executables = [
        Executable(
            "main.py",
            base="gui",
            icon="FlooCastApp.png",
            target_name="FlooCast",
            shortcut_name="FlooCast",
        )
    ]

bdist_mac_options = {
    "iconfile": "FlooCastApp.icns"
}
bdist_dmg_options = {
    "applications_shortcut": True,
}

setup(
    name="FlooCast",
    version="1.0.9",
    description="FlooGoo FMA120 Configurator",
    executables=executables,
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
)