'''Crea una clase Usuario con atributos como nombre, email y contraseña.
Crea métodos para cambiar la contraseña y para mostrar la información del
usuario.'''

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def cambiar_contra(self, contra_nueva):
        self.contraseña = contra_nueva
        print("Se ha modificado tu contraseña")

    def informacion_usuario(self):
        print(f"nombre: {self.nombre}")
        print(f"email: {self.email}")
        print(f"contraseña: {self.contraseña}")

# Ejemplo

usuario1 = Usuario("Jose", "josesito@gmail.com", "0303")
usuario1.informacion_usuario() 

usuario1.cambiar_contra(4787)
usuario1.informacion_usuario()