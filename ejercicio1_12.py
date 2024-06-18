'''Define una clase abstracta llamada Empleado que tenga métodos abstractos
como calcular_sueldo() y generar_reporte(). Luego, crea clases concretas
como Desarrollador, Gerente, Contador, etc., que hereden de Empleado y
proporcionen implementaciones concretas para estos métodos.'''


from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario_base = salario

    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, horas_ext, valor_hora_ex):
        super().__init__(nombre, salario)
        self.horas_extra = horas_ext
        self.valor_hora_extra = valor_hora_ex

    def calcular_sueldo(self):
        return self.salario_base + (self.horas_extra * self.valor_hora_extra)

    def generar_reporte(self):
        sueldo = self.calcular_sueldo()
        print(f'Desarrollador: {self.nombre}, Sueldo: ${sueldo:.2f}')


class Gerente(Empleado):
    def __init__(self, nombre, salario, productividad):
        super().__init__(nombre, salario)
        self.salario = salario
        self.productividad = productividad

    def calcular_sueldo(self):
        return self.salario + self.productividad

    def generar_reporte(self):
        sueldo = self.calcular_sueldo()
        print(f'Gerente: {self.nombre}, Sueldo: ${sueldo:.2f}')

class Contador(Empleado):
    def __init__(self, nombre, salario, trabajos_realizados):
        super().__init__(nombre, salario)
        self.trabajos_realizados = trabajos_realizados

    def calcular_sueldo(self):
        return self.salario_base + self.trabajos_realizados

    def generar_reporte(self):
        sueldo = self.calcular_sueldo()
        print(f'Contador: {self.nombre}, Sueldo: ${sueldo:.2f}')

# Ejemplo 
desarrollador1 = Desarrollador("Matias", 20000, 120, 65)
gerente1 = Gerente("Leonardo", 22000, 2000)
contador1 = Contador("Charlie", 17500, 400)

desarrollador1.generar_reporte()
gerente1.generar_reporte()
contador1.generar_reporte()
