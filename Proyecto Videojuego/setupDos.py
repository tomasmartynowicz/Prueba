import cx_Freeze

executables=[cx_Freeze.Executable("Jump The Rock.py")]

cx_Freeze.setup(
    name="Jump the Rock",
     options={"build_exe":{"packages":["pygame"],"include_files":["image","sound","font"]}},
    description="Jump The Rock - videojuego",
    executables=executables

    )
