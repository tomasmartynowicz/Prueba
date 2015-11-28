import pygame
from Personaje import Personaje

class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y):
            Personaje.__init__(self,imagen,x,y)

    #Getters and Setters
        def setImagen(self, imagen):
            self.imagen=pygame.image.load(imagen).convert_alpha()

        def setX(self, x):
            self.x=x

        def setY(self, y):
            self.y=y

    #toPantalla()
        def toPantalla(self,display):  #tipo el toString()
            display.blit(self.imagen,[self.x, self.y]) #imprime en pantalla


        def desplazarIzquierda(self):
            if self.x<-86:
                self.x=1000
                self.y=320
            else:
               self.x=self.x-15
               self.y=320

        def desplazarIzquierdaRapido(self):
            if self.x<-16:
                self.x=1000
                self.y=320
            else:
               self.x=self.x-40
               self.y=320


        def desplazarIzquierda2(self, t):
            if t>150:
                self.x=1000
                self.x = int(self.x)
                t=1
            else:
               self.x=1000 -t*8
               t=t+2
            return t

        def desplazarIzquierda3(self, t):
            if t>150:
                self.x=1000
                self.x = int(self.x)
                t=1
            else:
               self.x=1000 -t*8
               t=t+4
            return t



