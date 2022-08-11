'''
tema:  17 - polimorfismo
        A - polimorfismo

ejercicio:
01  -   sobrecargar operadores aritmeticos y hacer interacción entre 2 objetos

'''
'''

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                A - polimorfismo
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



'''
#--------------------------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
01  -   sobrecargar operadores aritmeticos y hacer interacción entre 2 objetos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
print('01  -  polimorfismo\n')

class Empleado:

    def __init__(self,nombre,sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self) -> str:
        return f'Empleado:{self.nombre} - Sueldo:{self.sueldo}'


class Gerente(Empleado):

    def __init__(self, nombre, sueldo,departamento) -> None:
        super().__init__(nombre, sueldo)
        self.departamento = departamento


    def __str__(self) -> str:
        return f'departamento: {self.departamento} - {super().__str__()}'

    
def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto)

empleado = Empleado('yo',5000)
imprimir_detalles(empleado)

gerente = Gerente('tu', 6000, 'qa')
imprimir_detalles(gerente)

if isinstance(empleado,Gerente):
    print('true')

else:
    print('false')
