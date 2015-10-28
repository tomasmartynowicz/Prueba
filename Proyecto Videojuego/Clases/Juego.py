import Personaje #no estoy seguro si se importa o python sabe que esta dentro del modelo

class Juego(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self):                                          #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.jugador=Personaje          #El parametro self no se que significa pero tiene que ir.
        self.enemigo=Personaje
        self.sonido=Sonido
    def crearPersonaje(self):
        print 'en contruccion'
    def reproducirSonido(self):
        print 'en contruccion'
