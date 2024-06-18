'''Crea un simulador de una red social donde los usuarios puedan registrarse,
agregar amigos, publicar mensajes, etc. Debe haber clases como Usuario,
Publicación, Comentario, etc. '''


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, usuario):
        self.amigos.append(usuario)

    def publicar(self, texto):
        publicacion = Publicacion(texto, self)
        self.publicaciones.append(publicacion)

    def mostrar_publicaciones(self):
        for publicacion in self.publicaciones:
            print(publicacion)


class Publicacion:
    def __init__(self, texto, usuario):
        self.texto = texto
        self.usuario = usuario
        self.comentarios = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def mostrar_comentarios(self):
        for comentario in self.comentarios:
            print(comentario)


class Comentario:
    def __init__(self, texto, publicacion):
        self.texto = texto
        self.publicacion = publicacion


class RedSocial:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.nombre)



red_social = RedSocial()

usuario1 = Usuario("Juan", "juan@gmail.com")
usuario2 = Usuario("Maria", "maria@gmail.com")
usuario3 = Usuario("Pedro", "pedro@gmail.com")

red_social.agregar_usuario(usuario1)
red_social.agregar_usuario(usuario2)
red_social.agregar_usuario(usuario3)

usuario1.agregar_amigo(usuario2)
usuario2.agregar_amigo(usuario3)


usuario1.publicar("¿Que onda")
usuario2.publicar("Wepa")

publicacion1 = usuario1.publicaciones[0]
publicacion1.agregar_comentario(Comentario("Buenas", publicacion1))
publicacion2 = usuario2.publicaciones[0]
publicacion2.agregar_comentario(Comentario("Hola Juan!", publicacion2))

print("Publicaciones de Juan:")
usuario1.mostrar_publicaciones()
print("Comentarios de la publicación 1 de Juan:")
publicacion1.mostrar_comentarios()
print("Publicaciones de Maria:")
usuario2.mostrar_publicaciones()
print("Comentarios de la publicación 1 de Maria:")
publicacion2.mostrar_comentarios()

