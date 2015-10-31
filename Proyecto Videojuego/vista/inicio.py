#from Clases.Menu import Clase     Asi se importa una clase. "Clases" es la carpeta
#                                  "Menu" el archivo .py y "clase" la clase que se importa.
#                                  Creo que la subclase se importa automaticamente junto con la clase. No estoy seguro.

import pygame
pygame.init()


pygame.init()

#Inicializacion de constantes
resolucion = (1080,420)
salir = False

#Configuracion de Pantalla
display = pygame.display.set_mode(resolucion)
pygame.display.set_caption("Jump the Rock")
reloj1 = pygame.time.Clock()


imagen=pygame.image.load('fondo.png')
perro=pygame.image.load('Perro4.png')
roca=pygame.image.load('rock.png')
display.blit(imagen,[0, 0])

display.blit(roca,[900, 320])
display.blit(perro,[0, 330])

# Definir colores
BLANCO = (255, 255, 255)
#Configuracion del sonido
pygame.mixer.music.load('dog.mp3')
pygame.mixer.music.play(-1)



#texto en pantalla
fuente = pygame.font.Font(None, 25)
texto = fuente.render("Jum the rock!!", True, BLANCO)
display.blit(texto, [0, 0])



#Bucle principal del videojuego
while salir != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True


    reloj1.tick(30)
  #cmabiar color de pantalla-->  display.fill(BLANCO)
    pygame.display.update()





pygame.quit()
quit()




