#Esta la estructura de basica de una clase en python.
class Personaje(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,imagen,x,y):                                          #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.imagen = imagen           #El parametro self no se que significa pero tiene que ir.
        self.x=x
        self.y=y
