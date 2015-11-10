import pygame
from modelo.Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y,alias):
            Personaje.__init__(self,imagen,x,y)              #A mi me funciona sin tener que ponerla pero asi compila seguro.
            self.alias=alias
            self.t = 1
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

    #Getters and Setters
        def setImagen(self, imagen):
            self.imagen=pygame.image.load(imagen)
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
            if self.t > 10:
                self.t=1
            self.y = 320 - 50*(self.t) + 5 * (self.t)*(self.t)
            self.y = int(self.y)
            self.t = self.t + 1

        def animar(self):
            print 'en contruccion'
