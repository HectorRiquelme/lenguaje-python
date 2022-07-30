'''
tema: 03 - tipo de datos
       A - tipos de datos existentes
       B - identificar el tipo de dato de una variable

ejercicio: 01 - imprimir los tipos de datos
           02 - califica tu dia
'''

#:::::A - tipos de datos existentes:::::

## los tipos de datos que exiten en python son los siguientes

## int    : entero
## complex: complejo
## float  : flotante
## str    : string
## bool   : boleano

## csi categorizamos, los tipos de datos existentes serían:

## Numeric :         - Integer            : int
##                   - Complex Number     : compĺex
##                   - Float              : float
###############################################
##                   # Dictionary         : dict
###############################################
##                   # Boolean            : bool
###############################################
##                   # Set                : set
###############################################
## Sequence type :   - String             : str
##                   - List               : list
##                   - Tuple              : tuple

#:::::B - identificar el tipo de dato de una variable:::::

## se puede determinar el tipado de la variable con la función 'type(<variable>)'

#--------------------------------------------------------------------------------

#:::::01 - imprimir los tipos de datos:::::
print("\n\n")
print("imprimir los tipos de datos\n\n")

entero = 1
print("entero:",type(entero))

flotante = 1.22
print("flotante:",type(flotante))

complejo = complex(8,5)
print("complejo:",type(complejo))

diccionario= {'clave':'dato1','clave_dos':'dato2'}
print("diccionario:",type(diccionario))

boleano = True
print("boleano:",type(boleano))

seter = {"valor1","valor2",3}
print("seter:",type(seter))

cadena = "string"
print("cadena:",type(cadena))

lista = [1,2,"texto",4.21]
print("lista:",type(lista))

tupla = ("dato1",2,"dato3")
print("tupla:",type(tupla))

#:::::02 - califica tu dia:::::

calificacion = input('califica tu día (rango del 1 al 10)')

print(f'\n mi día estuvo: {calificacion}')