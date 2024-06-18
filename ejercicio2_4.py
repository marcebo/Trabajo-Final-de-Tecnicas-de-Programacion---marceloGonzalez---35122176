'''Crea un sistema de gestión de tareas que permita a los usuarios agregar,
eliminar y actualizar tareas. Debe haber clases como Tarea, ListaTareas, etc. '''

class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_detalles(self):
        print(f"Tarea: {self.nombre} ({self.estado}) - {self.descripcion}")


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_todas_las_tareas(self):
        for tarea in self.tareas:
            tarea.mostrar_detalles()


#Ejem
lista = ListaTareas()

tarea1 = Tarea("Enviar mail", "Hacer diagrama")
tarea2 = Tarea("Llamar a Jose", "Enviar documentación")

lista.agregar_tarea(tarea1)
lista.agregar_tarea(tarea2)

lista.mostrar_todas_las_tareas()
