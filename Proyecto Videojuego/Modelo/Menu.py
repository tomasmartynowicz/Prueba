from Modelo.Pantalla import Pantalla
import pygame, sys

class Menu(object):

    def __init__(self,imagen,inicio,verpuntaje,salir):
        self.imagen = imagen
        self.puntaje_nombre = []
        self.puntaje_valor = []
        self.botones = [inicio,verpuntaje,salir]
        self.pantalla = Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load(imagen),0,0)

    def verPuntajes(self):
        rojo = [255,0,0]
        espacio = ' '
        n=['1','2','3']
        c=0
        FONT = pygame.font.SysFont('monospace',40)
        y=200
        SURFACEFONT = FONT.render('MEJORES PUNTAJES',0,rojo)
        self.pantalla.display.blit(SURFACEFONT,[350,50])
        while (c <= 2):

            texto = n[c] + espacio + self.puntaje_nombre[c] + espacio + str(self.puntaje_valor[c])
            SURFACEFONT = FONT.render(texto,0,rojo)
            self.pantalla.display.blit(SURFACEFONT, [405,y])
            c=c+1
            y=y+50


    def salir(self):
        return True






