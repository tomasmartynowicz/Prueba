import cx_Freeze

executables=[cx_Freeze.Executable("inicio.py")]

cx_Freeze.setup(
    name="Jump the Rock",
    options={"build_exe":{"packages":["pygame"],"include_files":["colectivo.jpg","f_Martillo.jpg","F_TheWall.jpg","fondo.jpg","fondo2.jpg","intruc.jpg","marte.jpg","f_puntaje.png","f_TheWall.png","fondo2.png","fondo6.png","fondoIntro.png","fondoIntro2.png","gameover.png","noche.png","Perro4.png","pinkfloyd.png","pinkfloyd2.png","piso.png","piso2.png","rock.png","rock2.png","rock3.png","rock4.png","rock5.png","rockIntro.png","unla.png","dog.mp3","Yet Another Movie.mp3","bomb.mp3","LeagueGothic-Italic.otf","LeagueGothic-Regular.otf","Fontin-Bold.ttf","Fontin-Italic.ttf","Fontin-Regular.ttf","Fontin-SmallCaps.ttf","HEADOH__.ttf","HEADTH__.ttf"]}},
    description="Jump The Rock - videojuego",
    executables=executables

    )