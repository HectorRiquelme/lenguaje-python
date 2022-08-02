'''
tema:  08 - funciones
        A - funcion 
        B - parametros 
        C - retornos 
        D - argumentos variables 

ejercicio:
01 - funcion con *args para sumar 
02 - funcion con *args para multiplicar
03 - calculadora de impuestos

'''

'''
::::::::::::::::::::::::::::::
        A - funcion
::::::::::::::::::::::::::::::

las funciones son utilizadas para atomizar 
funcionalidades, danto la posibilidad
de ordenar y reutilizar codigo

    def funcion():
        print('soy una funcion')

::::::::::::::::::::::::::::::
        B - parametros
::::::::::::::::::::::::::::::

una función puede establecer parametros
que son datos de entrada para ser utilizados dentro
de la funcion

    def funcion( parametro1 , parametro2 ):
        print(parametro1+parametro2)

se puede definir el tipo de dato que se espera un parametro,
sin embargo, esto es solo de modo ilustrativo y de orientacion,
al no ser un lenguaje fuertemente tipado, la función podría recibir
de todas maneras otro tipo de dato en sus parametros

    def funcion(parametro: int)
        print(parametro)
        
las funciones tambien puede tener un parametro con un valor 
argumento por default, de forma tal que si la funcion no recibe un argumento
al momento de ser utilizada, entonces el parametro toba dicho valor

    def funcion(parametro: int = 100)
        return parametro

::::::::::::::::::::::::::::::
        C - retornos
::::::::::::::::::::::::::::::

el retorno en una funcion es el valor que esperamos
como resultado luego de que dicha funcion haya sido ejecutada

    def funcion_suma(parametro1, parametro2):
        return parametro1 + parametro2

tambien es posible indicar de forma ilustrativa lo que esperamos
que la funcion deba retornar

    def funcion(parametro: int) -> int
        return parametro * parametro

::::::::::::::::::::::::::::::
        D - argumentos variables
::::::::::::::::::::::::::::::

hablamos de argumentos variables cuando una función es capaz de recibir
más de un valor de un argumento, donde estos no han especificados.
Las formas utilizadas para ingresar argumentos variables a una funciones
es;
 mediante un parametro tipo tupla, ateponiendo un asterico al parametro:
 
        def funcion(*args)

 o un parametro tipo diccionario, anteponiendo dos asteriscos al parametro:

        def funcion(**wargs)

    
'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - funcion con *args para sumar
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print(f'\n01 - funcion con *args para sumar\n')

def sumar(*args) -> int:
    
    resultado = 0
    for valor in args:
        resultado += valor

    return resultado

print('resultado de suma:',sumar(4,5))

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - funcion con *args para multiplicar
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print(f'\n02 - funcion con *args para multiplicar\n')

def multiplicar(*args) -> int:
    
    resultadom = 1
    
    for valor in args:
        resultadom *= valor

    return resultadom
print('resultado de multiplicacion:',multiplicar(4,5))


'''
::::::::::::::::::::::::::::::::::::::::::::::::
    03 - calculadora de impuestos
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print(f'\n03 - calculadora de impuestos\n')

pago = int(input('proporcione el pago:'))
impuesto = int(input('proporcione el impuesto:'))

def calcularImpuesto(pago: int = 1, impuesto: int = 1) -> float:

    pago_con_impuesto = pago + impuesto * (pago/100)

    return pago_con_impuesto

print('pago con impuesto: ',calcularImpuesto(pago,impuesto))
