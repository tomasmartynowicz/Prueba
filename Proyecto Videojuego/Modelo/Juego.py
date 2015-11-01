from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
import pygame

class Juego(object):
    def __init__(self):
        self.jugador=Jugador(pygame.image.load('Perro4.png'),0,320,"jugador1")
        self.enemigo=Enemigo(pygame.image.load('rock.png'),1000,350)
        self.pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'))
        self.puntaje=0

    def crearPantalla(self):
        self.pantalla.display.blit(self.pantalla.imagen,[0,0])

    def mostrarJugador(self):
        self.pantalla.display.blit(self.jugador.imagen,[self.jugador.x, self.jugador.y])

    def mostrarEnemigo(self):
        self.pantalla.display.blit(self.enemigo.imagen,[self.enemigo.x, self.enemigo.y])

    def mostrarPuntaje(self):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score:0", True, (255, 255, 255))
        self.pantalla.display.blit(texto,[870, 0])

    def reproducirSonido(self):
        pygame.mixer.music.load('dog.mp3')
        pygame.mixer.music.play(-1)

