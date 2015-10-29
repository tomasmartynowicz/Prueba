#from Clases.Menu import Clase     Asi se importa una clase. "Clases" es la carpeta
#                                  "Menu" el archivo .py y "clase" la clase que se importa.
#                                  Creo que la subclase se importa automaticamente junto con la clase. No estoy seguro.

import pygame
import Modelo.Juego


pygame.init()

#Inicializacion de constantes
resolucion = (640,480)
salir = False

#Configuracion de Pantalla
display = pygame.display.set_mode(resolucion)
pygame.display.set_caption("Tutorial numero 1")
reloj1 = pygame.time.Clock()



#Bucle principal del videojuego
while salir != True:

    nuevoJuego=Modelo.Juego.Juego()
    nuevoJuego.jugador.imagen="/Perro4.png"
    nuevoJuego.jugador.x=300
    nuevoJuego.jugador.y=300

    nuevoJuego.enemigo.imagen="/Perro4.png"
    nuevoJuego.enemigo.x=100
    nuevoJuego.enemigo.y=100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True


    reloj1.tick(30)
    pygame.display.update()





pygame.quit()
quit()




