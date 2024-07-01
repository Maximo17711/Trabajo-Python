class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Edificio:
    def __init__(self, tipo, direccion):
        self.tipo = tipo
        self.direccion = direccion

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Ciudad:
    def __init__(self):
        self.ciudadanos = []
        self.edificios = []
        self.vehiculos = []

    def agregar_ciudadano(self, ciudadano):
        self.ciudadanos.append(ciudadano)

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_ciudad(self):
        print("Ciudadanos:")
        for ciudadano in self.ciudadanos:
            print(f"Nombre: {ciudadano.nombre}, Edad: {ciudadano.edad}")
        print("Edificios:")
        for edificio in self.edificios:
            print(f"Tipo: {edificio.tipo}, Dirección: {edificio.direccion}")
        print("Vehículos:")
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}")

# Ejemplo de uso
ciudad = Ciudad()
ciudadano1 = Ciudadano("Alice", 30)
ciudadano2 = Ciudadano("Bob", 45)
edificio1 = Edificio("Residencial", "123 Calle Falsa")
edificio2 = Edificio("Comercial", "456 Avenida Siempreviva")
vehiculo1 = Vehiculo("Toyota", "Corolla")
vehiculo2 = Vehiculo("Honda", "Civic")

ciudad.agregar_ciudadano(ciudadano1)
ciudad.agregar_ciudadano(ciudadano2)
ciudad.agregar_edificio(edificio1)
ciudad.agregar_edificio(edificio2)
ciudad.agregar_vehiculo(vehiculo1)
ciudad.agregar_vehiculo(vehiculo2)
ciudad.mostrar_ciudad()
