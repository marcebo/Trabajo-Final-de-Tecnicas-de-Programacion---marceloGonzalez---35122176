'''Crea una clase Producto con un método calcular_precio_descuento(). Luego,
crea clases derivadas como ProductoDescuento, ProductoNormal, etc., que
implementen este método de manera diferente.'''

class Producto:
    def __init__(self, nombre, precio):
       self.nombre = nombre
       self.precio = precio
    
    def calcular_precio_descuento(self):
        raise NotImplementedError

class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def calcular_precio_descuento(self):
        return self.precio * (1 - self.descuento/100)

class ProductoNormal(Producto):
    def calcular_precio_descuento(self):
        return self.precio
    
# Ejemplo
producto_desc = ProductoDescuento('Auto', 10000, 25)
precio_con_descuento = producto_desc.calcular_precio_descuento()
print(f'Precio con descuento de {producto_desc.nombre}: ${precio_con_descuento:.2f}')
