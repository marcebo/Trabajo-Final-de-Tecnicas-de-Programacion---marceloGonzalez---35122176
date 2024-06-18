'''Imagina que estás desarrollando un sistema de gestión para una compañía
de transporte. Tu objetivo es diseñar un conjunto de clases orientadas a
objetos para manejar vehículos, rutas, conductores y clientes. Debes crear
clases como 'Vehiculo', 'Ruta', 'Conductor' y 'Cliente'. Implementa herencia
para representar diferentes tipos de vehículos, como 'Automovil' y 'Camion'.
Utiliza la composición para gestionar la relación entre rutas, conductores y
clientes, y asegúrate de que el diseño sea escalable para futuras
funcionalidades del sistema de transporte. '''

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    def imprimir_datos(self):
        print(f"Vehículo: Placa {self.placa}, Marca {self.marca}, Modelo {self.modelo}")



class Automovil(Vehiculo):
    def __init__(self, placa, marca, modelo, capacidad_pasajeros):
        super().__init__(placa, marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")



class Camion(Vehiculo):
    def __init__(self, placa, marca, modelo, capacidad_carga):
        super().__init__(placa, marca, modelo)
        self.capacidad_carga = capacidad_carga

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Capacidad de carga: {self.capacidad_carga}")



class Ruta:
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia
        self.conductores = []
        self.clientes = []

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def imprimir_datos(self):
        print(f"Ruta: {self.nombre}, Distancia: {self.distancia}")
        print("Conductores:")
        for conductor in self.conductores:
            conductor.imprimir_datos()
        print("Clientes:")
        for cliente in self.clientes:
            cliente.imprimir_datos()


class Conductor:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def imprimir_datos(self):
        print(f"Conductor: {self.nombre}, Experiencia: {self.experiencia}")



class Cliente:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def imprimir_datos(self):
        print(f"Cliente: {self.nombre}, Destino: {self.destino}")



automovil1 = Automovil("ABC123", "Toyota", "Corolla", 5)
camion1 = Camion("DEF456", "Ford", "F-150", 1000)

ruta1 = Ruta("Ruta 1", 100)
ruta1.agregar_conductor(Conductor("Juan", 5))
ruta1.agregar_cliente(Cliente("Maria", "Ciudad"))
print(ruta1.imprimir_datos())