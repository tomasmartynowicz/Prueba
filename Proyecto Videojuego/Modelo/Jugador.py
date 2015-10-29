import Personaje

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
    def __init__(self,Personaje,alias):                                          #La funcion __init__ aca esta puesta para llamar a __init__ de la clase base
        Personaje.__init__(self,imagen,x,y)                                    #A mi me funciona sin tener que ponerla pero asi compila seguro.
        self.alias=alias
        #self.controles
        #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base

    def saltar(self):
        print 'en contruccion'
    def animar(self):
        print 'en contruccion'
