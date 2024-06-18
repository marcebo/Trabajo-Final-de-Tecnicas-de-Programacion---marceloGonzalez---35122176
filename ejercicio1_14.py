'''Define una clase Playlist que tenga una lista de canciones. Usa composición
para representar la relación entre una lista de reproducción y las canciones
que la componen.'''

class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f'{cancion.titulo} agregada a la playlist')

    def mostrar_canciones(self):
        print(f"Canciones '{self.nombre}':")
        for cancion in self.canciones:
            print(f"- {cancion.titulo} ({cancion.artista})")

# Ejemplo
cancion1 = Cancion('El perro', 'El mató a un policía motorizado')
cancion2 = Cancion('Diganselo', 'El Kuelgue')
cancion3 = Cancion('La sal no sala', 'Charly García')

mi_playlist = Playlist("Mis favoritas")
mi_playlist.agregar_cancion(cancion1)
mi_playlist.agregar_cancion(cancion2)
mi_playlist.agregar_cancion(cancion3)

mi_playlist.mostrar_canciones()

