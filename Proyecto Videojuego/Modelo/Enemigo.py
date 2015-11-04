import pygame
from modelo.Personaje import Personaje

class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y):
            Personaje.__init__(self,imagen,x,y)

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

    #toPantalla()
        def toPantalla(self,display):  #tipo el toString()
            return display.blit(self.imagen,[self.x, self.y]) #imprime en pantalla


        def desplazarIzquierda(self):
            if self.x<-16:
                self.x=1000
                self.y=320
            else:
               self.x=self.x-10
               self.y=320


