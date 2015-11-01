from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
import pygame

class Juego(object):
    def __init__(self):
        self.jugador=Jugador(pygame.image.load('Perro4.png'),0,320,"jugador1")
        self.enemigo=Enemigo(pygame.image.load('rock.png'),1000,350)
        self.pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'),0,0)
        self.puntaje=0

    def crearPantalla(self):
        self.pantalla.display.blit(self.pantalla.imagen,[self.pantalla.pos_x,self.pantalla.pos_y])


    def moverPantalla(self):
        pos_x=self.jugador.x
        pos_y=self.jugador.y
        for x in range(500):                  # animamos 500 cuadros
               self.pantalla.display.blit(self.pantalla.imagen,[pos_x,pos_y])
               self.pantalla.display.blit(self.jugador.imagen,[self.jugador.x, self.jugador.y])
               pos_x=pos_x+2
               pos_y=0
               pygame.display.update()                            # y los mostramos
               pygame.time.delay(-1)


    def mostrarJugador(self):
        self.pantalla.display.blit(self.jugador.imagen,[self.jugador.x, self.jugador.y])
        pygame.display.update()

    def mostrarEnemigo(self):
        self.pantalla.display.blit(self.enemigo.imagen,[self.enemigo.x, self.enemigo.y])
        pygame.display.update()

    def mostrarPuntaje(self):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score:0", True, (255, 255, 255))
        self.pantalla.display.blit(texto,[870, 0])

    def reproducirSonido(self):
        pygame.mixer.music.load('dog.mp3')
        pygame.mixer.music.play(-1)

