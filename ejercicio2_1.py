'''Crea una clase llamada Producto que tenga atributos como nombre, precio y
cantidad_disponible. Implementa métodos para actualizar la cantidad
disponible y para mostrar la información del producto.'''

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible =  cantidad_disponible

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    def mostrar_info(self):
        print (f'{self.nombre}')
        print (f'${self.precio}')
        print (f'Stock: {self.cantidad_disponible}')


# Ejemplo
producto1 = Producto('Pelota', 1200, 25)
producto2 = Producto('Gaseosa', 1400, 13)
producto3 = Producto('Manzana', 900, 10)

producto2.mostrar_info()

producto1.actualizar_cantidad(10)
producto1.mostrar_info()