class Ser:
    def __init__(self, energia, salud, edad):
        self.energia = energia
        self.salud = salud
        self.edad = edad

class Planta(Ser):
    def fotosintesis(self):
        self.energia += 10

class Animal(Ser):
    def comer(self):
        self.energia += 20

class Persona(Ser):
    def trabajar(self):
        self.energia -= 15
        self.salud -= 5

# Ejemplo de uso
planta = Planta(50, 80, 1)
animal = Animal(70, 90, 3)
persona = Persona(60, 100, 25)

planta.fotosintesis()
animal.comer()
persona.trabajar()

print(f"Planta - Energía: {planta.energia}, Salud: {planta.salud}, Edad: {planta.edad}")
print(f"Animal - Energía: {animal.energia}, Salud: {animal.salud}, Edad: {animal.edad}")
print(f"Persona - Energía: {persona.energia}, Salud: {persona.salud}, Edad: {persona.edad}")
