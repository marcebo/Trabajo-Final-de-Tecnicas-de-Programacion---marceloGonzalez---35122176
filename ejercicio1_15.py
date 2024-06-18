'''Crea una clase CarritoCompra que tenga una lista de productos. Usa
agregación para representar la relación entre un carrito de compra y los
productos que contiene.'''

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"El producto {producto.nombre} fue agregado al carrito con éxito")

    def mostrar_carrito(self):
        print("El carrito tiene estos productos:")
        for producto in self.productos:
            print(f"- {producto.nombre} (${producto.precio:.2f})")

    def eliminar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                print(f"El producto {nombre_producto} fue eliminado con éxito")
                return
        print(f"El producto {nombre_producto} no se encuentra en el carrito")

    def total_precio(self):
        total = sum(producto.precio for producto in self.productos)
        print(f'El total es de: {total}')
# Ejemplo de uso
producto1 = Producto("Carne", 5500)
producto2 = Producto("Limon", 1000)
producto3 = Producto("Papel higienico", 3500)

carrito1 = CarritoCompra()

carrito1.agregar_producto(producto1)
carrito1.agregar_producto(producto2)
carrito1.agregar_producto(producto3)

carrito1.mostrar_carrito()

carrito1.eliminar_producto("Limon")

carrito1.mostrar_carrito()
carrito1.total_precio()
