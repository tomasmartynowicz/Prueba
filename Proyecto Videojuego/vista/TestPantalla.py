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



#Prueba Setters

jugador=Jugador(pygame.image.load('Perro4.png'),0,320,"jugador1")
jugador.setImagen(pygame.image.load('Perro4.png'))
jugador.setX(0)
jugador.setY(320)
jugador.setAlias("jugador1")

enemigo=Enemigo(pygame.image.load('rock.png'),500,320)
enemigo.setImagen(pygame.image.load('rock.png'))
enemigo.setX(1000)
enemigo.setY(320)

pantalla=Pantalla(pygame.display.set_caption("Jump the Rock"),pygame.display.set_mode((1080,420)),pygame.image.load('fondo.png'),0,0)
pantalla.setDisplay(pygame.display.set_mode((1080 ,420)))
pantalla.setImagen(pygame.image.load('marte2.jpg'))
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
saltar=False
#Bucle principal del videojuego
while salir != True and newGame.actualizarPantalla()==False:
    newGame.actualizarPantalla()


    newGame.pantalla.moverPantalla()


    if saltar==True:
          newGame.jugador.subir()
    else:
          newGame.jugador.bajar()

    if newGame.puntaje>-1:
        newGame.enemigo.desplazarIzquierda()
        enemigo.setImagen(pygame.image.load('rock.png'))
        newGame.setEnemigo(enemigo)

    if newGame.puntaje>=500:
        newGame.enemigo.desplazarIzquierda()
        enemigo.setImagen(pygame.image.load('rock2.png'))
        newGame.setEnemigo(enemigo)

    if newGame.puntaje>=1000:
        newGame.enemigo.desplazarIzquierdaRapido()
        enemigo.setImagen(pygame.image.load('rock3.png'))
        newGame.setEnemigo(enemigo)

    for event in pygame.event.get():

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and saltar==False:
                saltar=True
            else:
                saltar=False

            if event.type == pygame.QUIT:
                      salir = True


    reloj1.tick(30)
    pygame.display.update()


pygame.quit()
quit()




