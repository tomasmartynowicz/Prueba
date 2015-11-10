from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
import pygame

class Pantalla(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self,nombre,display,imagen,x,y):                                   #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.nombre=pygame.display.set_caption(nombre)
        self.display=display
        self.imagen=pygame.image.load(imagen)
        self.x=x
        self.y=y

    #Setters
    def setNombre(self, nombre):
            self.nombre=pygame.display.set_caption(nombre)

    def setDisplay(self,x,y):
            self.display=pygame.display.set_mode((x,y))

    def setImagen(self, imagen):
            self.imagen=pygame.image.load(imagen)

    def setX(self, x):
            self.x=x

    def setY(self, y):
            self.y=y
    #toPantalla()
    def toPantalla(self):  #tipo el toString()
         self.display.blit(self.imagen,[self.x, self.y]) #imprime en pantalla


    #metodos

    def moverPantalla(self):
        if self.x<=-1900:
            self.x=0
            self.y=420
        else:
            self.x=self.x-2 #es 2
            self.y=0


    def detenerPantalla(self):
            self.x=0
            self.y=420

    def cargarPantalla(self,jugador,enemigo,puntaje,pantalla):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(puntaje), True, (255, 255, 255))
        pantalla.toPantalla()
        jugador.toPantalla(self.display)
        enemigo.toPantalla(self.display)
        self.display.blit(texto,[0, 0])#imprime puntaje

    def setEscribir(self,keys,event,cadena):

        f1 = pygame.font.Font(None, 100)
        reloj1 = pygame.time.Clock()
        escribio=False
        pos_x=0
        c=0
        while escribio!=True:

             for event in pygame.event.get():

                     keys = pygame.key.get_pressed()

                     if event.type == pygame.QUIT:
                               escribio = True
                     if pygame.key.get_focused() and keys[pygame.K_KP_ENTER]!=True and keys[pygame.K_NUMLOCK]!=True :

                         for i in xrange(0,len(keys)):
                           name=pygame.key.name(i)
                           if keys[i]==1 and c<=len(cadena):
                                      cadena=cadena+str(name)
                                      text=f1.render(cadena,True,(255,255,255))
                                      self.display.blit(text,(pos_x+10,100))
                                      c=c+1
                                      pygame.event.post(event)

             pygame.event.post(event)
             reloj1.tick(30)
             pygame.display.update()

        return cadena


    def mostrarEscribir(self, cadena):
        f2 = pygame.font.Font(None,300)
        text=f2.render(cadena,True,(255,255,255))
        self.display.blit(text,(0,100))
        pygame.display.update()

    def cadenaVacia(self, cadena):
        respuesta=False
        for i in xrange(0,len(cadena)):
            if cadena[i]=="":
               respuesta=True
        return respuesta










