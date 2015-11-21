import pygame
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla
from modelo.Menu import Menu
from modelo.Sonido import Sonido
from modelo.Puntaje import Puntaje
pygame.init()


reloj1 = pygame.time.Clock()


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
salto = False
tiempo=1
tiempoEnemigo=1
salir=False
escribio=False


menu=Menu()
sonido=Sonido()
puntaje=Puntaje()

sonido.playSonido(1)
menu.mostrarMenu()

#Bucle principal
while salir != True:

     jugador=Jugador('Perro4.png',0,320,"")
     enemigo=Enemigo('rock.png',1000,320)


     for event in pygame.event.get():


         keys = pygame.key.get_pressed()

         if keys[pygame.K_0] or keys[menu.opcion_instrucciones]:
            menu.mostrarInstrucciones()

         if keys[pygame.K_1] or keys[menu.opcion_jugar]:
            sonido.stopSonido()
            newGame=Juego(jugador,enemigo,menu.pantalla[1],0)
            newGame.iniciarJuego(salir,event)
            sonido.stopSonido()
            sonido.playSonido(1)
            menu.mostrarGameOver()
            puntaje.valor=newGame.puntaje
            puntaje.toPantalla(menu.pantalla[2].display)

            menu.lista_puntaje.append(newGame)




         if keys[pygame.K_2] or keys[menu.opcion_verPuntaje]:
             menu.PantallaPuntaje()#muestra la pantalla
             puntaje.toListaPuntaje(menu.pantalla[3].display,menu.lista_puntaje)

         if keys[pygame.K_3] or keys[menu.opcion_salir]:
            salir=True

         if keys[menu.opcion_menu]:
            menu.mostrarMenu()

         if event.type == pygame.QUIT:
                 salir = True

     pygame.event.post(event)
     reloj1.tick(30)

     pygame.display.update()



pygame.quit()
quit()
