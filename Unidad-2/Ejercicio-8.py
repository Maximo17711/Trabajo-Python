class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        for producto in self.productos:
            print(f"Producto: {producto.nombre}, Precio: {producto.precio}")

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Pedido:
    def __init__(self, usuario, carrito):
        self.usuario = usuario
        self.carrito = carrito

    def mostrar_pedido(self):
        print(f"Usuario: {self.usuario.nombre}, Email: {self.usuario.email}")
        self.carrito.mostrar_carrito()

class Cliente(Usuario):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.direccion = direccion

class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

# Ejemplo de uso
producto1 = Producto("Laptop", 1500)
producto2 = Producto("Mouse", 20)
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
cliente = Cliente("Alice", "alice@example.com", "123 Calle Falsa")
pedido = Pedido(cliente, carrito)
pedido.mostrar_pedido()
