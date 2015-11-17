class Controles (object):
    instance = None
    def __init__(self):                                          #La funcion __ini__ se ejecuta cuando se crea la clase.
        self.ArrayControles
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance
