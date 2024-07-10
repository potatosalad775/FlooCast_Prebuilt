from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "includes": ["queue", "Xlib.ext.xfixes", "Xlib.ext.xinput", "Xlib.ext.damage", "Xlib.ext.res"],
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

setup(
    name="FlooCast",
    version="1.0.9",
    description="FlooGoo FMA120 Configurator",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="gui")],
)