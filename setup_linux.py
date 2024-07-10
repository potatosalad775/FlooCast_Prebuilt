from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "includes": ["queue", "Xlib.ext.xfixes", "Xlib.ext.xinput", "Xlib.ext.damage", "Xlib.ext.res", "System",
      "System.IO.Ports", "_scproxy", "_wmi", "defusedxml", "gi", "gi.repository", "msvcrt", "nturl2path", "numpy",
      "numpy.typing", "packaging.version", "re.IGNORECASE", "typing_extensions"
    ],
    "packages": [],
    "include_files": [
      "FlooCastApp.gif",
      "FlooCastApp.ico",
      "FlooCastHeader.png",
      "offS.png",
      "onS.png",
      "locales"
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

setup(
    name="FlooCast",
    version="1.0.9",
    description="FlooGoo FMA120 Configurator",
    executables=executables,
    options={"build_exe": build_exe_options},
)