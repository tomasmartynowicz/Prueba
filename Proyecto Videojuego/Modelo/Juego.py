from modelo.Personaje import Personaje
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Pantalla import Pantalla
from modelo.Sonido import Sonido
import pygame

class Juego(object):
    def __init__(self,jugador,enemigo,pantalla,puntaje):
        self.jugador=jugador
        self.enemigo=enemigo
        self.pantalla=pantalla
        self.puntaje=puntaje
        self.sonido=Sonido()

 #Getter and Setter
    def setJugador(self, jugador):
        self.jugador=jugador

    def setEnemigo(self, enemigo):
        self.enemigo=enemigo

    def getEnemigo(self):
            return self.enemigo

    def setPantalla(self, pantalla):
        self.pantalla=pantalla

    def setPuntaje(self, puntaje):
        self.puntaje=puntaje


 #metodos
    def actualizarPantalla(self): #retorna falso si hay colision
        perdiste=False
        self.pantalla.cargarPantalla(self.jugador,self.enemigo,self.puntaje,self.pantalla)
        if self.saltoRoca()==True:
            self.puntaje=self.puntaje+100
        if self.colision()==True:
            perdiste=True
            self.gameOver()
        return perdiste



    def colision(self):
        respuesta=False
        if self.jugador.x==self.enemigo.x and self.jugador.y==self.enemigo.y:
            respuesta=True
        return respuesta


    def saltoRoca(self):
        respuesta=False
        if self.jugador.y<300 and self.jugador.x==self.enemigo.x:
            respuesta=True
        return respuesta

    def gameOver(self):
        fuente = pygame.font.Font(None, 72)
        texto = fuente.render("Game Over!! Score: "+str(self.puntaje), True, (255, 255, 255))
        self.pantalla.display.blit(texto,[0, 0])

    def iniciarJuego(self,salir,event):
        tiempoEnemigo=1
        salto = False
        escribio=False
        reloj1 = pygame.time.Clock()
        self.sonido.playSonido(0)
        #Bucle principal del videojuego
        while salir != True and self.actualizarPantalla()!=True:

                self.pantalla.moverPantalla(0)
                self.pantalla.moverPantalla(1)
                self.pantalla.moverPiso(0)
                self.pantalla.moverPiso(1)
                self.enemigo.desplazarIzquierda2(tiempoEnemigo)
                tiempoEnemigo=self.enemigo.desplazarIzquierda2(tiempoEnemigo)

                 #Cambia enemigo segun puntaje

                if self.puntaje>=500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')

                if self.puntaje>=1000 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock4.png')
                    self.pantalla.imagen='F_TheWall.png'
                    self.pantalla.setImagen()

                if self.puntaje>=1500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock5.png')


                if self.puntaje>=2000 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')
                    self.pantalla.imagen='noche.png'
                    self.pantalla.setImagen()

                if self.puntaje>=2500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock.png')

                if self.puntaje>=3000 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock4.png')
                    self.pantalla.imagen='f_Martillo.jpg'
                    self.pantalla.setImagen()

                if self.puntaje>=3500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock5.png')


                if self.puntaje>=4000 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')
                    self.pantalla.imagen='f_puntaje.png'
                    self.pantalla.setImagen()

                if self.puntaje>=4500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock.png')


                for event in pygame.event.get():

                                 keys = pygame.key.get_pressed()


                                 if keys[pygame.K_SPACE]:
                                    salto=True


                                 if salto==True:
                                    self.jugador.saltar()
                                    if self.jugador.y==320:
                                        salto=False

                                 if event.type == pygame.QUIT:
                                         salir = True
                pygame.event.post(event)
                reloj1.tick(30)
                pygame.display.update()

        while escribio!=True:

            for event in pygame.event.get():

                self.pantalla.toPantalla()
                self.pantalla.mensajeIngrese()
                self.pantalla.mostrarCadena(self.jugador.alias)

                keys = pygame.key.get_pressed()

                if keys[pygame.K_ESCAPE]:
                    escribio=True
                if escribio!=True:
                    self.jugador.alias=self.pantalla.setEscribir(keys,event,self.jugador.alias)

            pygame.event.post(event)





