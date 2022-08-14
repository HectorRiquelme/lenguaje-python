'''
tema: 03 - tipo de datos
       A - tipos de datos existentes
       B - identificar el tipo de dato de una variable

ejercicio: 
01 - imprimir los tipos de datos
02 - califica tu dia
'''
'''
::::::::::::::::::::::::::::::::::::::::::
       A - tipos de datos existentes
::::::::::::::::::::::::::::::::::::::::::

los tipos de datos que existen en python son los siguientes

              int    : entero         ej: 4
              complex: complejo       ej: 4,5j
              float  : flotante       ej: 3.14
              str    : string         ej: "soy un texto"
              bool   : boleano        ej: True
              list   : list           ej: [dato1,"dato2"]
              tuple  : tupla          ej: (dato1,"dato2")
              set    : set            ej: {datoUnico1,datoUnico2}
              dict   : diccionario    ej: {"llave":"valor"}


si categorizamos, los tipos de datos existentes serían:

Numeric :         - Integer            : int
                  - Complex            : compĺex
                  - Float              : float

                  # Dictionary         : dict

                  # Boolean            : bool

                  # Set                : set

Sequence type :   - String             : str
                  - List               : list
                  - Tuple              : tuple


::::::::::::::::::::::::::::::::::::::::::::::::::
 B - identificar el tipo de dato de una variable
::::::::::::::::::::::::::::::::::::::::::::::::::

 se puede determinar el tipado de la variable con la función 'type(<variable>)'

'''
#--------------------------------------------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
01 - imprimir los tipos de datos
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print("\n01 - imprimir los tipos de datos\n")

entero = 1
print("entero:",type(entero))             #resultado: <int>

flotante = 1.22
print("flotante:",type(flotante))         #resultado: <float>

complejo = complex(8,5)
print("complejo:",type(complejo))         #resultado: <complex>

diccionario= {'clave':'dato1','clave_dos':'dato2'}
print("diccionario:",type(diccionario))   #resultado: <dict>

boleano = True
print("boleano:",type(boleano))           #resultado: <bool>

seter = {"valor1","valor2",3}
print("seter:",type(seter))               #resultado: <set>

cadena = "string"
print("cadena:",type(cadena))             #resultado: <str>

lista = [1,2,"texto",4.21]
print("lista:",type(lista))               #resultado: <list>

tupla = ("dato1",2,"dato3")
print("tupla:",type(tupla))               #resultado: <tuple>

'''
::::::::::::::::::::::::::::::::::::::::::::::::
       02 - califica tu dia
::::::::::::::::::::::::::::::::::::::::::::::::
'''
print("\n02 - califica tu dia\n")

calificacion = input('califica tu día (rango del 1 al 10)')

print(f'\n mi día estuvo: {calificacion}')