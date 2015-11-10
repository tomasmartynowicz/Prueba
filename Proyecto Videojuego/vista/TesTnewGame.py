
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla
from modelo.Sonido import Sonido

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import pygame
pygame.init()


salir = False

reloj1 = pygame.time.Clock()


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
tiempoEnemigo=1
tiempo=1
saltar=False
salto = False
sonido=Sonido()



#Prueba Setters

jugador=Jugador('colectivo.jpg',0,320,"jugador1")

enemigo=Enemigo('rock.png',500,320)

pantalla=Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'f_Martillo.jpg',0,0)
pantalla.setDisplay(1080 ,600)
pantalla.setImagen('f_Martillo.jpg')
pantalla.setNombre("Test Nuevo Juego")
pantalla.setX(0)
pantalla.setY(0)


newGame=Juego(jugador,enemigo,pantalla,0)



sonido.playSonido(1)
#salir=True
#Bucle principal del videojuego
while salir != True:

    if newGame.actualizarPantalla()!=True: #mientras no pierda
        newGame.pantalla.moverPantalla()
        newGame.actualizarPantalla()

    if newGame.puntaje>-1:
        newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)
        tiempoEnemigo=newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)

        enemigo.setImagen('rock.png')
        newGame.setEnemigo(enemigo)

    if newGame.puntaje>=300:
        newGame.enemigo.desplazarIzquierda2(tiempoEnemigo+1)
        tiempoEnemigo=newGame.enemigo.desplazarIzquierda2(tiempoEnemigo+1)

        enemigo.setImagen('rock2.png')
        newGame.setEnemigo(enemigo)

    if newGame.puntaje>=1000:
        newGame.enemigo.desplazarIzquierda2(tiempoEnemigo+1)
        tiempoEnemigo=newGame.enemigo.desplazarIzquierda2(tiempoEnemigo+1)

        enemigo.setImagen('rock3.png')
        newGame.setEnemigo(enemigo)


    for event in pygame.event.get():

                     keys = pygame.key.get_pressed()


                     if keys[pygame.K_SPACE]:
                        salto=True


                     if salto==True:
                        newGame.jugador.saltar(tiempo)
                        tiempo=newGame.jugador.saltar(tiempo)
                        if newGame.jugador.y==320:
                            salto=False
                            tiempo=1

                     if event.type == pygame.QUIT:
                             salir = True
    pygame.event.post(event)


    reloj1.tick(30)
    pygame.display.update()


pygame.quit()
quit()




