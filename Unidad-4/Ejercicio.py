class Profesor:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

class Alumno:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.calificaciones = {}

    def agregar_calificacion(self, asignatura, calificacion):
        if asignatura not in self.calificaciones:
            self.calificaciones[asignatura] = []
        self.calificaciones[asignatura].append(calificacion)

    def obtener_promedio(self):
        total_calificaciones = 0
        cantidad_calificaciones = 0
        for calificaciones in self.calificaciones.values():
            total_calificaciones += sum(calificaciones)
            cantidad_calificaciones += len(calificaciones)
        return total_calificaciones / cantidad_calificaciones if cantidad_calificaciones > 0 else 0

    def esta_promocionado(self):
        return self.obtener_promedio() >= 6

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

class SistemaCalificaciones:
    def __init__(self):
        self.profesores = []
        self.alumnos = []
        self.asignaturas = []

    def registrar_profesor(self, nombre, asignatura):
        profesor = Profesor(nombre, asignatura)
        self.profesores.append(profesor)
        return profesor

    def registrar_alumno(self, nombre, curso):
        alumno = Alumno(nombre, curso)
        self.alumnos.append(alumno)
        return alumno

    def registrar_asignatura(self, nombre):
        asignatura = Asignatura(nombre)
        self.asignaturas.append(asignatura)
        return asignatura

# Ejemplo de uso
sistema = SistemaCalificaciones()
profesor1 = sistema.registrar_profesor("Sr. Pérez", "Matemáticas")
alumno1 = sistema.registrar_alumno("Juan Gómez", "1° A")
asignatura1 = sistema.registrar_asignatura("Matemáticas")

alumno1.agregar_calificacion("Matemáticas", 8)
alumno1.agregar_calificacion("Matemáticas", 7)

print(alumno1.obtener_promedio())
print(alumno1.esta_promocionado())
