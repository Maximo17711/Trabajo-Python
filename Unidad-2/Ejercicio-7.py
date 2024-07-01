class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def publicar(self, mensaje):
        self.publicaciones.append(mensaje)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print("Amigos:")
        for amigo in self.amigos:
            print(f"- {amigo.nombre}")
        print("Publicaciones:")
        for publicacion in self.publicaciones:
            print(f"- {publicacion}")

# Ejemplo de uso
usuario1 = Usuario("Alice")
usuario2 = Usuario("Bob")
usuario1.agregar_amigo(usuario2)
usuario1.publicar("Hola, este es mi primer mensaje!")
usuario1.mostrar_informacion()
