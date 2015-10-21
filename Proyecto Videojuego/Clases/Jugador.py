#Esta la estructura de basica de una clase en python.
class Clase(object):                                             #El parametro object se pone para poder crear subclases apartir de esta clase.
    def __init__(self):                                          #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.atributo = 'Este es atributo de la clase'           #El parametro self no se que significa pero tiene que ir.
    def Metodo(self):
        print 'Este es metodo de la clase'


class SubClase(Clase):                                           #Esta es la SubClase de Clase. Se define igual pero poniendo como parametro la clase base.
    def __init__(self):                                          #La funcion __init__ aca esta puesta para llamar a __init__ de la clase base
        super(SubClase,self).__init__                            #A mi me funciona sin tener que ponerla pero asi compila seguro.


Objeto = SubClase()                                              #Creo un objeto de la Subclase

Objeto.Metodo()                                                  #Ejecuto el metodo de la clase base