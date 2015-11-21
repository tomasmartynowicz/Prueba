import pygame

class Puntaje(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Puntaje,self).__new__(self)
         self.valor=0
         self.fuente = pygame.font.Font('HEADTH__.ttf', 60)
      return self._instance

    def toPantalla(self,display):
        self.texto = self.fuente.render("SCORE: "+str(self.valor), True, (255, 255, 255))
        display.blit(self.texto,[500, 300])#imprime puntaje

    def toPuntaje(self,display,valor,x):
        self.texto=self.fuente.reder("SCORE: "+str(valor), True, (255, 255, 255))
        display.blit(self.texto,[500, 100+x])


    def toListaPuntaje(self,display,lista_puntaje):
         x=10
         text=self.fuente.render("Lista de puntajes: SCORE - ALIAS", True, (255, 255, 255))
         display.blit(text,[80, 50])

         lista_puntaje=self.burbuja(lista_puntaje)

         for member in lista_puntaje:
            text=self.fuente.render("            "+str(member.puntaje)+"-"+str(member.jugador.alias), True, (255, 255, 255))
            display.blit(text,[280, 100+x])
            x=x+50

    def burbuja(self, arrayLista):
            lenD = len(arrayLista)
            for i in range(-1,lenD-1):
                for j in xrange(lenD-1,i+1,-1): #incremento -1 para  hacer j--
                         if(arrayLista[j].puntaje>arrayLista[j-1].puntaje):
                                    self.intercambiar(arrayLista,j,j-1)
            return arrayLista



    def intercambiar(self,arrayLista, indice1, indice2):
        tmp=arrayLista[indice1]
        arrayLista[indice1]=arrayLista[indice2]
        arrayLista[indice2]=tmp
