import pygame
from modelo.Personaje import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
        def __init__(self,imagen):
            Personaje.__init__(self,imagen)                                 #A mi me funciona sin tener que ponerla pero asi compila seguro.
            #self.controles
            #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

        def saltar(self):
            print 'en contruccion'
        def animar(self):
            print 'en contruccion'
