'''
tema:  07 - colecciones
        A - introducción 
        B - listas 
        C - tuplas 
        D - sets 
        E - diccionarios 

ejercicio:
01 - uso de rangos 
02 - uso de tuplas

'''

'''
::::::::::::::::::::::::::::::
        A - introducción
::::::::::::::::::::::::::::::

en python existen distantas formas
de almacenar información, hasta el momento
hemos visto como se almacenan en variables
pero estas almacenan un solo dato,
pero y si queremos almacenar muchos datos
en una sola variable? ahí es donde aparecen
las colecciones, de las cuales veremos sus
similitudes y diferencias

::::::::::::::::::::::::::::::::::::
        B - listas
::::::::::::::::::::::::::::::::::::

        lista = [dato1,dato2]

las listas son una coleccion de objetos
con un orden determinado (poseen indices) que pueden
ser modificados, eliminados y se pueden
añadir nuevos elementos:

1-. contar elementos de una lista:

        leng(lista) # esto nos retornará "2"

2-. agregar elementos al final de la lista:

        lista.append(dato3)   #resultado: [dato1,dato2,dato3]

3-. agregar elemento en una posición especifica:

        lista.insert(1,dato4) #resultado: [dato1,dato4,dato2,dato3]

4-. eliminar ultimo elemento de una lista:

        lista.pop()           #resultado: [dato1,dato4,dato2]

5-. eliminar dato de la lista especificando el elemento a eliminar:

        lista.remove(dato1)   #resultado: [dato4,dato2]

6-. editar una posicion especifica de la lista:

        lista[0]= dato99      #resultado: [dato99,dato2]

7-. vaciar la lista:

        lista.clear()


::::::::::::::::::::::::::::::::::::
        C - tuplas
::::::::::::::::::::::::::::::::::::

        tupla = (dato1,dato2)

las tuplas al igual que las listas
tienen un orden especifico (poseen indices), sin embargo,
las tuplas no pueden ser modificadas.
Por otro lado, la forma de recorrer y leer
los datos de una tupla es igual a la de una lista.
Si en algun caso necesitara alterar una tupla, sería
necesario transformarla en una lista, realizar los cambios y luego
volver a transformarla en una tupla

1-. contar elementos de una tupla:

        leng(lista)             #resultado: esto nos retornará "2"

2-. al intentar modificar una posición especifica de la tupla:

        tupla[0] = dato99       #resultado: error


::::::::::::::::::::::::::::::::::::
        D - set
::::::::::::::::::::::::::::::::::::

   variable_set = {"dato1","dato2"}

los elementos tipo set son colecciones
que no poseen un orden en especifico(no poseen indices), por lo tanto
no es valido intentar acceder a un espacio en
especifico para buscar algún dato,
es editable, sin embargo, los datos ingresados
no pueden repetirse

1-. contar elementos de un set:

        leng(variable_set)             #resultado: esto nos retornará "2"

2-. agregar un nuevo elemento:

        variable_set.add("dato3")
        print(variable_set)             #resultados posibles=   {"dato3","dato3","dato3"} #orden aleatorio
                                                                {"dato3","dato1","dato2"} #orden aleatorio
                                                                {"dato1","dato3","dato3"} #orden aleatorio

3-. eliminar elemento:

        variable_set.discard("dato3")   #resultados posibles=   {"dato1","dato2"} #orden aleatorio
                                                                {"dato2","dato1"} #orden aleatorio


::::::::::::::::::::::::::::::::::::
        E - diccionarios
::::::::::::::::::::::::::::::::::::

        diccionario = { 'dato1':'datito1',
                        'dato2':'datito2' }

los diccionarios son colecciones cuya informacion
esta compuesta por una llave y un valor asociado a esa llave,
estos son modificables y no poseen un orden especifico (noposeen indices)

1-. contar elementos de un diccionario:

        leng(diccionario)             #resultado: esto nos retornará "2"

2-. agregar una nueva llave al diccionario:

        diccionario['dato3']= "datito3"

3-. eliminar elemento:

        variable_set.discard("dato3")   #resultados posibles=   {"dato1":"datito1","dato2":"datito2} #orden aleatorio
                                                                {"dato2":"datito2","dato1":"datito1} #orden aleatorio
-. eliminar elemento:

        variable_set.discard("dato3")   #resultados posibles=   {"dato1","dato2"} #orden aleatorio
                                                                {"dato2","dato1"} #orden aleatorio
'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - uso de rangos
::::::::::::::::::::::::::::::::::::::::::::::::
'''
# iterar rangos de 0 a 10 e imprimir numeros divisibles entre 3
print("\n01 - uso de rangos: de 0 a 10 e imprimir numeros divisibles entre 3\n")

for i in range(11):
        if i%3==0:
                print(f'{i}')

# crear rango de numeros de 2 a 6 e imprimirlos
print("\n01 - uso de rangos: numeros de 2 a 6 e imprimirlos\n")
for i in range (2,7):
        print(f'{i}')

# crear rango de numeros de 3 a 10 pero con incremento de 2 en 2
print("\n01 - uso de rangos: numeros de 3 a 10 pero con incremento de 2 en 2\n")

for i in range(3,11,2):
        print(f'{i}')


'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - uso de tuplas
::::::::::::::::::::::::::::::::::::::::::::::::
'''
#dada la siguiente tupla (13,1,8,3,2,5,8), crear una lista que contenga los número menores a 5
print("\n02 - uso de tuplas: dada la siguiente tupla (13,1,8,3,2,5,8), crear una lista que contenga los número menores a 5\n")

tupla = (13,1,8,3,2,5,8)
lista = []

for elemento in tupla:
        if elemento < 5:
                lista.append(elemento)

print(f'{lista}')
