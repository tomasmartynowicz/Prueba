from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
import pygame

class Pantalla(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,nombre,display,imagen,pos_x,pos_y):                                   #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.nombre=nombre
        self.display=display
        self.imagen=imagen
        self.pos_x=pos_x
        self.pos_y=pos_y


    def moverPantalla(self):
         self.pos_x=self.pos_x-2
         self.pos_y=0


    def cargarPantalla(self,jugador,enemigo,puntaje):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(puntaje), True, (255, 255, 255))
        self.display.blit(self.imagen,[self.pos_x, self.pos_y])
        self.display.blit(jugador.imagen,[jugador.x,jugador.y])
        self.display.blit(enemigo.imagen,[enemigo.x,enemigo.y])
        self.display.blit(texto,[800, 0])
        #self.moverPantalla()
        #pygame.time.delay(-1)
        #pygame.display.update()


