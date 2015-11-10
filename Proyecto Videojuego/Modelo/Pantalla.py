from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
import pygame

class Pantalla(object):
    def __init__(self,nombre,display,imagen,x,y,resolucion):
        self.nombre=pygame.display.set_caption(nombre)
        self.display=display
        self.resolucion=resolucion
        self.imagen=imagen                                                      #imagen guarda la direccion del fondo
        self.fondo1=pygame.image.load(imagen)                                   #Cargo la imagen a 2 fondos diferentes
        self.fondo2=pygame.image.load(imagen)
        self.x=[x,x+resolucion]
        self.y=y

    #Setters
    def setNombre(self, nombre):
            self.nombre=pygame.display.set_caption(nombre)

    def setDisplay(self,x,y):
            self.display=pygame.display.set_mode((x,y))

    def setImagen(self):
            self.fondo1=pygame.image.load(self.imagen)
            self.fondo2=pygame.image.load(self.imagen)

    def setX(self, x):
            self.x=x

    def setY(self, y):
            self.y=y
    #toPantalla()
    def toPantalla(self):  #tipo el toString()
         self.display.blit(self.fondo1,[self.x[0], self.y]) #imprime en pantalla los 2 fondos
         self.display.blit(self.fondo2,[self.x[1],self.y])


    #metodos

    def moverPantalla(self,pos):          #cambia la posicion de 1 fondo, por lo que se pasa como
        if self.x[pos]<=-self.resolucion:      #parametro la posicion en X[]
            self.x[pos]=self.resolucion
            self.y=420
        else:
            self.x[pos]=self.x[pos]-2 #es 2
            self.y=0


    def detenerPantalla(self):
            self.x[0]=0
            self.y=420

    def cargarPantalla(self,jugador,enemigo,puntaje,pantalla):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(puntaje), True, (255, 255, 255))
        pantalla.toPantalla()
        jugador.toPantalla(self.display)
        enemigo.toPantalla(self.display)
        self.display.blit(texto,[0, 0])#imprime puntaje





