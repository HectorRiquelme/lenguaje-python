'''
tema:  13 - clases abstractas
        A - introducción a clases abstractas

ejercicio:
01 - crear clase abstracta

'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        A - introducción a clases abstractas
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

las clases abstractas son clases en las que sus métodos son declarados
pero no implementados, es decir, una clase que tiene la estructura de todos
sus métodos (nombre y parametros) pero no se han definido el código interno
de esos métodos, cabe mencionar que no se pueden crear instancias directamente
de una clase abstracta, pero, para qué sirve esto entonces?


    class ClaseAbstracta(ABC):              # las clases abstractas extienden de la clase ABC

        def __init__(self, dato):
            self.variable = dato

        @abstractmethod                     # se define una clase abstracta usando decorador @abstractmethod
        def metodo_abstracto(self):         # por definición no puede estar implmentada
            pass                            


una clase abstracta se crea pensando en que sus atributos y métodos serán heredados
eventualemente por una clase hija, la cual tendrá que implementar la lógica de los
métodos de la clase padre de forma obligatoria


    class ClaseHija(ClaseAbstracta):
        def __init__(self,dato):
            super().__init__(dato):
 
        def metodo_abstracto(self)                          # el método ha sido implementado
            return 'método abstracto implementado'


'''

#-----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
        01 - crear clase abstracta
::::::::::::::::::::::::::::::::::::::::::::::::
'''

from abc import ABC, abstractmethod


class FiguraGeonetrica(ABC):

    def __init__(self, ancho, largo) -> None:
       self._ancho = ancho
       self._largo = largo

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho) -> None:
        self._ancho = ancho

    @property
    def largo(self):
        return self._largo
    @largo.setter
    def largo(self,largo) -> None:
        self._largo = largo

    @abstractmethod
    def calcular_area(self):
        pass


class ClaseHija(FiguraGeonetrica):

    def __init__(self,ancho,alto):
        super().__init__(ancho,alto)

    def calcular_area(self):
        print('método abstracto implementado')


hijo = ClaseHija(13,12)
hijo.calcular_area()