'''
tema:  05 - sentencias de control
        A - if else
        B - operador ternario
        C - conversión

ejercicio:  
01 - calcular estaciones de año
02 - sistema de calificaciones

'''

'''
::::::::::::::::::::::::::::::
        A - if else
::::::::::::::::::::::::::::::

los operadores de control permiten condicionar
la logica de nuestro codigo para que ejecuten
diferentes acciones dependendiendo de las condiciones

        if valor==1:
            <realizar acción a>
        else:
            <realizar accion b>


::::::::::::::::::::::::::::::
    B - operador ternario
::::::::::::::::::::::::::::::

el operador ternario es una forma simplificada "if else"
se recomiendo usar en los casos que las condiciones se
mantengan simples

<realizar acción a>     if valor==1 else ##      <realizar acción b>


::::::::::::::::::::::::::::::
        C - conversión
::::::::::::::::::::::::::::::

si bien no es necesario especificar el tipado delas variables en python,
existen casos en los que necesitamos estar seguros que trabajamos con
un tipo de datos en especifico, eso se puede hacer de la siguiente manera:

variable= int(<valo_asignado_a_la_variable>)

'''
#----------------------------------------------
'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - calcular estaciones de año
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print('\n------ 01 - calcular estaciones de año ------\n')

otonio = 'otoño'
invierno = 'invierno'
primavera = 'primavera'
verano = 'verano'
mes_ingresado = None

mes_ingresado = int(input('ingrese mes (del 1 al 12):'))

if mes_ingresado <= 2 or mes_ingresado == 12:
    print(f'\nel mes 0{mes_ingresado} corresponde a la epoca de {verano}\n')
elif mes_ingresado <= 5:
    print(f'\nel mes 0{mes_ingresado} corresponde a la epoca de {otonio}\n')
elif mes_ingresado <= 8:
    print(f'\nel mes 0{mes_ingresado} corresponde a la epoca de {invierno}\n')
elif mes_ingresado <= 11:
    print(f'\nel mes 0{mes_ingresado} corresponde a la epoca de {primavera}\n')
else:
    print('\ningrese un valor dentro del rango\n')

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - sistema de calificaciones
::::::::::::::::::::::::::::::::::::::::::::::::
'''

print('\n------ 02 - sistema de calificaciones ------\n')

calificacion = int(input('ingrese su calificacion (rango del 1 al 10): '))

if calificacion < 6:
    print(' ha sido calificado con una : F\n')
elif calificacion < 7:
    print(' ha sido calificado con una : D\n')
elif calificacion < 8:
    print(' ha sido calificado con una : C\n')
elif calificacion < 9:
    print(' ha sido calificado con una : B\n')
elif calificacion <= 10:
    print(' ha sido calificado con una : A\n')
else:
    print(' INGRESE NOTA VALIDA\n')