from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        return "El coche está acelerando"

    def frenar(self):
        return "El coche está frenando"

class Moto(Vehiculo):
    def acelerar(self):
        return "La moto está acelerando"

    def frenar(self):
        return "La moto está frenando"

class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta está acelerando"

    def frenar(self):
        return "La bicicleta está frenando"

# Ejemplo de uso
coche = Coche()
moto = Moto()
bicicleta = Bicicleta()

print(coche.acelerar())
print(coche.frenar())
print(moto.acelerar())
print(moto.frenar())
print(bicicleta.acelerar())
print(bicicleta.frenar())
