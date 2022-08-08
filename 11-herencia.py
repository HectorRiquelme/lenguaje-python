'''
tema:  11 - herencia
        A - introduccion a herencia 
        B - sobreescritura

ejercicio:
01 - uso de herencia

'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        A - introduccion a herencia 
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

como hemos mencionado atenriormente, la programación orientada
a objetos responde a una logica en la que se define un concepto abstracto
para crear objetos de desde esa base se van a contruir objetos más especificos,
heredando las caracteristicas de su clase padre, la forma de heredad las carecticas
de una clase en otra es la siguiente:

    class ClaseHija(ClasePadre):

Hemos definido una clase llamada "ClaseHija" que está heredando las carasteristicas de
una clase llamada "ClasePadre"

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        B - uso de constructor de la clase padre
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    #clase padre
    class Padre:
        def __init__(self, nombre):
            self.nombre=nombre

    
    #clase hija
    Class Hija(Padre):
        def __init__(self, edad , nombre):
            self.edad=edad


en este punto hemos creado una clase Padre y una clase Hija que se "extiende"
de la clase Padre, ahora bien, cada clase cuenta con un constructor (__init__)
que está esperando información de entrada para completar la información de sus atributos


    - clase Padre está esperando que se le entre un nombre

    - clase Hija está esperando que se le entre una edad


según lo aprendido hasta este punto, sabemos que si la clase Hija se
extiende de la clase Padre, entonces el atributo perteneciente al padre (nombre)
será heredado por la clase Hija


    - atributos de clase Padre -> nombre

    - atributos de clase Hija  -> edad , nombre


con eso en consideración sería facil deducir que es necesario entregarle un nombre junto
con una edad al momento de realizar un objeto de la clase Hija


        #clase hija
        Class Hija(Padre):
            def __init__(self, edad , nombre):
                self.edad=edad

    instancia_clase_hija = Hija(edad , nombre)


pero, la idea de heredar atributos y metodos de una clase padre es poder utilizar estos
datos para no tener que volver a crear dichos atributos en la clase hija, es decir

        #clase hija

        Class Hija(Padre):
            def __init__(self, edad , nombre):
                self.edad= edad
                self.edad= nombre   #   Esto NO tiene sentido, debido a que deberiamos
                                    #   guardar el nombre en el atributo heredado por el padre
                                    #   pero en este caso lo estamos volviendo a crear


entonces, como podríamos pasarle información a la clase Hija y al mismo tiempo
asignar esa información a los atributos heredados del padre?

La respuesta está en una función llamada "super" que nos permite hacer uso
de los atributos y métodos del padre, entonces, lo que habría que hacer es llamar
al constructor del padre y entregarle y asignarle valores a sus atributos (nombre).
Eso quedaría de la siguiente manera


        #clase hija
        Class Hija(Padre):
            def __init__(self, edad , nombre):
                super().__init__(nombre)        # con super() llamamos al constructor de
                self.edad= edad                 # la clase padre


    instancia_clase_hija = Hija(edad , nombre)


de esta manera ya estariamos haciendo uso de los atributos por medio
de la herencia

    print(instancia_clase_hija.nombre)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        C - sobreescritura de métodos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

la sobre escritura de métodos se refiere a la accion de utilizar el mismo nombre
para crear varios métodos los cuales pueden ser diferenciados entre ellos
según la signatura que contenga cada uno, es decir se diferencias por sus parametros
de entrada

def nueva_funcion():
    print('función sin parametros')

def nueva_funcion(entrada_uno):
    print('función con un parametro')

def nueva_funcion(entrada_uno ,entrada_dos ):
    print('función con dos parametros')

en este caso hemos sobrecargado la función "nueva_funcion" dos veces

'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
            01 - uso de herencia
::::::::::::::::::::::::::::::::::::::::::::::::
'''

class Persona:

    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre) -> None:
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad) -> None:
        self._edad = edad

    
    def caminar(self) -> None:
        print(f'{self._nombre} está caminando')


class Doctor(Persona):
    
    def __init__(self, nombre, edad, especialidad) -> None:
        super().__init__(nombre, edad)
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._nombre
    @especialidad.setter
    def especialidad(self, especialidad) -> None:
        self._especialidad = especialidad

    def indicarEspecialidad(self) -> None:
        print(f'especialidad del doctor {self._nombre}: {self._especialidad}')

    def operar(self) -> None:
        print(f'especialidad del doctor {self._nombre} está operando')


if __name__ == "__main__":

    doctor = Doctor("hector" ,12, "cardiologo")
    
    doctor.indicarEspecialidad()

    doctor.especialidad = "neurocirujano"

    doctor.indicarEspecialidad()

    doctor.caminar()
    