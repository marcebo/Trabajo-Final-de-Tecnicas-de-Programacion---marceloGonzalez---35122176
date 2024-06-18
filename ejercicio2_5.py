'''Desarrolla un simulador de una ciudad donde puedas controlar aspectos
como la población, la economía, la seguridad, etc. Crea clases como
Ciudadano, Edificio, Vehículo, etc.'''

import random

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad_ciudadanos = 0
        self.economia = 0
        self.seguridad = 100
        self.edificios = []
        self.vehiculos = []
        self.transportes = []

    def agregar_ciudadano(self):
        self.cantidad_ciudadanos += 1

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_transporte(self, transporte):
        self.transportes.append(transporte)

    def mostrar_datos(self):
        print(f"Ciudad: {self.nombre}")
        print(f"Cantidad de ciudadanos: {self.cantidad_ciudadanos}")
        print(f"Economía: {self.economia}")
        print(f"Seguridad: {self.seguridad}")
        print(f"Edificios: {len(self.edificios)}")
        print(f"Vehículos: {len(self.vehiculos)}")
        print(f"Transportes: {len(self.transportes)}")


class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def trabajar(self):
        return random.randint(1000, 5000)


class Edificio:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        return f"Edificio {self.tipo}"


class Vehículo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        return f"{self.marca}"


class Transporte:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        return f"Transporte {self.tipo}"



ciudad = Ciudad("Buenos Aires")

ciudadano1 = Ciudadano("Ramon", 18)
ciudadano2 = Ciudadano("Pepita", 45)

ciudad.agregar_ciudadano()
ciudad.agregar_ciudadano()

edificio1 = Edificio("Residencial")
edificio2 = Edificio("Comercial")
ciudad.agregar_edificio(edificio1)
ciudad.agregar_edificio(edificio2)

vehiculo1 = Vehículo("Toyota")
vehiculo2 = Vehículo("Ford")
ciudad.agregar_vehiculo(vehiculo1)
ciudad.agregar_vehiculo(vehiculo2)

transporte1 = Transporte("Bondi")
ciudad.agregar_transporte(transporte1)

ciudad.mostrar_datos()
print("\nTrabajo de los ciudadanos:")
print(f"Salario de Juan: {ciudadano1.trabajar()}")
print(f"Salario de Maria: {ciudadano2.trabajar()}")