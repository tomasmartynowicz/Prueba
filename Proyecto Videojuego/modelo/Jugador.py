import pygame
from Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen,x,y,alias):
            Personaje.__init__(self,imagen,x,y)              #A mi me funciona sin tener que ponerla pero asi compila seguro.
            self.alias=alias
            self.t = 1
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

    #Getters and Setters
        def setImagen(self, imagen):
            self.imagen=pygame.image.load(imagen).convert_alpha()
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

        def escribirAlias(self,salir,event,pantalla):
                escribio=False
                reloj1 = pygame.time.Clock()
                keys = pygame.key.get_pressed()

                while keys[pygame.K_ESCAPE]!=True:
                    pantalla.toPantalla()
                    pantalla.mensajeIngrese()
                    pantalla.mostrarCadena(self.alias)

                    if pygame.key.get_focused():
                               keys = pygame.key.get_pressed()

                               escribio=True
                               reloj1.tick(8)


                    for event in pygame.event.get():


                     if escribio:
                            self.alias=pantalla.setEscribir(keys,self.alias)
                            escribio=False



                    pygame.event.post(event)

                    pygame.display.flip()

                return salir,event,pantalla




