'''
tema:  06 - ciclos
        A - while 
        B - for 
        C - break 
        D - continue 

ejercicio:  
01 - número del 0 al 5 con while 
02 - número del 0 al 5 con for

'''
'''
::::::::::::::::::::::::::::::
        A - while
::::::::::::::::::::::::::::::

el ciclo while es un ciclo o bucle
en el cual se entra y no se puede escapar 
de él mientras la condición se siga cumpliendo

        a=1
        
        while a==1:
                a=2
 
::::::::::::::::::::::::::::::
        B - for
::::::::::::::::::::::::::::::

el ciclo for es un ciclo o bucle
en el cual se estará iterando por n
número de veces que se determine en
su condición

        for i in range(10):
                print(i)


::::::::::::::::::::::::::::::
        C - break
::::::::::::::::::::::::::::::

es una sentencia cuya funcionalidad es
romper un bucle aún sin terminar su ciclo
para así escapar de él

        while(1==1):
                break

::::::::::::::::::::::::::::::
        D - continue
::::::::::::::::::::::::::::::

es una sentencia cuya funcionalidad es
saltar al siguiente ciclo en el bucle,
es decir,

supongamos que estas haciendo uso de "for"
el cual será recorrido 5 veces, pero usted desea
que en el tercer recorrido su código no ejecute la lógica
dentro del ciclo for y que salte al cuarto recorrido sin
hacer nada de lo que está programado, eso quedaría
de la siguiente forma:

        for i in range(5):

                if i == 3:
                   continue # dejamos de ejecutar la logica y saltamos al cuarto ciclo
                
                print(i)

'''

#----------------------------------------------

'''
::::::::::::::::::::::::::::::::::::::::::::::::
    01 - número del 0 al 5 con while
::::::::::::::::::::::::::::::::::::::::::::::::
'''
print('\n01 - numero del 0 al 5 con while\n')
contador=0

while contador < 5:
        print(f' i:{contador+1}')
        contador+=1
'''
::::::::::::::::::::::::::::::::::::::::::::::::
    02 - número del 0 al 5 con for
::::::::::::::::::::::::::::::::::::::::::::::::
'''
print('\n02 - numero del 0 al 5 con for\n')

for i in range(5):
        print(f' i:{i+1}')
        