import pygame
from modelo.Personaje import Personaje

class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y):
            Personaje.__init__(self,imagen,x,y)

        def desplazarIzquierda(self):
            self.x=0
            self.y=350 #ac? esta el perro

#            for x in range(100):
#               pantalla.blit(self.imagen,[self.x, self.y])
#               self.x=self.x+2
#               self.y=self.y+2
#               pygame.display.update()                            # y los mostramos
#               pygame.time.delay(-1)

#            self.x=1000
#            self.y=350

