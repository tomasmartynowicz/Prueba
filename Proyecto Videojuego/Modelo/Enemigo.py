import Personaje.py


class Enemigo(Personaje):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
    def __init__(self):                                          #La funcion __init__ aca esta puesta para llamar a __init__ de la clase base
        super(Enemigo,self).__init__                           #A mi me funciona sin tener que ponerla pero asi compila seguro.
    def desplazarIzquierda(self):
        print 'en contruccion'