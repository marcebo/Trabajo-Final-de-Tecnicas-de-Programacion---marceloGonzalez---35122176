'''Implementa un sistema de reservas para un cine que permita a los usuarios
reservar asientos para películas. Debe haber clases como Pelicula, SalaCine,
Reserva, etc.'''

import random
class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion


class SalaCine:
    def __init__(self, numero, asientos_totales):
        self.numero = numero
        self.asientos_totales = asientos_totales
        self.asientos_disponibles = asientos_totales

    def mostrar_asientos_disponibles(self):
        print(f"Asientos disponibles: {self.asientos_disponibles}")

    def reservar_asiento(self):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            return True
        else:
            return False
        


pelicula1 = Pelicula("Spiderman", "Fantasía", 190)
sala1 = SalaCine(25, 100)

print(f"Película: {pelicula1.titulo}")
print(f"Género: {pelicula1.genero}")
print(f"Duración: {pelicula1.duracion} minutos")

sala1.mostrar_asientos_disponibles()

numero_reservas = random.randint(1, sala1.asientos_totales)
for _ in range(numero_reservas):
    if sala1.reservar_asiento():
        print("Asiento reservado con éxito.")
    else:
        print("Lo siento, no hay más asientos disponibles.")

sala1.mostrar_asientos_disponibles()




        


