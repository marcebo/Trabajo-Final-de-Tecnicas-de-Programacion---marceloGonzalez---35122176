'''Imagina que estás desarrollando un sistema de gestión para una empresa de
comercio electrónico. Tu tarea es diseñar un conjunto de clases orientadas a
objetos para manejar productos, carritos de compra, usuarios y pedidos.
Debes crear clases como 'Producto', 'Carrito', 'Usuario' y 'Pedido'. Aplica
herencia para representar diferentes tipos de usuarios, como 'Cliente' y
'Administrador'. Utiliza la composición para gestionar la relación entre
productos y carritos, y asegúrate de que el diseño sea escalable para futuras
características del comercio electrónico. '''


class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio



class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def calcular_precio_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def imprimir_carrito(self):
        print("Carrito:")
        for producto in self.productos:
            print(f"  - {producto.nombre}: ${producto.precio:.2f}")
        print(f"Total: ${self.calcular_precio_total():.2f}")


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Usuario):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.direccion = direccion


class Administrador(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password


class Pedido:
    def __init__(self, usuario, carrito):
        self.usuario = usuario
        self.carrito = carrito
        self.estado = "Pendiente"

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def imprimir_pedido(self):
        print(f"Pedido de {self.usuario.nombre} - Estado: {self.estado}")
        print("Carrito:")
        self.carrito.imprimir_carrito()

#ejem
producto1 = Producto(1, "Producto 1", 1000)
producto2 = Producto(2, "Producto 2", 3500)
producto3 = Producto(3, "Producto 3", 9000)
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

cliente = Cliente("Krusty", "KK@gmail.com", "Calle Falsa 123")

pedido = Pedido(cliente, carrito)

pedido.imprimir_pedido()