class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} está maullando")

# Ejemplo de uso
perro1 = Perro("Fido", 3, "Labrador")
perro1.mostrar_informacion()
perro1.ladrar()

gato1 = Gato("Misu", 2, "Blanco")
gato1.mostrar_informacion()
gato1.maullar()
