import pygame

class Personaje():                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,imagen,x,y):                                          #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.imagen = pygame.image.load(imagen)           #El parametro self no se que significa pero tiene que ir.
        self.x=x
        self.y=y
