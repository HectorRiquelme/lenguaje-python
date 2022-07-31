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
04 - convertidor de temperaturas

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



'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - funcion con *args para sumar
::::::::::::::::::::::::::::::::::::::::::::::::
'''


'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - funcion con *args para multiplicar
::::::::::::::::::::::::::::::::::::::::::::::::
'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    03 - calculadora de impuestos
::::::::::::::::::::::::::::::::::::::::::::::::
'''

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    04 - convertidor de temperaturas
::::::::::::::::::::::::::::::::::::::::::::::::
'''