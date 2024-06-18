'''Crea una clase abstracta llamada Vehiculo que tenga métodos abstractos
como acelerar() y frenar(). Luego, crea clases concretas como Coche, Moto,
Bicicleta, etc., que hereden de Vehiculo y proporcionen implementaciones
concretas para estos métodos.'''


from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass


class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad):
        super().__init__(marca, modelo)
        self.velocidad = velocidad
    
    def acelerar(self):
        print(f'El {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h.')

    def frenar(self):
        print(f'El {self.marca} {self.modelo} está frenando.')


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def acelerar(self):
        print(f'La {self.marca} {self.modelo} de {self.cilindrada} cc está acelerando.')

    def frenar(self):
        print(f'La {self.marca} {self.modelo} de {self.cilindrada} cc está frenando.')


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, rodado):
        super().__init__(marca, modelo)
        self.rodado = rodado

    def acelerar(self):
        print(f'La bicicleta {self.marca} {self.modelo} rodado {self.rodado} está acelerando.')

    def frenar(self):
        print(f'La bicicleta {self.marca} {self.modelo} rodado {self.rodado} está frenando.')


# Ejemplo de uso
coche1 = Coche("Peugeot", "206", 109)
moto1 = Moto("Honda", "Biz", 150)
bicicleta1 = Bicicleta("Trek", "MARLIN 8", 29)

vehiculos = [coche1, moto1, bicicleta1]

for vehiculo in vehiculos:
    vehiculo.acelerar()
    vehiculo.frenar()
