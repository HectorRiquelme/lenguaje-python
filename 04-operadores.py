'''
tema: 04 - operadores
       A - operadores aritméticos
       B - operadores de asignación
       C - operadores de comparación
       D - operadores lógicos

ejercicio: 
01 - calcular área de un rectángulo
02 - par o impar
03 - mayoria de edad
04 - tienda de libros
'''
'''
::::::::::::::::::::::::::::::::::::::::::
       A - operadores aritméticos
::::::::::::::::::::::::::::::::::::::::::

Los operadores aritméticos son utilizados para realizar
cálculos matemáticos, los cuales son:


              suma              : +
              resta             : -
              multiplicación    : *
              división          : /
              división (enteros): //
              resto (mod)       : %


::::::::::::::::::::::::::::::::::::::::::
       B - operadores de asignación
::::::::::::::::::::::::::::::::::::::::::

son utilizados para alterar el valor de una variable
tomando como base su valor actual:


       sumar algo a una variable       : variable += 1
       resta algo a una variable       : variable -= 1
       multiplicar algo a una variable : variable *= 1
       divir algo a una variable       : variable /= 1


::::::::::::::::::::::::::::::::::::::::::
       C - operadores de comparación
::::::::::::::::::::::::::::::::::::::::::


              igual         que :   ==
              distinto      que :   !=
              mayor         que :   >
              mayor o igual que :   >=
              menor         que :   <
              menor o igual que :   <=


::::::::::::::::::::::::::::::::::::::::::
       D - operadores lógicos
::::::::::::::::::::::::::::::::::::::::::

                     -and
                     -or
                     -not
'''
#--------------------------------------------------------
'''
::::::::::::::::::::::::::::::::::::::::::
   01 - calcular area de un rectángulo
::::::::::::::::::::::::::::::::::::::::::
'''

print('\n------ 01 - calcular área de un rectangulo ------\n')

alto =  int(input('indicar alto de un rectangulo: '))
ancho = int(input('indicar ancho del rectangulo: '))

perimetro = (alto + ancho) * 2
area = alto * ancho

print(f'\nperimetro del rectangulo : {perimetro}')
print(f'\narea del rectangulo : {area}')

'''
::::::::::::::::::::::::::::::::::::::::::
   01 - 02 - par o impar
::::::::::::::::::::::::::::::::::::::::::
'''

print('\n----- 02 - par o impar -----\n')


numero_ingresado = int(input('ingrese un numero: '))

if numero_ingresado%2 == 0:

       print(f'\nel numero ingresado [{numero_ingresado}] es par')
else:
       print(f'\nel numero ingresado [{numero_ingresado}] es impar')


'''
::::::::::::::::::::::::::::::::::::::::::
       03 - mayor de de edad
::::::::::::::::::::::::::::::::::::::::::
'''

print('\n----- 03 - mayor de de edad -----\n')

edad = int(input('indique edad: '))

if edad < 18:
       print('es menor de edad')
else:
       print('es mayor de edad')

'''
::::::::::::::::::::::::::::::::::::::::::
       04 - tienda de libros
::::::::::::::::::::::::::::::::::::::::::
'''

print('\n----- 04 - tienda de libros -----\n')

nombre= input('ingrese nombre del libro: ')
id= int(input('ingrese id del libro: '))
precio= int(input('ingrese precio del libro: '))
envio= input('envio del libro gratuito? (True or False): ')

envio = bool(envio)

print(f'''\n
nombre del libro : {nombre} \n
id del libro : {id} \n
precio del libro : {precio} \n
envio gratuito? : {envio} \n
\n''')