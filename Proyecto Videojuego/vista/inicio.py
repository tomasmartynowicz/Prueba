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

jugador=Jugador('Perro4.png',0,320,"jugador1")


enemigo=Enemigo('rock.png',500,320)

pantalla=Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'fondo.png',0,0)
pantalla.setDisplay(1080 ,420)
pantalla.setImagen('marte2.jpg')
pantalla.setNombre("Jump the Rock")
pantalla.setX(0)
pantalla.setY(0)




newGame=Juego(jugador,enemigo,pantalla,0,'dog.mp3')

newGame.actualizarPantalla()

newGame.reproducirSonido()
#salir=True
saltar=False
#Bucle principal del videojuego
while salir != True and newGame.actualizarPantalla()==False:
    newGame.actualizarPantalla()


    newGame.pantalla.moverPantalla()


    if keys[pygame.K_SPACE] and salto == False:
            tiempo = 1
            salto = True

    if salto == True:
            newGame.jugador.saltar(tiempo)
            newGame.actualizarPantalla()
            if newGame.jugador.y >= 320:
                salto = False
            tiempo = tiempo + 1

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

