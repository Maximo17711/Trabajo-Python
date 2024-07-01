class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_descuento(self):
        pass

class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def calcular_precio_descuento(self):
        return self.precio * (1 - self.descuento / 100)

class ProductoNormal(Producto):
    def calcular_precio_descuento(self):
        return self.precio

# Ejemplo de uso
producto_descuento = ProductoDescuento("Televisor", 1000, 10)
producto_normal = ProductoNormal("Silla", 100)

print("Precio con descuento del televisor:", producto_descuento.calcular_precio_descuento())
print("Precio normal de la silla:", producto_normal.calcular_precio_descuento())
