'''Crea una clase base llamada Animal con atributos como nombre y edad.
Luego, define clases derivadas como Perro, Gato, etc., que agreguen
atributos específicos y métodos relacionados con cada tipo de animal.'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre} esta ladrando')


class Gato(Animal):
    def __init__(self, nombre, edad, tamaño):
        super().__init__(nombre, edad)
        self.tamaño = tamaño

    def arañar(self):
        print(f'{self.nombre} me esta arañando')

# Ejemplo
perro1 = Perro('Spike', 4, 'Bulldog')
perro1.ladrar()

gato1 = Gato('Toto', 6, 'Mediano')
gato1.arañar()