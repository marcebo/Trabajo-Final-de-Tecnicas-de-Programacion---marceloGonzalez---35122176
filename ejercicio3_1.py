'''Diseña e implementa un sistema completo de gestión de eventos en línea que
permita a los usuarios crear, buscar, registrarse y administrar eventos. Los
eventos pueden ser conferencias, conciertos, reuniones, etc. El sistema debe
incluir funcionalidades avanzadas como recomendación de eventos, gestión
de pagos, notificaciones en tiempo real, etc.'''


from datetime import datetime

class Evento:
    def __init__(self, nombre, fecha_inicio, fecha_fin, lugar):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.lugar = lugar

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de inicio: {self.fecha_inicio}")
        print(f"Fecha de fin: {self.fecha_fin}")
        print(f"Lugar: {self.lugar}")


class Conferencia(Evento):
    def __init__(self, nombre, fecha_inicio, fecha_fin, lugar, presentador):
        super().__init__(nombre, fecha_inicio, fecha_fin, lugar)
        self.presentador = presentador

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Presentador: {self.presentador}")


class Concierto(Evento):
    def __init__(self, nombre, fecha_inicio, fecha_fin, lugar, artistas):
        super().__init__(nombre, fecha_inicio, fecha_fin, lugar)
        self.artistas = artistas

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Artistas: {', '.join(self.artistas)}")


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class SistemaEventos:
    def __init__(self):
        self.eventos = []
        self.usuarios = []

    def crear_evento(self, evento):
        self.eventos.append(evento)

    def buscar_evento(self, nombre):
        for evento in self.eventos:
            if evento.nombre.lower() == nombre.lower():
                return evento
        return None

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def recomendar_eventos(self, usuario):
        eventos_recomentados = [e for e in self.eventos if e.fecha_inicio > datetime.now() and e not in usuario.asistidos]
        if eventos_recomentados:
            return eventos_recomentados[0]
        else:
            return None

    def pagar_entrada(self, usuario, evento):
        print(f"Se ha pagado la entrada para {usuario.nombre} para el evento {evento}")

    def enviar_notificacion(self, usuario, evento):
        print(f"Se ha enviado una notificación a {usuario.email} para el evento {evento}")


sistema_eventos = SistemaEventos()

conferencia1 = Conferencia("Conferencia 1", datetime(2023, 3, 1), datetime(2023, 3, 2), "Ciudad Universitaria", "Profesor X")
concierto1 = Concierto("Concierto 1", datetime(2023, 4, 15), datetime(2023, 4, 15), "Estadio", ["Artista A", "Artista B"])

usuario1 = Usuario("Pipo", "pipo@gmail.com")
usuario2 = Usuario("Mariana", "mariana@gmail.com")

sistema_eventos.crear_evento(conferencia1)
sistema_eventos.crear_evento(concierto1)
sistema_eventos.registrar_usuario(usuario1)
sistema_eventos.registrar_usuario(usuario2)

evento_recomendado = sistema_eventos.recomendar_eventos(usuario1)
if evento_recomendado:
    evento_recomendado.imprimir_datos()
else:
    print("No hay eventos recomendados")


sistema_eventos.pagar_ticket(usuario1, evento_recomendado)
sistema_eventos.enviar_notificacion(usuario1, evento_recomendado)