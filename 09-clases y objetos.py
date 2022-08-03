'''
tema:  09 - clases y objetos
        A - fundamentos de objetos 
        B - objetos con argumentos 
        C - modificacion de atributos de una clase
        D - metodos de instancia
        E - self y atributos de instancia

ejercicio:
01 - crear clase aritmetica 

'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        A - fundamentos de objetos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

el paradigma orientado a objetos responde a la necesidad de
programar pensando en elemento de forma abstracta de forma tal
que estos puedan evolucionar en elementos más especificos 
con sus caracteristicas especificas. Pr ejemplo:

        i-. creamos un objeto vehiculo que puede moverse y frenar
        ii-. creamos el objeto auto que hereda esas funcionalidades
        iii-. creamos el objeto avion que hereda las funcionalidades de
                vehiculo pero ademas le agregamos la funcionalidad de volar

las clases son la forma en la que creamos un objeto de forma programada,
por ende podemos decir que un objeto es una instancia de una clase.

Las clases en python se definen de la siguiente forma:

        class Persnona:

                __init__(self):

                        #atributos
                        self.nombre = 'luis'
                        self.apellido = 'lopez'

                #metodos
                hablar(self):
                        print('la persona está hablando')

donde hemos creado una clase llamada persona
que cuenta con los atributos "nombre" y "apellido"
así como tambien un método llamado "hablar"

para hacer uso de esta clase solo hace falta crear 
una variable (instancia) asociada a esta clase

        instancia_de_persona= Persona()

en este punto ya sería posible acceder a los atributos y metodos
de Persona mediante la instancia creada

        #imprimir nombre
        print(instancia_de_persona.nombre)

        #imprimir apellido
        print(instancia_de_persona.apellido)

        #realiza accion "hablar"
        instancia_de_persona.hablar()

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        B - objetos con argumentos
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

cuando creamos un objeto generalmente no tendrán sus atributos
con datos de forma automatica, es decir, si creamos una instancia
de la clase "Persona" , no vamos a desear que todas se llamen "luis lopez"
creamos otra instancia probablemente con otro nombre, para poder esto
es necesario poder entregarle dicha información a nuestro objeto,
eso lo hacemos de la siguiente manera

        class Persona:

                __init__(self,nombre, apellido):

                        self.nombre = nombre
                        self.apellido = apellido

                hablar(self):
                        print('la persona está hablando')


init es una funcion especial que nos permite entregar
información al momento de crear una clase
a esto lo llamamos 'metodo constructor'

una vez creada la clase de esta forma será posible crear un
objeto con su propio nombre y apellido

        objeto_persona = Persona(self, 'hector', 'riquelme')


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        C - modificacion de atributos de una clase
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

intuitivamente, si quisieramos modificar información de un objeto
ya creado, pensariamos en acceder a la información de dicho objeto
y asignarle un nuevo valor

        objeto_persona.nombre = "carlos"

esto en rigor, funciona, sin embargo, no es la forma correcta
en la que debemos realizar dichos cambios, ya que no siempre será
posible acceder a todos los datos de un objeto desde cualquier lugar.
Este concepto es conocido como encapsulamiento el cual veremos más adelante.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        D - metodos de instancia
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

un metodo es una funcionalidad o una 'funcion' que se agrega
a una clase indicando una de las "acciones" que puede realizar este objeto.
Entre los tipos de metodos existentes hay uno llamado "metodo de instancia"
el cual puede hacer uso de las variables de instancia de un objeto.

                hablar(self):
                        print(f'la persona {self.nombre} está hablando')

la manera de identificarlos es que hace uso del parametro self
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        E - self y atributos de instancia
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

los atributos y metodos que hemos visto hasta este momento son conocidos
como "atributos y métodos de instancia", lo que quiere decir que dicha información
es propia de la instancia creada y no del objeto, más adelante veremos que
existen otro tipo de variables a los cuales es posible acceder desde cualquier instancia,
incluso directamente de la clase sin siquiera crear una instancia de la clase.

'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - crear clase aritmetica
::::::::::::::::::::::::::::::::::::::::::::::::
'''
print('\n01 - crear clase aritmetica\n')

class Aritmetica:

        def __init__(self, entrada_uno: int, entrada_dos: int):
                self.entrada_uno = entrada_uno
                self.entrada_dos = entrada_dos

        def sumar(self):
                resultado = self.entrada_uno+self.entrada_dos
                print(f'{self.entrada_uno} + {self.entrada_uno}={resultado}')

        def restar(self):
                resultado = self.entrada_uno-self.entrada_dos
                print(f'{self.entrada_uno} - {self.entrada_uno}={resultado}')

        def multiplicar(self):
                resultado = self.entrada_uno * self.entrada_dos
                print(f'{self.entrada_uno} * {self.entrada_uno}={resultado}')

        def dividir(self):
                resultado = self.entrada_uno // self.entrada_dos
                print(f'{self.entrada_uno} / {self.entrada_uno}={resultado}')

aritmetica= Aritmetica(5,5)

aritmetica.sumar()
aritmetica.restar()
aritmetica.multiplicar()
aritmetica.dividir()