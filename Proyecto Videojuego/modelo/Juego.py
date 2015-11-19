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
        self.enemigo2=Enemigo('rock.png',1000,320)
        self.enemigo3=Enemigo('rock4.png',1000,320)
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

        if self.jugador.x==self.enemigo2.x and self.jugador.y==self.enemigo2.y:
            respuesta=True

        if self.jugador.x==self.enemigo3.x and self.jugador.y==self.enemigo3.y:
            respuesta=True


        return respuesta


    def saltoRoca(self):
        respuesta=False
        if self.jugador.y<300 and self.jugador.x==self.enemigo.x:
            respuesta=True

        if self.jugador.y<300 and self.jugador.x==self.enemigo2.x:
            respuesta=True

        return respuesta

    def gameOver(self):
        fuente = pygame.font.Font(None, 72)
        texto = fuente.render("Game Over!! Score: "+str(self.puntaje), True, (255, 255, 255))
        self.pantalla.display.blit(texto,[0, 0])

    def iniciarJuego(self,salir,event):
        tiempoEnemigo=1
        tiempoEnemigo2=1
        tiempoEnemigo3=30
        salto = False
        escribio=False
        reloj1 = pygame.time.Clock()
        self.sonido.playSonido(0)
        self.pantalla.imagen='fondo6.png'
        self.pantalla.setImagen()
        self.pantalla.piso='piso.png'
        self.pantalla.setPiso()
        #Bucle principal del videojuego
        while salir != True and self.actualizarPantalla()!=True:

                self.pantalla.moverPantalla(0)
                self.pantalla.moverPantalla(1)
                self.pantalla.moverPiso(0)
                self.pantalla.moverPiso(1)

                #desplazar mas rapido los enemigos en funcion del tiempo
                if self.puntaje<600:
                    self.enemigo.desplazarIzquierda2(tiempoEnemigo)
                    tiempoEnemigo=self.enemigo.desplazarIzquierda2(tiempoEnemigo)

                if self.puntaje>600 and self.puntaje<2500:
                    self.enemigo.desplazarIzquierda3(tiempoEnemigo)
                    tiempoEnemigo=self.enemigo.desplazarIzquierda3(tiempoEnemigo)
                    self.enemigo2.desplazarIzquierda3(tiempoEnemigo2)
                    tiempoEnemigo2=self.enemigo2.desplazarIzquierda3(tiempoEnemigo2)

                    self.enemigo2.toPantalla(self.pantalla.display)

                if self.puntaje>2500 and self.puntaje<3000:
                    self.enemigo.desplazarIzquierda2(tiempoEnemigo)
                    tiempoEnemigo=self.enemigo.desplazarIzquierda2(tiempoEnemigo)

                    self.enemigo2.desplazarIzquierda2(tiempoEnemigo2)
                    tiempoEnemigo2=self.enemigo2.desplazarIzquierda2(tiempoEnemigo2)
                    self.enemigo2.toPantalla(self.pantalla.display)

                    self.enemigo3.desplazarIzquierda2(tiempoEnemigo3)
                    tiempoEnemigo3=self.enemigo3.desplazarIzquierda2(tiempoEnemigo3)
                    self.enemigo3.toPantalla(self.pantalla.display)


                if self.puntaje>3000:
                    self.enemigo.desplazarIzquierda3(tiempoEnemigo)
                    tiempoEnemigo=self.enemigo.desplazarIzquierda3(tiempoEnemigo)

                    self.enemigo2.desplazarIzquierda2(tiempoEnemigo2)
                    tiempoEnemigo2=self.enemigo2.desplazarIzquierda2(tiempoEnemigo2)
                    self.enemigo2.toPantalla(self.pantalla.display)


                 #Cambia enemigo segun puntaje

                if self.puntaje>=500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')

                if self.puntaje>=1000 and self.puntaje<1200 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock4.png')
                    self.enemigo2.setImagen('rock4.png')
                    self.pantalla.imagen='F_TheWall.png'
                    self.pantalla.piso='piso2.png'
                    self.pantalla.setImagen()
                    self.pantalla.setPiso()

                if self.puntaje>=1500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock5.png')
                    self.enemigo2.setImagen('rock.png')


                if self.puntaje>=2000 and self.puntaje<2200 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')
                    self.enemigo2.setImagen('rock.png')

                    self.pantalla.imagen='noche.png'
                    self.pantalla.setImagen()

                if self.puntaje>=2500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock.png')

                if self.puntaje>=3000 and self.puntaje<3200 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock4.png')
                    self.enemigo2.setImagen('rock.png')

                    self.pantalla.imagen='f_Martillo.jpg'
                    self.pantalla.setImagen()

                if self.puntaje>=3500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock5.png')


                if self.puntaje>=4000 and self.puntaje<4200 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock2.png')
                    self.sonido.stopSonido
                    self.pantalla.imagen='marte2.jpg'
                    self.pantalla.setImagen()

                if self.puntaje>=4500 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock5.png')

                if self.puntaje>=5000 and self.puntaje<5200 and tiempoEnemigo==1:
                    self.enemigo.setImagen('rock4.png')
                    self.pantalla.imagen='pinkfloyd2.png'
                    self.pantalla.setImagen()

                if self.puntaje>=5500 and tiempoEnemigo==1:
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
        self.pantalla.imagen='fondo6.jpg'





