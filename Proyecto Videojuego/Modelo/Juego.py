from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
import pygame

class Juego(object):
    def __init__(self):
        self.jugador=Jugador(pygame.image.load('Perro4.png'))
        self.enemigo=Enemigo(pygame.image.load('rock.png'))
        self.pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'))

    def crearPantalla(self):
        self.pantalla.display.blit(self.pantalla.imagen,[0,0])

    def crearPersonaje(self): #se tiene que pasar el personaje jugador/enemigo como parametro
        self.pantalla.display.blit(self.jugador.imagen,[0, 320])

    def reproducirSonido(self):
        pygame.mixer.music.load('dog.mp3')
        pygame.mixer.music.play(-1)

