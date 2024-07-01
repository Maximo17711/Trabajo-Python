class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad disponible: {self.cantidad_disponible}")

# Ejemplo de uso
producto1 = Producto("Laptop", 1000, 50)
producto1.mostrar_informacion()
producto1.actualizar_cantidad(45)
producto1.mostrar_informacion()
