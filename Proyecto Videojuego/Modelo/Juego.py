from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
import pygame

class Juego(object):
    def __init__(self):
        self.jugador=Jugador(pygame.image.load('Perro4.png'),0,320,"jugador1")
        self.enemigo=Enemigo(pygame.image.load('rock.png'),1000,320)
        self.pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'),0,0)
        self.puntaje=0

    def actualizarPantalla(self):
        self.pantalla.cargarPantalla(self.jugador,self.enemigo,self.puntaje)

        if self.colision()==True:
            fuente = pygame.font.Font(None, 72)
            texto = fuente.render("Game Over!! Score: "+str(self.puntaje), True, (255, 255, 255))
            self.pantalla.display.blit(texto,[100, 0])
            pygame.event.wait()
        if self.saltoRoca()==True:
            self.puntaje=self.puntaje+10

    def colision(self):
        respuesta=False
        if self.jugador.x==self.enemigo.x and self.jugador.y==self.enemigo.y:
            respuesta=True
        return respuesta

    def saltoRoca(self):
        respuesta=False
        if self.jugador.y==150 and self.jugador.x==self.enemigo.x:
            respuesta=True
        return respuesta


    def mostrarJugador(self):
        self.pantalla.display.blit(self.jugador.imagen,[self.jugador.x, self.jugador.y])
        pygame.display.update()

    def mostrarEnemigo(self):
        self.pantalla.display.blit(self.enemigo.imagen,[self.enemigo.x, self.enemigo.y])
        pygame.display.update()

    def crearEnemigo(self):
        self.enemigo=Enemigo(pygame.image.load('rock.png'),1000,350)

    def mostrarPuntaje(self):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(self.puntaje), True, (255, 255, 255))
        self.pantalla.display.blit(texto,[800, 0])

    def reproducirSonido(self):
        pygame.mixer.music.load('dog.mp3')
        pygame.mixer.music.play(-1)





