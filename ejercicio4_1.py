'''Desarrolla un programa en Python que permita gestionar las calificaciones de
estudiantes en una institución educativa. El sistema debe permitir el registro
de profesores, alumnos, asignaturas y calificaciones, así como calcular
automáticamente el promedio y determinar la promoción de cada estudiante.
El sistema debe incluir las siguientes funcionalidades:
Registro de profesores: El sistema debe permitir el registro de profesores,
incluyendo su nombre y la asignatura que imparten.
Registro de alumnos: El sistema debe permitir el registro de alumnos,
incluyendo su nombre y el curso al que pertenecen.
Registro de asignaturas: El sistema debe permitir el registro de asignaturas,
incluyendo su nombre.
Registro de calificaciones: El sistema debe permitir el registro de
calificaciones de los alumnos en las diferentes asignaturas. Cada calificación
debe incluir el nombre del alumno, la asignatura, el profesor que la imparte y
la calificación obtenida.
Cálculo del promedio: El sistema debe calcular automáticamente el promedio
de calificaciones de cada alumno.
Determinación de la Promoción: El sistema debe determinar
automáticamente si un alumno está promocionado o no, en función de su
promedio de calificaciones. '''


class Profesor:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

class Alumno:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = {}

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

class Nota:
    def __init__(self, alumno, materia, profesor, nota):
        self.alumno = alumno
        self.materia = materia
        self.profesor = profesor
        self.nota = nota

class SistemaDeNotas:
    def __init__(self):
        self.profesores = {}
        self.alumnos = {}
        self.materias = {}

    def registrar_profesor(self, nombre, materia):
        self.profesores[nombre] = Profesor(nombre, materia)
        print(f'Profesor {nombre} registrado.')

    def registrar_alumno(self, nombre, curso):
        self.alumnos[nombre] = Alumno(nombre, curso)
        print(f'Alumno {nombre} registrado.')

    def registrar_materia(self, nombre):
        self.materias[nombre] = Asignatura(nombre)
        print(f'Asignatura {nombre} registrada.')

    def registrar_nota(self, nombre_alumno, nombre_materia, nombre_profesor, nota):
        alumno = self.alumnos[nombre_alumno]
        if nombre_materia not in alumno.notas:
            alumno.notas[nombre_materia] = []
        alumno.notas[nombre_materia].append(nota)
        print(f'Nota de {nota} registrada para {nombre_alumno} en {nombre_materia} dictada por {nombre_profesor}.')

    def calcular_promedio_nota(self, nombre_alumno):
        alumno = self.alumnos[nombre_alumno]
        total_notas = sum(sum(notas) for notas in alumno.notas.values())
        cantidad_notas = sum(len(notas) for notas in alumno.notas.values())
        return total_notas / cantidad_notas

    def es_aprobado(self, nombre_alumno):
        promedio_nota = self.calcular_promedio_nota(nombre_alumno)
        return promedio_nota >= 6.0

    def mostrar_promedios_y_promocion(self):
        for nombre_alumno in self.alumnos:
            promedio = self.calcular_promedio_nota(nombre_alumno)
            promocionado = 'Sí' if self.es_aprobado(nombre_alumno) else 'No'
            print(f'Alumno: {nombre_alumno}, Promedio: {promedio:.2f}, Promocionado: {promocionado}')

#ejem
sistema = SistemaDeNotas()

sistema.registrar_profesor('Pablo', 'Matemática')
sistema.registrar_profesor('Matias Gomez', 'Lengua')
sistema.registrar_alumno('Jose Perez', 'Primero')
sistema.registrar_alumno('Facundo', 'Segundo')
sistema.registrar_materia('Matemática')
sistema.registrar_materia('Lengua')

sistema.registrar_nota('Jose Perez', 'Matemática', 'Pablo', 9.5)
sistema.registrar_nota('Facundo', 'Lengua', 'Matias Gomez', 8.0)
sistema.registrar_nota('Maria', 'Lengua', 'Matias Gomez', 6.0)

sistema.mostrar_promedios_y_promocion()
