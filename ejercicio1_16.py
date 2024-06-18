'''Implementa una clase Aula que tenga una lista de estudiantes y un profesor.
Usa composición para representar la relación entre un aula y las personas
que la ocupan.'''

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Aula:
    def __init__(self, profesor):
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_aula(self):
        print(f"Profesor: {self.profesor.nombre}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")

#Ejemplo
profesor1= Profesor("Jose Lopez")
estudiante1 = Estudiante("Mirtha")
estudiante2 = Estudiante("Ramon")

aula_principal = Aula(profesor1)
aula_principal.agregar_estudiante(estudiante1)
aula_principal.agregar_estudiante(estudiante2)

aula_principal.mostrar_aula()
