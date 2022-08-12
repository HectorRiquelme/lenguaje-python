'''
tema:  16 - sobrecarga de operadores

ejercicio:

01  -   crear el siguiente sistema:

-   Computadora:
        + contadorComputadoras: int <static>
        - idComputadora: int
        - nombre: String
        - monitor: Monitor
        - teclado: Teclado
        - raton: Raton

        + str()
        + (getter y setter)

-   Monitor:
        + contadorMonitores: int <static>
        - idMonitor: int
        - marca: String
        - tamaño: Monitor

        + str()
        + (getter y setter)

-   Orden:
        + contadorOrdenes: int <static>
        - idOrden: int
        
        + agregarComputadora(Computadora)
        + str()
        + (getter y setter)

-   DispositivoEntrada
        - tipoEntrada: String
        - marca: String

        + str()
        + (getter y setter)

-   Raton
        + contadorRatones: int <static>
        - idRaton: int
-   Teclado
        + contadorTeclados: int <static>
        - idTeclado: int

        + str()

'''
#--------------------------------------------------------------

'''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            01 - laboratorio mundo PC
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
from typing import List


print('01 - laboratorio mundo PC\n')      


class Monitor:

        contadorMonitores: int = 0

        def __init__(self,marca: str,tamaño: int) -> None:

                self.aumentarContadorMonitores()
                self._idMonitor=self.contadorMonitores
                self._marca=marca
                self._tamaño=tamaño

        def __del__(self) -> None:
                self.disminuirContadorMonitores()

        def __str__(self) -> str:
                return f'Monitor :: id :{self._idMonitor} marca:{self._marca} tamaño:{self._tamaño}'
        @property
        def idMonitor(self):
                return self._idMonitor
        
        @property
        def marca(self):
                return self._marca
        
        @marca.setter
        def marca(self,marca):
                self._marca=marca
        @property
        def tamaño(self):
                return self._tamaño
        
        @tamaño.setter
        def tamaño(self,tamaño):
                self._tamaño=tamaño

        @classmethod
        def aumentarContadorMonitores(cls):
                cls.contadorMonitores += 1
        @classmethod
        def disminuirContadorMonitores(cls):
                cls.contadorMonitores -= 1                

class DispositivoEntrada:

        def __init__(self,tipoEntrada: str,marca: str) -> None:
                self._tipoEntrada=tipoEntrada
                self._marca=marca

        def __str__(self) -> str:
                return f'DispositivoEntrada :: tipoEntrada:{self._tipoEntrada} marca:{self._marca}'

        @property
        def  tipoEntrada(self):
                return self._tipoEntrada
        @tipoEntrada.setter
        def tipoEntrada(self,tipoEntrada):
                self._tipoEntrada=tipoEntrada

        @property
        def  marca(self):
                return self._marca
        @marca.setter
        def marca(self,marca):
                self._marca=marca

class Raton(DispositivoEntrada):

        contadorRatones: int = 0

        def __init__(self,tipoEntrada: str,marca: str) -> None:
                super().__init__(tipoEntrada,marca)
                self.aumentarContadorRatones()
                self._idRaton=self.contadorRatones

        def __str__(self):
                return f'{super().__str__()} Raton:: _idRaton:{self._idRaton}'
                
        def __del__(self):
                self.disminuirContadorRatones()

        @property
        def idRaton(self):
                return self._idRaton

        @classmethod
        def aumentarContadorRatones(cls):
                cls.contadorRatones += 1

        @classmethod
        def disminuirContadorRatones(cls):
                cls.contadorRatones -= 1

class Teclado(DispositivoEntrada):

        contadorTeclados: int = 0

        def __init__(self,tipoEntrada: str,marca: str) -> None:
                super().__init__(tipoEntrada,marca)
                self.aumentarContadorTeclados()
                self._idTeclado=self.contadorTeclados

        def __str__(self):
                return f'{super().__str__()} Teclado:: _idTeclado:{self._idTeclado}'

        def __del__(self):
                self.disminuirContadorTeclados()

        @property
        def idTeclado(self):
                return self._idRaton

        @classmethod
        def aumentarContadorTeclados(cls):
                cls.contadorTeclados += 1

        @classmethod
        def disminuirContadorTeclados(cls):
                cls.contadorTeclados -= 1

class Computadora:

        contadorComputadoras: int = 0

        def __init__(self,nombre: str,monitor: Monitor,teclado: Teclado,raton: Raton) -> None:

                self.aumentarContadorComputadoras()
                self._idComputadora= self.contadorComputadoras
                self._nombre=nombre                
                self._monitor=monitor
                self._teclado=teclado
                self._raton=raton

        def __str__(self) -> str:
                return f'''
                contadorComputadoras:{self.contadorComputadoras}\n
                idComputadora:{self._idComputadora},
                nombre:{self._nombre},
                monitor:{self._monitor},
                teclado:{self._teclado},
                raton:{self._raton},
                '''
        
        def __del__(self) -> None:
                self.disminuirContadorComputadoras()


        @property
        def idComputadora(self):
                return self._idComputadora

        @property
        def nombre(self):
                return self._nombre

        @nombre.setter
        def nombre(self,nombre):
                self._nombre= nombre

        @property
        def monitor(self):
                return self._monitor

        @monitor.setter
        def monitor(self,monitor):
                self._monitor= monitor

        @property
        def teclado(self):
                return self._teclado

        @teclado.setter
        def teclado(self,teclado):
                self._teclado= teclado

        @property
        def raton(self):
                return self._raton

        @raton.setter
        def raton(self,raton):
                self._raton= raton


        @classmethod
        def aumentarContadorComputadoras(cls):
                cls.contadorComputadoras += 1
        @classmethod
        def disminuirContadorComputadoras(cls):
                cls.contadorComputadoras -= 1

class Orden:

        contadorOrdenes: int = 0

        def __init__(self,computadoras) -> None:
                self.aumentarContadorOrdenes()
                self._idOrden=self.contadorOrdenes
                self._computadoras = computadoras



        def __del__(self):
                self.disminuirContadorOrdenes()

        def __str__(self) -> str:
                computadoras_str = ''

                for computadora in self._computadoras:
                        computadoras_str += computadora.__str__()

                return f'ORDEN::{self._idOrden} - computadoras:{ computadoras_str}'
        @property
        def idOrden(self):
                return self._idOrden
         
        @classmethod
        def aumentarContadorOrdenes(cls):
                cls.contadorOrdenes += 1

        @classmethod
        def disminuirContadorOrdenes(cls):
                cls.contadorOrdenes -= 1

        def agregarComputadora(self,computadora):
                self._computadoras.append(computadora)


raton1 = Raton('raton','logitech')
teclado1 = Teclado('teclado','reddragon')
monitor1 = Monitor('asus',24)
computadora1 = Computadora('pc gamer',monitor1,teclado1,raton1)

raton2 = Raton('raton','robalito')
teclado2 = Teclado('teclado','robalito')
monitor2 = Monitor('robalito',50)
computadora2 = Computadora('pc antigamer',monitor2,teclado2,raton2)

orden1 = Orden([computadora1,computadora2])
print(orden1)