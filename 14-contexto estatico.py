'''
tema:  14 - contexto estático
        A - introducción a los contextos
        B - variables de clase
        C - variables al vuelo
        D - métodos estáticos
        E - métodos de clase
        F - constantes

ejercicio:
01 - crear contador de objetos

'''
'''

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                A - introducción a los contextos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

hasta ahora cuando trabajamos con clases, hemos interactuado con
la instancia de una clase, es decir creamos un objeto y luego hemos 
accedido a sus métodos y atributos, pero tambén se puede interactuar con
cierto tipo de atributos y métodos sin la necesidad de crear un objeto,
interactuando directamente con la clase


                        print(MiClase.atributo_de_clase)


Para lograr hacer esto es necesario comprender la diferecia de contextos
en un una clase. los contextos nos indican en qué punto se crean cierta
información perteneciente a una clase y, por ende, diferencia desde qué punto
se puede interactuar con ellos y cuando no. Por un lado está el contexto estático
o contexto de clase, el cual crea e inicializa sus atributos y métodos al momento
de importar una clase, es decir, incluso antes de que se cree una instancia de dicha clase,
la información del contexto estático ya puede ser accedida


                        print(MiClase.atributo_de_clase)        #atributos y métodos accedidos
                        MiClase.metodo_estático()               #directamente de la clase y no
                                                                #creando una instancia

por otro lado tenemos el contexto dinámico o de instancia, en el cual su información
solo es accedida cuando se crea un objeto a partir de una clase

                        objeto_instanciado = MiClase()
                        print(objeto_instanciado.atributo_de_instancia)        #atributos y métodos accedidos
                                                                               #luego de crear un objeto

                                                                               
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                B - variables de clase
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

las varibles de clase en python son aquellas que no están definidas dentro del constructor,
es decir, si son declaradas e inicializadas fuera del constructor entonces son variables de clase


                class MiClass:

                        variable_de_clase = "soy una variable de clase"

                        __init_(self):
                                pass


lo más importante a destacar, es que las variables en este caso pertenecen a la clase y no a
la instancia, por lo tanto, su valor es transversal a todas las instancias que han sido creadas
y que se crearán en un futuro, por ejemplo, si se define que "variable_de_clase = 1", todas las instancias
verán que ese valor es  "1", ahora bien, si alguna de las instancias módifica ese valor a 
"variable_de_clase= 2", este cambios se verá reflejado en la clase, por lo tanto, si alguna otra 
instancia consulta el valor de está variable, verá que su valor es "2"


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                C - variables al vuelo
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

le decimos variables 'al vuelo' a aquellas que se crean en tiempo de ejecución,
es decir, la clase ya está definida y sin embargo, le anexamos una variable y le damos valor


                MiClase.variable_clase2= 'valor de variable al vuelo'


Esto en otro lenguajes de programción fuertemente tipado no se puede hacer, python
es bastante permisivo en varios aspectos


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                D - métodos estáticos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Los métodos estáticos, como mencionamos anteriormente, son métodos a los cuales
se puede acceder sin necesidad de crear una instancia de la clase a la que pertenece
dicho método. Para crear métodos estáticos hacemos uso del decorador @staticmethod


                @staticmethod
                def metodo_estático():
                        print('soy un método estático')


Los métodos estáticos no pueden acceder a ver a los métodos o variables de instancia,
y para acceder a las variables de clase, es necesario que esté sea acceido de forma indirecta
mediante el nombre de la clase, ejemplo


                @staticmethod
                def metodo_estático():
                        print(MiClase.variable_de_clase)


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                E - métodos de clase
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

los métodos de clase comparten varias similitudes con los métodos de estáticos, podríamos decir
que son una variable de métodos estáticos, pueden ser accedidos directamente desde la clase, 
no tienen acceso a las variables de instancia y deben ser creadas mediante un decorador @classmethod,
sin embargo, hay una diferencia importante, este tipo de métodos puede acceder a las variables de clase
de forma directa mediante un parametro "cls"(el nombre puede variar).


                @classmethod
                def metodo_de_clase(cls):
                        cls.variables de clase = 3


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                F - constantes
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

las constantes en python no son más que una convencción o reglas que se asume que hay que respetar
porque a nivel práctico las constantes no existen en este lenguaje como tal, entonces
nos fijamos si las variables están creadas con nombre en mayúsculas, esto nos indicará que hablamos de 
de constantes y no de variables


        SOY_UNA_CONSTANTE = 3.1416


'''
#-----------------------------------------------
'''
::::::::::::::::::::::::::::::::::::::::::::::::
        01 - crear contador de objetos
::::::::::::::::::::::::::::::::::::::::::::::::
'''


print('\n01 - crear contador de objetos\n')

class Persona:

        contador_de_personas = 0
        contador_de_ids = 0
        def __init__(self, nombre):

                Persona._aumentar_contador()
                self.id      = Persona.contador_de_ids
                self.nombre  = nombre
                print(f'soy persona:{self.id} - nombre:{self.nombre}')

        def __del__(self):
              Persona._disminuir_contador()
              print(f'persona:{self.id} - nombre:{self.nombre} ELIMINADA')


        @classmethod
        def _aumentar_contador(cls):
                cls.contador_de_personas += 1
                cls.contador_de_ids += 1

        @classmethod
        def _disminuir_contador(cls):
                cls.contador_de_personas -= 1

        def contar_personas(self):
                print(f'existe {Persona.contador_de_personas} personas')


persona_1 = Persona('uno')
persona_1.contar_personas()

persona_2 = Persona('dos')
persona_2.contar_personas()

persona_3 = Persona('tres')
persona_3.contar_personas()

persona_4 = Persona('cuatro')
persona_4.contar_personas()


del persona_4

persona_5 = Persona('cinco')
persona_5.contar_personas()
