'''Crea una clase abstracta llamada Animal que tenga métodos abstractos
como hacer_sonido() y moverse(). Luego, crea clases concretas como Perro,
Gato, Pájaro, etc., que hereden de Animal y proporcionen implementaciones
concretas para estos métodos. '''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def moverse(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        print ('Guau')
    
    def moverse(self):
        print ('El perro esta corriendo')
    

class Gato(Animal):
    def hacer_sonido(self):
        print ('Miau')
    
    def moverse(self):
        print ('El gato esta saltando')
    

class Pajaro(Animal):
    def hacer_sonido(self):
        print ('Pio pio')

    def moverse(self):
        print ('El pajaro está volando')
    

# Ejemplo
perro1 = Perro('Toto')
perro1.hacer_sonido()
perro1.moverse()

gato1 = Gato('Coco')
gato1.hacer_sonido()
gato1.moverse()

pajaro1 = Pajaro('Ramon')
pajaro1.hacer_sonido()
pajaro1.moverse()
       

