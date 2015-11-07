import pygame
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla

pygame.init()



reloj1 = pygame.time.Clock()


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
salto = False
tiempo=1
tiempoEnemigo=1
salir=False


#Prueba Setters

jugador=Jugador('Perro4.png',0,320,"jugador1")


enemigo=Enemigo('rock.png',1000,320)

pantalla=Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'fondo.png',0,0)
pantalla.setDisplay(1080 ,420)
pantalla.setImagen('marte2.jpg')
pantalla.setNombre("Jump the Rock")
pantalla.setX(0)
pantalla.setY(0)



newGame=Juego(jugador,enemigo,pantalla,0,'dog.mp3')
newGame.setJugador(jugador)
newGame.setEnemigo(enemigo)
newGame.setPantalla(pantalla)
newGame.setPuntaje(0)
newGame.setSonido('Yet Another Movie.mp3')

newGame.actualizarPantalla()

newGame.reproducirSonido()

saltar=False
#Bucle principal del videojuego
while salir != True:
     newGame.actualizarPantalla()
     newGame.pantalla.moverPantalla()

     newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)
     tiempoEnemigo=newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)

     #Cambia enemigo segun puntaje

     if newGame.puntaje>=500 and tiempoEnemigo==1:
        enemigo.setImagen('rock2.png')
        newGame.setEnemigo(enemigo)

     if newGame.puntaje>=1000 and tiempoEnemigo==1:
        enemigo.setImagen('rock.png')
        newGame.setEnemigo(enemigo)

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


     pygame.event.post(event)
     reloj1.tick(30)

     pygame.display.update()
<<<<<<< HEAD
=======

>>>>>>> 19b8e0d7a598f29a79c637cd3e403773422a507c


pygame.quit()
quit()

