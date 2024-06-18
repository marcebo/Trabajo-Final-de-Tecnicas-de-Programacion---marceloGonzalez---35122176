'''Crea una clase Cancion que tenga atributos como nombre, artista y duracion.
Crea métodos para reproducir la canción y para mostrar sus detalles.'''

class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def reproducir_cancion(self):
        print(f'Reproduciendo: {self.nombre} de {self.artista}')

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Artista: {self.artista}')
        print(f'Duracion: {self.duracion} mins')


# Ejemplo:
cancion1 = Cancion('El pibe de los astilleros', 'Patricio Rey y sus redonditos de ricota',3.32)
cancion1.reproducir_cancion()
cancion1.mostrar_informacion()