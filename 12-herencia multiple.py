'''
tema:  12 - herencia multiple
        A - introduccion a herencia multiple
        B - prioridad en la herencia multiple

ejercicio:
01 - figura geometrica

'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        A - introduccion a herencia multiple
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

hasta ahora hemos visto como llevar a cabo la herencia desde una
clase padre hacia una clase hija, pero podrían darse escenarios
en los que se requiera que una clase hija hereda de las caracteristicas
de más de una clase, a esto lo llamamos herencia multiple


        class ClaseHija( PadreUno, PadreDos):


pero , según vimos anteriormente, cuando tenemos una clase padre
especificamos que usaremos el constructor de la clase padre mediante
el uso de la función super(), pero en este caso, si usamos la función super()
estaremos utilizando el constructor de la clase PadreUno o PadreDos?


                class ClaseHija( PadreUno, PadreDos):

                    def __init__(selft,atributo_uno,atributo_dos):
                        super().__init__(atributo_uno)  # no sabemos a cual padre
                                                        # le estamos pasando ese atributo


en este caso no podemos saber si estamos llamando al método constructor
del PAdreUno o PadreDos, entonces para solucionar este problema es necesario
especificar la clase a la cual estamos invocando su constructor


                class ClaseHija( PadreUno, PadreDos):

                    def __init__(selft,atributo_uno):
                        PadreUno.__init__(atributo_uno)  
                        PadreDos.__init__(atributo_dos)  



::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        B - prioridad en la herencia multiple
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

al trabajar con herencia multiple, es posible que se tengas métodos
con el mismo nombre en ambas clases padres, para estos casos será necesario
saber a cual clase va a tomar como prioridad antes de buscar el método en otra clase,
existe una función llamada MRO que sirve para indicar la prioridad de ejecución de
métodos de una clase


                print( ClasehHija.mro() )


'''

#-----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
        01 - figura geometrica
::::::::::::::::::::::::::::::::::::::::::::::::
'''

class FiguraGeometrica:

    def __init__(self, alto, ancho) -> None:
        self._alto = alto
        self._ancho = ancho

    def __str__(self):
        return f'FiguraGeometrica [alto:{self._alto} - ancho:{self._ancho}]'

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto) -> None:
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        self._ancho = ancho


class Color:
    
    def __init__(self,color) -> None:
        self._color=color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color) -> None:
        self._color=color

    def __str__(self):
        return f'Color [color:{self._color}]'


class Rectangulo(FiguraGeometrica,Color):

    def __init__( self, alto, ancho, color) -> None:
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__( self, color)

    def area(self):
        return int(self.alto) * int(self.ancho)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}---{Color.__str__(self)}'


rectangulo = Rectangulo(4,3,"rojo")
print(rectangulo)
print(rectangulo.area())
