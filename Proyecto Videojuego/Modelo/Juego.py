from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
import pygame

class Juego(object):
    def __init__(self,jugador,enemigo,pantalla,puntaje,sonido):
        self.jugador=jugador
        self.enemigo=enemigo
        self.pantalla=pantalla
        self.puntaje=puntaje
        self.sonido=pygame.mixer.music.load(sonido)

 #Getter and Setter
    def setJugador(self, jugador):
        self.jugador=jugador

    def setEnemigo(self, enemigo):
        self.enemigo=enemigo

    def setPantalla(self, pantalla):
        self.pantalla=pantalla

    def setPuntaje(self, puntaje):
        self.puntaje=puntaje

    def setSonido(self, sonido):
        self.sonido=pygame.mixer.music.load(sonido)

 #metodos
    def actualizarPantalla(self): #retorna falso si hay colision
        perdiste=False
        self.pantalla.cargarPantalla(self.jugador,self.enemigo,self.puntaje,self.pantalla)
        if self.saltoRoca()==True:
            self.puntaje=self.puntaje+100
        if self.colision()==True:
            perdiste=True
            self.gameOver()
        return perdiste



    def colision(self):
        respuesta=False
        if self.jugador.x==self.enemigo.x and self.jugador.y==self.enemigo.y:
            respuesta=True
        return respuesta

    def saltoRoca(self):
        respuesta=False
        if self.jugador.y<300 and self.jugador.x==self.enemigo.x:
            respuesta=True
        return respuesta

    def mostrarPuntaje(self):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(self.puntaje), True, (255, 255, 255))
        self.pantalla.display.blit(texto,[800, 0])

    def reproducirSonido(self):
        #pygame.mixer.music.load('Yet Another Movie.mp3') #es dog.mp3
        pygame.mixer.music.play(-1)

    def gameOver(self):
        fuente = pygame.font.Font(None, 72)
        texto = fuente.render("Game Over!! Score: "+str(self.puntaje), True, (255, 255, 255))
        self.pantalla.display.blit(texto,[0, 0])





