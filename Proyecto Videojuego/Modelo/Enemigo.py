import pygame
from modelo.Personaje import Personaje

class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y):
            Personaje.__init__(self,imagen,x,y)

        def desplazarIzquierda(self):
            if self.x<-16:
                self.inicializarPosicion()
            else:
               self.x=self.x-10
               self.y=350

        def inicializarPosicion(self):
                self.x=1000
                self.y=350

