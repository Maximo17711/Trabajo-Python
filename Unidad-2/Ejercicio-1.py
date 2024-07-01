class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, cantidad):
        self.cantidad_disponible = cantidad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad disponible: {self.cantidad_disponible}"

# Ejemplo de uso
producto = Producto("Laptop", 1500, 10)
print(producto.mostrar_informacion())
producto.actualizar_cantidad(7)
print(producto.mostrar_informacion())
