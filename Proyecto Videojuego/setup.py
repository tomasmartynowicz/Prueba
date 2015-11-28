import cx_Freeze

executables=[cx_Freeze.Executable("inicio.py")]

cx_Freeze.setup(
    name="Jump the Rock",
  #options={"build_exe":{"packages":["pygame"],"include_files":["image\colectivo.jpg","image/f_Martillo.jpg","image/F_TheWall.jpg","image/fondo.jpg","image/fondo2.jpg","image\intruc.jpg","image\marte.jpg","image/f_puntaje.png","image/f_TheWall.png","image/fondo2.png","image/fondo6.png","image/fondoIntro.png","image/fondoIntro2.png","image\gameover.png","image/noche.png","image\Perro4.png","image\pinkfloyd.png","image\pinkfloyd2.png","image\piso.png","image\piso2.png","image\rock.png","image\rock2.png","image\rock3.png","image\rock4.png","image\rock5.png","image\rockIntro.png","image\unla.png","sound\dog.mp3","sound\Yet Another Movie.mp3","sound\bomb.wav","font\LeagueGothic-Italic.otf","font\LeagueGothic-Regular.otf","font/Fontin-Bold.ttf","font/Fontin-Italic.ttf","font/Fontin-Regular.ttf","font/Fontin-SmallCaps.ttf","font\HEADOH__.ttf","font\HEADTH__.ttf","font\Snickles.ttf","modelo\Enemigo.py","modelo\Juego.py","modelo\Jugador.py","modelo\Menu.py","modelo\Pantalla.py","modelo\Personaje.py","modelo\Puntaje.py","modelo\Sonido.py"]}},
    options={"build_exe":{"packages":["pygame"],"include_files":["image","sound","font"]}},
    description="Jump The Rock - videojuego",
    executables=executables

    )
