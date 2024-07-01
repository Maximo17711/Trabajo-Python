class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Artista: {self.artista}"

class Playlist:
    def __init__(self):
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def mostrar_playlist(self):
        for cancion in self.canciones:
            print(cancion.mostrar_informacion())

# Ejemplo de uso
playlist = Playlist()
cancion1 = Cancion("Imagine", "John Lennon")
cancion2 = Cancion("Bohemian Rhapsody", "Queen")

playlist.agregar_cancion(cancion1)
playlist.agregar_cancion(cancion2)
playlist.mostrar_playlist()
