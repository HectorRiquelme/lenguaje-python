'''
tema:  19 - manejo de excepciones
        A - manejo de errores
        B - tipos de excepciones
        C - else y finally

ejercicio:
01  -   implementar excepciones con else y finally

'''
'''

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                A - manejo de errores
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Existen ocasiones en que al codificar nos encontremos con errores
que no podamos "controlar", que exista la posibilidad de que un error
se nos presente aunque le agreguemos todas las validaciones que creamos necesarias,
entonces, como evitar que nuestra aplicación sufra una caída?

Para estos casos nos sería útil usar la herramienta de control de errores
"try except" en la cual ingresamos nuestro código de forma regular
dentro del espacio de nuestro "try"


                try:
                        #codigo que queremos que sea controlado


luego de que hemos ingresado nuestro código establecemos el control de error
al usar "except"


                try:
                        #codigo que queremos que sea controlado
                
                except Exception as e:

                        # acción que queremos que se realice en caso de caer en un error


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                B - tipos de excepciones
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

en python es posible que los errores sean identificados por un tipo
de error en específico, es decir, si en un caso en particular
quisieramos validar especificamente un error aritmético entonces podríamos
usar la excepción ArithmeticError


                                   BaseException
                                        |
                                     Exception
                                        |
        -------------------------------------------------------------------------
        |                  |                 |               |                  |
ArithmeticError         OSError         RuntimeError    LookupError       SyntaxError
        |                  |                                 |                  |
ZeroDivisionError          |                                 |          IndentationError
                           |                          ----------------
                   -----------------                  |              |
                  |                 |           IndexError        KeyError
          FileNotFoundError   PermissionError


pero, para qué nos puede servir usar una Exception específica si la global las cubre a todas?
pues, un try puede llevar muchos except de la mano, nos puede servir para realizar una acción
diferente para cada tipo de exception que encontremos


                a = '10'
                b = 0
                resultado = None
                try:
                        resultado = a / b

                except ZeroDivisionError as e:
                        
                        print('soy un error al divir por 0')

                except TypeError as e:
                        
                        print('soy un error al usar un strung como variable numérica')

                except Exception as e:
                        
                        print('soy otro tipo de error')

                

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                C - else y finally
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

también es posible usar un bloque llamado "else" , el cuál es uso
para realizar acción solo si no ha ocurrido ninguna excepción,
es decir, si ocurre una excepción, no accedemos a este bloque

Si lo que deseamos es establecer un bloque en el que se ejecuten acción
tanto si el código se ejecutó correctamente o entró en una excepción,
entonces podríamos usar el bloque "finally"


                a = '10'
                b = 0
                resultado = None
                try:
                        resultado = a / b

                except Exception as e:
                        
                        print('soy otro tipo de error')

                else:

                        print('no ha ocurrido ningun error')

                finally:

                        print('me ejecuto independientemente de si existen errores o no')


'''
#--------------------------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
01  -   implementar excepciones con else y finally
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''

a = '10'
b = 0
resultado = None
try:
        resultado = a / b

except Exception as e:
        
        print('soy otro tipo de error')

else:

        print('no ha ocurrido ningun error')

finally:

        print('me ejecuto independientemente de si existen errores o no')
