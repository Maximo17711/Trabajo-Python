def reproducir(medio):
    medio.reproducir()

class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

    def reproducir(self):
        print(f"Reproduciendo la canción {self.nombre} por {self.artista}")

class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def reproducir(self):
        print(f"Reproduciendo la película {self.titulo} dirigida por {self.director}")

# Ejemplo de uso
cancion = Cancion("Imagine", "John Lennon")
pelicula = Pelicula("Inception", "Christopher Nolan")

reproducir(cancion)
reproducir(pelicula)
