'''
tema:  08 - funciones
        A - función 
        B - parámetros 
        C - retornos 
        D - argumentos variables 

ejercicio:
01 - función con *args para sumar 
02 - función con *args para multiplicar
03 - calculadora de impuestos

'''

'''
::::::::::::::::::::::::::::::
        A - función
::::::::::::::::::::::::::::::

las funciones son utilizadas para atomizar acciones que se realizan
separadas del resto, dando la posibilidad de ordenar y reutilizar código


        def función():
            print('soy una función')


::::::::::::::::::::::::::::::
        B - parámetros
::::::::::::::::::::::::::::::

una función puede establecer parámetros
que son datos de entrada para ser utilizados dentro
de la función


    def función( parámetro1 , parámetro2 ):
        print(parámetro1+parámetro2)


se puede definir el tipo de dato que se espera en un parámetro,
sin embargo, esto es solo de modo ilustrativo y de orientación,
al no ser un lenguaje fuertemente tipado, la función podría recibir
de todas maneras otro tipo de dato en sus parámetros


    def función(parámetro: int)
        print(parámetro)


las funciónes también pueden tener un parámetro con un valor (argumento) 
por default, de forma tal que si la función no recibe un valor
al momento de ser utilizada, entonces el parámetro toma dicho valor 
establecido previamente


    def función(parámetro: int = 100)
        return parámetro


::::::::::::::::::::::::::::::
        C - retornos
::::::::::::::::::::::::::::::

el retorno en una función es el valor que esperamos
como resultado luego de que dicha función haya sido ejecutada


    def función_suma(parámetro1, parámetro2):
        return parámetro1 + parámetro2


también es posible indicar de forma ilustrativa lo que esperamos
que la función deba retornar


    def funcion(parámetro: int) -> int:   #se espera que el retorno sea un valor entero
        return parámetro * parámetro


:::::::::::::::::::::::::::::::::::::::
        D - argumentos variables
:::::::::::::::::::::::::::::::::::::::

hablamos de argumentos variables cuando una función es capaz de recibir
más de un valor en sus argumentos y estos no han sido especificados.
Las formas utilizadas para ingresar argumentos variables a una funciónes es


  - mediante un parámetro tipo tupla, anteponiendo un asterico al parámetro:
 
            def funcion(*args)

  - o un parámetro tipo diccionario, anteponiendo dos asteriscos al parámetro:

            def funcion(**wargs)

    
'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - función con *args para sumar
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print(f'\n01 - función con *args para sumar\n')

def sumar(*args) -> int:
    
    resultado = 0
    for valor in args:
        resultado += valor

    return resultado

print('resultado de suma:',sumar(4,5))

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - función con *args para multiplicar
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print(f'\n02 - función con *args para multiplicar\n')

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
