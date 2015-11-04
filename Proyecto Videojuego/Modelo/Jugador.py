import pygame
from modelo.Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y,alias):
            Personaje.__init__(self,imagen,x,y)              #A mi me funciona sin tener que ponerla pero asi compila seguro.
            self.alias=alias
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

    #Getters and Setters
        def setImagen(self, imagen):
            self.imagen=imagen
        def getImagen(self):
            return imagen

        def setX(self, x):
            self.x=x
        def getX(self):
            return x

        def setY(self, y):
            self.y=y
        def getY(self):
            return y

        def setAlias(self, alias):
            self.alias=alias
        def getAlias(self):
            return alias
    #toPantalla()
        def toPantalla(self,display):
            display.blit(self.imagen,[self.x, self.y]) #imprime en pantalla

    #metodos
        def saltar(self):
            self.x=0
            self.y=150

        def caer(self):
            self.x=0
            self.y=320

        def animar(self):
            print 'en contruccion'
