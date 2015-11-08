import pygame

class Puntaje(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Puntaje,self).__new__(self)
         self.valor=0
         self.fuente = pygame.font.Font(None, 50)
      return self._instance

    def toPantalla(self,display):
        self.texto = self.fuente.render("Score: "+str(self.valor), True, (255, 255, 255))
        display.blit(self.texto,[500, 300])#imprime puntaje

    def toPuntaje(self,display,valor,x):
        self.texto=self.fuente.reder("Score: "+str(valor), True, (255, 255, 255))
        display.blit(self.texto,[500, 100+x])


    def toListaPuntaje(self,display,lista_puntaje):
         x=10
         text=self.fuente.render("Lista de puntajes: ", True, (255, 255, 255))
         display.blit(text,[300, 50])

         for member in lista_puntaje:
            text=self.fuente.render("Score= "+str(member), True, (255, 255, 255))
            display.blit(text,[300, 100+x])
            x=x+30