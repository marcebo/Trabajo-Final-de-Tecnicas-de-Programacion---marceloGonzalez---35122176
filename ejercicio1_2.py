'''Crea una clase Persona con atributos nombre y edad. Crea un método para
imprimir los datos de la persona.'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Ejemplo de uso
persona1 = Persona('Pepe', 30)
persona2 = Persona('Pepa', 25)
persona1.mostrar_datos()  
persona2.mostrar_datos()
