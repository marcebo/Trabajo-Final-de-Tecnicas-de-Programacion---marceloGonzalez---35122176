'''Crea una clase Empleado con atributos como nombre, salario y
departamento. Crea clases derivadas como Desarrollador, Diseñador, etc.,
que añadan atributos y métodos propios de cada tipo de empleado.'''

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguaje):
        super().__init__(nombre, salario, departamento)
        self.lenguaje = lenguaje

    def desarrollar(self):
        print(f'{self.nombre} está haciendo la aplicación en {self.lenguaje}')


class Diseñador(Empleado):
    def __init__(self, nombre, salario, departamento, programas):
        super().__init__(nombre, salario, departamento)
        self.programas = programas

    def diseñar(self):
        print(f'{self.nombre} está diseñando en {self.programas}.')


#Ejemplo
desarrollador1 = Desarrollador('Jose', 1000, 'Tecnologia','python')
desarrollador1.desarrollar()    

diseñador1 = Diseñador('Coco', 1000, 'Diseño', 'Figma')
diseñador1.diseñar()