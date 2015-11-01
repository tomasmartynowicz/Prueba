import pygame
from modelo.Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y,alias):
            Personaje.__init__(self,imagen,x,y)              #A mi me funciona sin tener que ponerla pero asi compila seguro.
            self.alias=alias
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

        def saltar(self):
            self.x=100
            self.y=600

        def animar(self):
            print 'en contruccion'
