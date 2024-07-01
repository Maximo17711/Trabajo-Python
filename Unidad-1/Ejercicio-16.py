class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, grado):
        super().__init__(nombre)
        self.grado = grado

    def mostrar_informacion(self):
        return f"Estudiante: {self.nombre}, Grado: {self.grado}"

class Profesor(Persona):
    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

    def mostrar_informacion(self):
        return f"Profesor: {self.nombre}, Asignatura: {self.asignatura}"

class Aula:
    def __init__(self, profesor):
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_aula(self):
        print(self.profesor.mostrar_informacion())
        for estudiante in self.estudiantes:
            print(estudiante.mostrar_informacion())

# Ejemplo de uso
profesor = Profesor("Dr. Smith", "Matemáticas")
aula = Aula(profesor)
estudiante1 = Estudiante("Alice", "10mo")
estudiante2 = Estudiante("Bob", "10mo")

aula.agregar_estudiante(estudiante1)
aula.agregar_estudiante(estudiante2)
aula.mostrar_aula()
