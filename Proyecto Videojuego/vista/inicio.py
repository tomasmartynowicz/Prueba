#from Clases.Menu import Clase     Asi se importa una clase. "Clases" es la carpeta
#                                  "Menu" el archivo .py y "clase" la clase que se importa.
#                                  Creo que la subclase se importa automaticamente junto con la clase. No estoy seguro.

import pygame
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla

pygame.init()


salir = False

reloj1 = pygame.time.Clock()


# Definir colores
BLANCO = (255, 255, 255)

newGame=Juego()
newGame.crearPantalla()
newGame.mostrarPuntaje()
newGame.mostrarJugador()
#newGame.mostrarEnemigo()
#newGame.reproducirSonido()


#Bucle principal del videojuego
while salir != True:

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        newGame.crearPantalla()
        #newGame.moverPantalla()

        if keys[pygame.K_SPACE]:
             newGame.jugador.saltar()
             newGame.mostrarJugador()
             newGame.mostrarEnemigo()
             newGame.enemigo.desplazarIzquierda()
        if event.type == pygame.QUIT:
                salir = True


    reloj1.tick(30)

    pygame.display.update()





pygame.quit()
quit()




