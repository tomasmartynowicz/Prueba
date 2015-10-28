import Personaje.py

class Jugador(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
    def __init__(self):                                          #La funcion __init__ aca esta puesta para llamar a __init__ de la clase base
        super(Jugador,self).__init__                           #A mi me funciona sin tener que ponerla pero asi compila seguro.
        self.alias="jugador1"
        #self.controles
        #self.listaAnimacion en contruccion         #Ejecuto el metodo de la clase base
    def saltar(self):
        print 'en contruccion'
    def animar(self):
        print 'en contruccion'