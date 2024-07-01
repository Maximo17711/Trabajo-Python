class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def obtener_promedio_calificaciones(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas_vistas = {}

    def calificar_pelicula(self, pelicula, calificacion):
        pelicula.agregar_calificacion(calificacion)
        self.peliculas_vistas[pelicula.titulo] = calificacion

    def recomendar_peliculas(self, peliculas):
        recomendaciones = []
        for pelicula in peliculas:
            if pelicula.titulo not in self.peliculas_vistas:
                recomendaciones.append((pelicula.titulo, pelicula.obtener_promedio_calificaciones()))
        recomendaciones.sort(key=lambda x: x[1], reverse=True)
        return [titulo for titulo, _ in recomendaciones]

# Ejemplo de uso
pelicula1 = Pelicula("Pelicula A", "Acción")
pelicula2 = Pelicula("Pelicula B", "Comedia")
usuario1 = Usuario("Carlos")

usuario1.calificar_pelicula(pelicula1, 5)
usuario1.calificar_pelicula(pelicula2, 4)

pelicula3 = Pelicula("Pelicula C", "Drama")
pelicula4 = Pelicula("Pelicula D", "Acción")

peliculas = [pelicula1, pelicula2, pelicula3, pelicula4]
recomendaciones = usuario1.recomendar_peliculas(peliculas)
print(recomendaciones)
