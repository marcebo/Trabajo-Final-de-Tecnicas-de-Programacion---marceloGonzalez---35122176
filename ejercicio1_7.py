'''Crea una clase base Vehiculo con atributos como marca, modelo y color.
Luego, crea clases derivadas como Coche, Moto, etc., que hereden de
Vehiculo y agreguen atributos y métodos específicos.'''

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, puertas ):
        super().__init__(marca, modelo, color)
        self.puertas = puertas

    def arrancar(self):
        print(f'El {self.marca} está arrancando.')


class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def frenar(self):
        print(f'La {self.marca} está frenando.') 

# Ejemplo
coche1 = Coche('Peugeot', 206, 'Rojo', 3)
coche1.arrancar()

moto1 = Moto('Honda','BIZ', 'azul', 150)
moto1.frenar()