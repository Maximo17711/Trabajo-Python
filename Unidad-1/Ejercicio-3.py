class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

    def cambiar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

# Ejemplo de uso
usuario1 = Usuario("Ana", "ana@example.com", "1234")
usuario1.mostrar_informacion()
usuario1.cambiar_contrasena("abcd")
usuario1.mostrar_informacion()
