'''Define una clase Figura con métodos como calcular_area() y
calcular_perimetro(). Luego, crea clases derivadas como Triangulo,
Cuadrado, etc., que sobrescriban estos métodos para calcular el área y
perímetro de cada figura.'''

class Figura:
    def __init__(self):
        pass

    def calcular_area(self):
        raise NotImplementedError
    
    def calcular_perimetro(self):
        raise NotImplementedError

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        lado1 = self.base
        lado3 = self.altura
        return lado1 + lado1 + lado3

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

# Ejemplo de uso
triangulo1 = Triangulo(2, 7)
cuadrado1 = Cuadrado(4)

print(f"Área del triángulo: {triangulo1.calcular_area()}")
print(f"Perímetro del triángulo: {triangulo1.calcular_perimetro()}")

print(f"\nÁrea del cuadrado: {cuadrado1.calcular_area()}")
print(f"Perímetro del cuadrado: {cuadrado1.calcular_perimetro()}")