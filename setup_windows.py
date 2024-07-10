from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "includes": ["queue"],
    "packages": [],
    "include_files": [
      "assets",
      "locales"
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

setup(
    name="FlooCast",
    version="1.0.9",
    description="FlooGoo FMA120 Configurator",
    executables=executables,
    options={"build_exe": build_exe_options},
)