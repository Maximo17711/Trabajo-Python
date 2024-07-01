class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguaje_programacion):
        super().__init__(nombre, salario, departamento)
        self.lenguaje_programacion = lenguaje_programacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje de programación: {self.lenguaje_programacion}")

class Diseñador(Empleado):
    def __init__(self, nombre, salario, departamento, herramienta_diseno):
        super().__init__(nombre, salario, departamento)
        self.herramienta_diseno = herramienta_diseno

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Herramienta de diseño: {self.herramienta_diseno}")

# Ejemplo de uso
desarrollador1 = Desarrollador("Carlos", 50000, "Desarrollo", "Python")
desarrollador1.mostrar_informacion()

diseñador1 = Diseñador("Laura", 45000, "Diseño", "Photoshop")
diseñador1.mostrar_informacion()
