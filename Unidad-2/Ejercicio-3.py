class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, cantidad):
        self.cantidad_disponible = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def actualizar_existencias(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.actualizar_cantidad(cantidad)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad disponible: {producto.cantidad_disponible}")

# Ejemplo de uso
inventario = Inventario()
producto1 = Producto("PC", 1250, 10)
producto2 = Producto("Mouse", 20, 50)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.mostrar_inventario()
inventario.actualizar_existencias("PC", 7)
inventario.mostrar_inventario()
