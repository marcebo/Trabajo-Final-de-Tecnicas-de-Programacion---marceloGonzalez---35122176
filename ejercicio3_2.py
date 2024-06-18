'''Desarrolla un sistema de recomendación de películas que sugiera películas a
los usuarios en función de sus gustos previos y las calificaciones de otras
películas. Utiliza algoritmos de filtrado colaborativo o sistemas de
recomendación basados en contenido para generar recomendaciones
personalizadas para cada usuario. Considera también la implementación de
funciones avanzadas como la detección de tendencias, la recomendación de
grupos y la retroalimentación del usuario. '''

class Pelicula:
    def __init__(self, titulo, genero, director, año):
        self.titulo = titulo
        self.genero = genero
        self.director = director
        self.año = año

class Usuario:
    def __init__(self, nombre, apellidos, email, gustos_previos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.gustos_previos = gustos_previos

class SistemaRecomendacion:
    def __init__(self):
        self.peliculas = []
        self.usuarios = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def calcular_similitud(self, usuario1, usuario2):
        similaridad = 0
        for gusto1 in usuario1.gustos_previos:
            for gusto2 in usuario2.gustos_previos:
                if gusto1 == gusto2:
                    similaridad += 1
        return similaridad / len(usuario1.gustos_previos)

    def generar_recomendaciones(self, usuario_id):    
        usuario = self.usuarios[usuario_id]
        gustos_previos = usuario.gustos_previos
        similarities = []
        for i in range(len(self.usuarios)):
            if i != usuario_id:
                similarity = self.calcular_similitud(usuario, self.usuarios[i])
                similarities.append((i, similarity))
        similar_users = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]
        recommended_movies = []
        for user_id, similarity in similar_users:
            for pelicula in [pelicula for pelicula in self.peliculas if pelicula.genero in [gusto for gusto in self.usuarios[user_id].gustos_previos]]:
                if pelicula not in recommended_movies:
                    recommended_movies.append(pelicula.titulo)

        return recommended_movies


sistema_recomendacion = SistemaRecomendacion()

sistema_recomendacion.agregar_pelicula(Pelicula("El caballero oscur", "Acción", "Christopher Nolan", 2008))
sistema_recomendacion.agregar_pelicula(Pelicula("Cadena Perpetua", "Drama", "Frank Darabont", 1994))
sistema_recomendacion.agregar_pelicula(Pelicula("El padrino", "Acción", "Francis Ford Coppola", 1972))

sistema_recomendacion.agregar_usuario(Usuario("Tito", "Gomez", "tito12@gmail.com", ["Acción", "Comedia", "Dramático"]))
sistema_recomendacion.agregar_usuario(Usuario("Lola", "Smith", "lolas@gmail.com", ["Thriller", "Drama", "Romántico"]))


user_id = 0
recommended_movies = sistema_recomendacion.generar_recomendaciones(user_id)
print("Recomendaciones para el usuario", user_id)
print(recommended_movies)