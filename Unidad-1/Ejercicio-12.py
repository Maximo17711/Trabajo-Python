from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass

class Desarrollador(Empleado):
    def calcular_sueldo(self):
        return "El sueldo del desarrollador es $5000"

    def generar_reporte(self):
        return "Reporte del desarrollador"

class Gerente(Empleado):
    def calcular_sueldo(self):
        return "El sueldo del gerente es $7000"

    def generar_reporte(self):
        return "Reporte del gerente"

class Contador(Empleado):
    def calcular_sueldo(self):
        return "El sueldo del contador es $4000"

    def generar_reporte(self):
        return "Reporte del contador"

# Ejemplo de uso
desarrollador = Desarrollador()
gerente = Gerente()
contador = Contador()

print(desarrollador.calcular_sueldo())
print(desarrollador.generar_reporte())
print(gerente.calcular_sueldo())
print(gerente.generar_reporte())
print(contador.calcular_sueldo())
print(contador.generar_reporte())
