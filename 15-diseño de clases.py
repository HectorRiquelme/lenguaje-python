'''
tema: 15 - diseño de clases

ejercicio:
01  -   crear clase orden y clase producto
    -   producto puede contener muchos productos
    -   clase orden debe contener atributos: - contador de ordenes  autoincremental
                                             - id_orden     int
                                             - productos    Producto list
                                    metodos: - str

    -   clase producto debe contener atributos: - contador de productos autoincremental
                                                - id_producto       int
                                                - nombre            str
                                                - precio            float
                                        metodos: - str    
'''
#--------------------------------------------------------------

'''
:::::::::::::::::::::::::::::::::::
01 - diseño de clases
:::::::::::::::::::::::::::::::::::
'''
print('01 - diseño de clases\n')
class Producto:

    contador_de_productos = 0

    def __init__(self,nombre,precio) -> None:
        self.aumentar_contador()
        self._id_producto = self.contador_de_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return f'''
            id_producto:{self._id_producto}
            nombre:{self._nombre}
            precio:{self._precio}
        '''

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    

    @classmethod
    def aumentar_contador(cls):
        cls.contador_de_productos += 1


class Orden:

    contador_de_ordenes = 0

    def __init__(self,productos) -> None:
        self.aumentar_contador()
        self._id_orden = self.contador_de_ordenes
        self._productos = list(productos)

    def __str__(self) -> str:

        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, Productos: {productos_str}'

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos

    @classmethod
    def aumentar_contador(cls):
        cls.contador_de_ordenes += 1
    
    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_precio(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

producto1 = Producto('pan', 2000)
producto2 = Producto('leche', 980)
producto3 = Producto('juevos', 5000)

print(producto1)
print(producto2)
print(producto3)

productos = [producto1,producto2,producto3]

orden1 = Orden(productos)

print(orden1)