'''
tema:  16 - sobrecarga de operadores
        A - sobrecarga de operadores

ejercicio:
01  -   sobrecargar operadores aritméticos y hacer interacción entre 2 objetos

'''
'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                A - sobrecarga de operadores
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

en el mundo del paradigma orientado a objetos es posible sobrecargar
métodos, es decir, creamos un método nuevo llamado de igual que un método
ya existente. La forma de diferenciarlos es identificando su signatura (parametros),
todo esto lo habíamos mencionado en el capítulo 11.

Ahora bien, pensemos en qué es un método, se define como las acciones que puede realizar
un objeto, acción...?! , entonces cuando sumamos o restamos, estamos realizando una acción?,
la respuesta es sí, con eso en mente, no suena ilógico el creer que es posible sobreescribir
operadores como "+" o "-" , esto es completamente posible en python, solo necesitamos
identificar el nombre de estos métodos que deseamos sobreescribir.


                        operadores aritméticos

                +   --->    __add__(self,other)
                -   --->    __sub__(self,other)
                /   --->    __truediv__(self,other)
                //  --->    __floordiv__(self,other)
                %   --->    __mod__(self,other)
                *   --->    __mul__(self,other)
                **  --->    __pow__(self,other)

                        operadores logicos

                <    --->   __lt__(self,other)
                >    --->   __gt__(self,other)
                <=   --->   __le__(self,other)
                =>   --->   __ge__(self,other)
                ==   --->   __eq__(self,other)
                !=   --->   __ne__(self,other)

                        asignacion compuestos

                -=   --->    __isub__(self,other)
                +=   --->    __iadd__(self,other)
                *=   --->    __imul__(self,other)
                /=   --->    __idiv__(self,other)
                //=  --->    __filoordiv__(self,other)
                %=   --->    __imod__(self,other)
                **=  --->    __ipow__(self,other)

'''
#--------------------------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
01  -   sobrecargar operadores aritméticos y hacer interacción entre 2 objetos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
print('01  -   sobrecargar operadores aritmeticos y hacer interacción entre 2 objetos\n')
class Persona:

        def __init__(self, nombre,edad) -> None:
                self.nombre = nombre
                self.edad = edad


        def __str__(self) -> str:
                return f'{self.nombre}'


        def __add__(self, another):
                return f'edad sumada de {self.nombre}+{another.nombre}:{self.edad+another.edad}'

persona = Persona('yo',30)
persona2 = Persona('tu',40)

print(persona+persona2)