import pygame
from modelo.Personaje import Personaje

class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen):
            Personaje.__init__(self,imagen)

        def desplazarIzquierda(self):
         print 'en contruccion'