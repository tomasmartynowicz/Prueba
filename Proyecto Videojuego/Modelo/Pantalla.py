from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
import pygame

class Pantalla(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,nombre,display,imagen,x,y):                                   #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.nombre=nombre
        self.display=display
        self.imagen=imagen
        self.x=x
        self.y=y

    #Getters and Setters
        def setNombre(self, nombre):
            self.nombre=nombre
        def getNombre(self):
            return nombre

        def setDisplay(self, display):
            self.display=display
        def getDisplay(self):
            return display

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

    #metodos

    def moverPantalla(self):
        if self.x<-400:
            self.x=1080
            self.y=420
        else:
            self.x=self.x-2
            self.y=0

    def cargarPantalla(self,jugador,enemigo,puntaje):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(puntaje), True, (255, 255, 255))

        self.display.blit(self.imagen,[self.x, self.y]) #imprime pantalla
        jugador.toPantalla(self.display)
        enemigo.toPantalla(self.display)
        #self.display.blit(enemigo.imagen,[enemigo.x,enemigo.y])#imprime enemigo
        #self.display.blit(texto,[800, 0])#imprime puntaje





