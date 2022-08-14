'''
tema:  10 - clases y objetos
        A - fundamentos de encapsulamiento 
        B - get y set en python 
        C - atributos de solo lectura
        D - uso de módulos
        E - comprobación de módulo principal

ejercicio:
01 - crear clase aritmetica con encapsulamiento

'''
'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        A - fundamentos de encapsulamiento
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

cuando creamos un objeto, existe la posibilidad de que queramos
que sus atributos o algunos de sus atributos y métodos solo sean
accedidos desde la misma clase y no desde otro lugar, el controlar
el nivel de acceso de los atributos y métodos de una clase se le conoce
como encapsulamiento

para indicar que un atributo solo debería ser accedido dentro de la misma clase
se le define un indicador de que estamos ante un atributo "privado"


        # "_nombre" tiene guión bajo al principio de su declaración,
        #  que se traduce en una variable privada

        class Persona:
                def __init__(self)
                        self._nombre = "soy una variable privada"


de esta forma estamos indicando que esta variable debería ser tratada como
privada y no debería ser accedida ni modificada desde cualquier lugar,
sin embargo, esto es solo un indicador, ya que si intentamos leer o escribir
esta variable desde otro lugar, python lo realizará de todas formas, pero sería
una mala práctica


                persona = Persona()

                #mala práctica
                persona._nombre = "estoy cambiando el valor de _nombre"


existe otro indicador de atributos privados que sí es restrictivo pero es menos usado,
sería anteponiendo doble guíon bajo a una variable


        class Persona:
                def __init__(self)
                        self.__nombre = "soy una variable privada"


es poco usual ver el uso del "doble guíon bajo" pero a diferencia del guíon bajo simple,
este sí restringe el acceso a la variable desde fuera de la clase misma

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        B - get y set en python
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Entonces, Cuál sería la forma correcta de acceder y/o cambiar el valor
de los atributos privados de una clase?

Para realizar esta acción existen los conceptos de "getter y setter"
Estos no son más que unos métodos con la facultad
de consultar y modificar dichos atributos.


        - getter

                @property
                def nombre(self):
                        return self._nombre

        - setter

                @nombre.setter
                def nombre(self,nombre_nuevo):
                        self._nombre = nombre_nuevo


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        C - atributos de solo lectura
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

si queremos que un atributo privado pueda ser consultado desde otro lugar
que no sea la misma clase pero no queremos que este pueda ser modificado,
es necesario crear la función getter pero sin su función getter


        - getter

                @property
                def nombre(self):
                        return self._nombre


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        D - uso de módulos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

los módulos son archivos creados con código de python (.py), estos
archivos pueden contener funciones, clases y/o variables que
pueden ser importados en otro módulo para su uso

por ejemplo, si tuvieramos la clase Persona en otro módulo,
tendríamos que importar dicha clase en nuestro módulo actual


        from Persona import Persona as Personilla


- primero indica desde que archivo "from Persona"
- luego indica que es lo que va a importar desde dicho archivo "import Persona"
- finalmente y de forma alternativa se le puede dar un alias a lo importado "as Personilla"


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        E - comprobación de módulo principal
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

con módulo principal nos referimos al módulo desde el cual estamos
compilando nuestro código. Para verificar esto existe un metodo llamado "__name__"
que nos indica si un módulo es o no el principal, si este se encuentra con el valor
"__main__" es porque efectivamente si es el módulo principal


        if __name__ == "__main__":
                # realizar alguna acción

'''
#----------------------------------------------
'''
::::::::::::::::::::::::::::::::::::::::::::::::
01 - crear clase aritmetica con encapsulamiento
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print('01 - crear clase aritmética con encapsulamiento')

class Aritmetica:

        def __init__(self):
                self._valor_uno=0
                self._valor_dos=0

        @property
        def valor_uno(self):
                return self._valor_uno

        @valor_uno.setter
        def valor_uno(self,nuevo_valor_uno):
                self._valor_uno = nuevo_valor_uno

        @property
        def valor_dos(self):
                return self._valor_dos

        @valor_dos.setter
        def valor_dos(self, nuevo_valor_dos):
                self._valor_dos = nuevo_valor_dos

        def sumar(self):
                resultado = self._valor_uno+self._valor_dos
                print(f'{self._valor_uno} + {self._valor_dos}={resultado}')

        def restar(self):
                resultado = self._valor_uno-self._valor_dos
                print(f'{self._valor_uno} - {self._valor_dos}={resultado}')

        def multiplicar(self):
                resultado = self._valor_uno * self._valor_dos
                print(f'{self._valor_uno} * {self._valor_dos}={resultado}')

        def dividir(self):
                resultado = self._valor_uno // self._valor_dos
                print(f'{self._valor_uno} / {self._valor_dos}={resultado}')

        
aritmetica = Aritmetica()

aritmetica.valor_uno = 10
aritmetica.valor_dos = 5
print(aritmetica.valor_uno)
print(aritmetica.valor_dos)

aritmetica.sumar()
aritmetica.restar()
aritmetica.multiplicar()
aritmetica.dividir()