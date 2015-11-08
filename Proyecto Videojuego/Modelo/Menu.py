from modelo.Pantalla import Pantalla
import pygame



class Menu(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Menu,self).__new__(self)
         self.imagen=pygame.image.load('fondo.jpg')
         self.pantalla=pygame.display.set_mode((1080,420))
         self.p=[Pantalla("Jump the Rock: Menu Principal",pygame.display.set_mode((1080,420)),'fondo.jpg',0,0),Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'marte2.jpg',0,0)]
         self.nombre="Jump the Rock: Menu Principal"
         self.opcion_jugar=pygame.K_KP1
         self.opcion_verPuntaje=pygame.K_KP2      #singleton
         self.opcion_salir=pygame.K_KP3
        #lista puntaje
      return self._instance

    def mostrarMenu(self):
        self.p[0].toPantalla()

    def mostarJuego(self):
        self.p[1].toPantalla()




