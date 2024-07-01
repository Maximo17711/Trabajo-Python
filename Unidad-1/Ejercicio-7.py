class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")

# Ejemplo de uso
coche1 = Coche("Toyota", "Corolla", "Rojo", 4)
coche1.mostrar_informacion()

moto1 = Moto("Honda", "CBR", "Negra", 600)
moto1.mostrar_informacion()
