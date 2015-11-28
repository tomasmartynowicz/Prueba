import cx_Freeze

import sys


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables=[cx_Freeze.Executable("Jump The Rock.py",icon="Perro.ico",base=base)]



cx_Freeze.setup(
    
	name="Jump the Rock",
     
	options={"build_exe":{"packages":["pygame"],"include_files":["image","sound","font"]}},
    
	description="Jump The Rock - videojuego",
    	
	executables=executables

    
	)
