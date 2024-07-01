class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = {}

    def agregar_calificacion(self, asignatura, calificacion):
        self.calificaciones[asignatura] = calificacion

    def mostrar_calificaciones(self):
        for asignatura, calificacion in self.calificaciones.items():
            print(f"Asignatura: {asignatura}, Calificación: {calificacion}")

class Profesor:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

class Calificacion:
    def __init__(self, estudiante, asignatura, nota):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.nota = nota

    def mostrar_calificacion(self):
        print(f"Estudiante: {self.estudiante.nombre}, Asignatura: {self.asignatura.nombre}, Nota: {self.nota}")

class EstudianteRegular(Estudiante):
    pass

class EstudianteAvanzado(Estudiante):
    pass

# Ejemplo de uso
profesor = Profesor("Sr. Pérez", "Matemáticas")
asignatura = Asignatura("Matemáticas", profesor)
estudiante = EstudianteRegular("Juan", 15)
calificacion = Calificacion(estudiante, asignatura, 8)
estudiante.agregar_calificacion(asignatura.nombre, calificacion.nota)
estudiante.mostrar_calificaciones()
