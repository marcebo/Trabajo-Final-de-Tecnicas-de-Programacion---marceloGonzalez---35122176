'''Desarrolla un juego de simulación de vida donde los "seres" pueden ser
plantas, animales, personas, etc. Cada ser debe tener atributos como
energía, salud, edad, etc., y comportamientos específicos según su tipo.'''

class Seres:
    def __init__(self, energia, salud, edad):
        self.energia = energia
        self.salud = salud
        self.edad = edad


class Plantas(Seres):
    def __init__(self, energia, salud, edad, tipo_suelo):
        super().__init__(energia, salud, edad)
        self.tipo_suelo = tipo_suelo

class Animales(Seres):
    def __init__(self, energia, salud, edad):
        super().__init__(energia, salud, edad)


class Personas(Seres):
    def __init__(self, energia, salud, edad):
        super().__init__(energia, salud, edad)

        
