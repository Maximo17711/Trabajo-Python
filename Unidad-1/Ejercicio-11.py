from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

    def moverse(self):
        return "El perro está corriendo"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

    def moverse(self):
        return "El gato está saltando"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío"

    def moverse(self):
        return "El pájaro está volando"

# Ejemplo de uso
perro = Perro()
gato = Gato()
pajaro = Pajaro()

print(perro.hacer_sonido())
print(perro.moverse())
print(gato.hacer_sonido())
print(gato.moverse())
print(pajaro.hacer_sonido())
print(pajaro.moverse())
