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
tiempoEnemigo=1
salir=False


#Prueba Setters

jugador=Jugador('Perro4.png',0,320,"jugador1")


enemigo=Enemigo('rock.png',1000,320)

pantalla=Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'fondo.jpg',0,0)
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

#newGame.reproducirSonido()

saltar=False
#Bucle principal del videojuego
while salir != True:

     if newGame.actualizarPantalla()!=True: #mientras no pierda
        newGame.pantalla.moverPantalla()
        newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)
        tiempoEnemigo=newGame.enemigo.desplazarIzquierda2(tiempoEnemigo)
     else:
        newGame.pantalla.detenerPantalla()
        newGame.setSonido('punch.wav')
        newGame.reproducirSonido()
        pygame.display.update()
        newGame.stopSonido()

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
             salto = True

         if salto == True:
             newGame.jugador.saltar()
             newGame.actualizarPantalla()
             if newGame.jugador.y >= 320:
                 salto = False


         if event.type == pygame.QUIT:
                 salir = True


     pygame.event.post(event)
     reloj1.tick(30)

     pygame.display.update()



pygame.quit()
quit()

