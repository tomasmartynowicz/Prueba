import pygame
from modelo.Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y,alias):
            Personaje.__init__(self,imagen,x,y)              #A mi me funciona sin tener que ponerla pero asi compila seguro.
            self.alias=alias
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

        def saltar(self):
            self.x=0
            self.y=100

        def caer(self):
            self.x=0
            self.y=320

        def animar(self):
            print 'en contruccion'
