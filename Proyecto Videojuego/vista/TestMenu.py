import pygame
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla
from modelo.Menu import Menu
pygame.init()



reloj1 = pygame.time.Clock()


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
salto = False
tiempo=1
tiempoEnemigo=1
salir=False


#instancia de las clases

jugador=Jugador('Perro4.png',0,320,"jugador1")

enemigo=Enemigo('rock.png',1000,320)

#pantalla=Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'marte2.jpg',0,0)

#newGame=Juego(jugador,enemigo,pantalla,0,'dog.mp3')


menu=Menu()

menu.mostrarMenu()
#pantalla=menu.pantalla

#pantalla.blit(menu.imagen,[0,0])


#Bucle principal del videojuego
while salir != True:



     for event in pygame.event.get():


         keys = pygame.key.get_pressed()

         if keys[pygame.K_1] or keys[menu.opcion_jugar]:

            newGame=Juego(jugador,enemigo,menu.p[1],0,'dog.mp3')
            newGame.iniciarJuego(salir,event)
            newGame.terminarJuego()
            menu.mostrarMenu()


         if keys[pygame.K_2] or keys[menu.opcion_verPuntaje]:
            newGame2=Juego(jugador,enemigo,menu.p[1],0,'dog.mp3')
            newGame2.iniciarJuego(salir,event)
            menu.mostrarMenu()

         if keys[pygame.K_3] or keys[menu.opcion_salir]:
            salir=True

         if event.type == pygame.QUIT:
                 salir = True

     pygame.event.post(event)
     reloj1.tick(30)

     pygame.display.update()



pygame.quit()
quit()



