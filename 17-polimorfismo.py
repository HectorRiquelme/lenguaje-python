'''
tema:  17 - polimorfismo
        A - polimorfismo

ejercicio:
01  -   sobreescribir mètodo str hacer e implementar interacción entre 2 objetos

'''
'''

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                A - polimorfismo
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Uno de los principios fundamentales en el paradigma orientado a objetos es el
polimorfismo, el cual nos indica que un mètodo puede tomar distintas formas dependiendo
del punto en el cual este es invocado, por ejemplo, si un mètodo en una la clase padre
tiene un comportamiento, el mismo nombre en una clase hija, con los mismos parametros
puede tomar otro comportamiento, aquì es donde entran en juego los conceptos de sobrecarga
y sobreescritura.

    - en la sobrecargar se crean mètodos con un mismo nombre pero con distinta signatura

    - en la sobreescritura se crean mètodos con un mismo nombre y signatura pero su comportamiento
      se redefine, pudiendo comportarse iguales o diferente entre ambas declaraciones, esto toma
      sentido cuando trabajamos con herencia


'''
#--------------------------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
01  -   sobreescribir mètodo str hacer e implementar interacción entre 2 objetos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
print('01  -  polimorfismo\n')

class Empleado:

    def __init__(self,nombre,sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self) -> str:                       # sobreescrito de la clase object
        return f'Empleado:{self.nombre} - Sueldo:{self.sueldo}' 


class Gerente(Empleado):

    def __init__(self, nombre, sueldo,departamento) -> None:
        super().__init__(nombre, sueldo)
        self.departamento = departamento


    def __str__(self) -> str:                        # sobreescrito de la clase Empleado
        return f'departamento: {self.departamento} - {super().__str__()}'

    
def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto)

empleado = Empleado('yo',5000)
imprimir_detalles(empleado)

gerente = Gerente('tu', 6000, 'qa')
imprimir_detalles(gerente)

if isinstance(empleado,Gerente):       # mètodo isInstance nos indica si una instancia pertenece a una clase en particular
    print('true')

else:
    print('false')
