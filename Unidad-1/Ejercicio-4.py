class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo {self.nombre} por {self.artista}...")

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Artista: {self.artista}")
        print(f"Duración: {self.duracion} minutos")

# Ejemplo de uso
cancion1 = Cancion("Imagine", "John Lennon", 3.1)
cancion1.mostrar_detalles()
cancion1.reproducir()
