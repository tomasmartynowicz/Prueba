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


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
salto = False
tiempo=1



#Prueba Setters

jugador=Jugador(pygame.image.load('Perro4.png'),0,320,"jugador1")
jugador.setImagen(pygame.image.load('Perro4.png'))
jugador.setX(0)
jugador.setY(320)
jugador.setAlias("jugador1")

enemigo=Enemigo(pygame.image.load('rock.png'),1000,320)
enemigo.setImagen(pygame.image.load('rock.png'))
enemigo.setX(1000)
enemigo.setY(320)

pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'),0,0)
pantalla.setDisplay(pygame.display.set_mode((1080,420)))
pantalla.setImagen(pygame.image.load('fondo.png'))
pantalla.setNombre(pygame.display.set_caption("Jump the Rock"))
pantalla.setX(0)
pantalla.setY(0)


newGame=Juego(jugador,enemigo,pantalla,0)
newGame.setJugador(jugador)
newGame.setEnemigo(enemigo)
newGame.setPantalla(pantalla)
newGame.setPuntaje(0)
newGame.actualizarPantalla()


#newGame.reproducirSonido()
#salir=True

#Bucle principal del videojuego
while salir != True:
    newGame.actualizarPantalla()
    newGame.pantalla.moverPantalla()
    newGame.enemigo.desplazarIzquierda()

    #enemigo2=Enemigo(pygame.image.load('rock.png'),1000,320)
    #enemigo2.toPantalla(pantalla.display)

    #enemigo3=Enemigo(pygame.image.load('rock.png'),800,320)
    #enemigo3.toPantalla(pantalla.display)

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()


        if keys[pygame.K_SPACE] and salto == False:
            tiempo = 1
            salto = True

        if salto == True:
            newGame.jugador.saltar(tiempo)
            newGame.actualizarPantalla()
            if newGame.jugador.y >= 320:
                salto = False
            tiempo = tiempo + 1


        if event.type == pygame.QUIT:
                salir = True


    reloj1.tick(30)

    pygame.display.update()





pygame.quit()
quit()




