'''Implementa un sistema de gestión de inventario para una tienda que incluya
clases como Producto, Inventario, Proveedor, etc. El inventario debe ser
capaz de realizar operaciones como agregar productos, actualizar
existencias, etc.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for prod in self.productos:
            if prod.nombre == nombre:
                return prod
        return None


class Proveedor:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.productos_suministrados = []

    def asociar_producto(self, producto):
        self.productos_suministrados.append(producto)


#Ej
producto1 = Producto("Camiseta", 20, 100)
producto2 = Producto("Zapatillas", 50, 50)

inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

proveedor1 = Proveedor("Proveedor SRL", "Calle Falsa 123")
proveedor1.asociar_producto(producto1)
proveedor1.asociar_producto(producto2)

