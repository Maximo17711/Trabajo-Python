class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        for producto in self.productos:
            print(producto.mostrar_informacion())

# Ejemplo de uso
carrito = CarritoCompra()
producto1 = Producto("Laptop", 1000)
producto2 = Producto("Mouse", 50)

carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.mostrar_carrito()
