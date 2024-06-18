'''Imagina que estás trabajando en un programa de gestión de un sistema
educativo. Tu tarea es diseñar un conjunto de clases orientadas a objetos
para administrar estudiantes, profesores, asignaturas y calificaciones. Debes
crear clases como 'Estudiante', 'Profesor', 'Asignatura' y 'Calificacion'.
Implementa herencia para representar diferentes niveles de estudiantes,
como 'EstudianteRegular' y 'EstudianteAvanzado'. Utiliza la composición para
gestionar la relación entre estudiantes, asignaturas y calificaciones, y
asegúrate de que el diseño sea versátil para futuras funcionalidades del
sistema educativo. '''

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class EstudianteRegular(Estudiante):
    def __init__(self, nombre, edad, nivel_academico):
        super().__init__(nombre, edad)
        self.nivel_academico = nivel_academico

    def imprimir_datos(self):
        print(f"Estudiante Regular: {self.nombre}, Edad: {self.edad}, Nivel Académico: {self.nivel_academico}")


class EstudianteAvanzado(Estudiante):
    def __init__(self, nombre, edad, nivel_academico, especialidad):
        super().__init__(nombre, edad)
        self.nivel_academico = nivel_academico
        self.especialidad = especialidad

    def imprimir_datos(self):
        print(f"Estudiante Avanzado: {self.nombre}, Edad: {self.edad}, Nivel Académico: {self.nivel_academico}, Especialidad: {self.especialidad}")


class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def imprimir_datos(self):
        print(f"Asignatura: {self.nombre}, Creditos: {self.creditos}")


class Calificacion:
    def __init__(self, estudiante, materia, nota):
        self.estudiante = estudiante
        self.materia = materia
        self.nota = nota

    def imprimir_datos(self):
        print(f"Calificación de {self.estudiante.nombre} en {self.materia.nombre}: {self.nota}")


estudiante1 = EstudianteRegular("Juan", 18, "Bachillerato")
estudiante2 = EstudianteAvanzado("Maria", 22, "Licenciatura", "Ingeniería en sistemas")


materia1 = Materia("Matemáticas", 3)
materia2 = Materia("Quimica", 2)


calificacion1 = Calificacion(estudiante1, materia1, 85)
calificacion2 = Calificacion(estudiante2, materia2, 90)


estudiante1.imprimir_datos()
calificacion1.imprimir_datos()
print()
estudiante2.imprimir_datos()
calificacion2.imprimir_datos()