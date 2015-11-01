class Pantalla(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,nombre,display,imagen,pos_x,pos_y):                                   #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.nombre=nombre
        self.display=display
        self.imagen=imagen
        self.pos_x=pos_x
        self.pos_y=pos_y
