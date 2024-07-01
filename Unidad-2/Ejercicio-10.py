class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad

class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

class Ruta:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

class Conductor:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

class Cliente:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

class GestionTransporte:
    def __init__(self):
        self.vehiculos = []
        self.rutas = []
        self.conductores = []
        self.clientes = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

# Ejemplo de uso
transporte = GestionTransporte()
vehiculo1 = Automovil("Toyota", "Corolla", 5)
vehiculo2 = Camion("Mercedes", "Actros", 10000)
ruta1 = Ruta("Buenos Aires", "Córdoba")
conductor1 = Conductor("Juan Pérez", "B12345")
cliente1 = Cliente("Carlos López", "Córdoba")

transporte.agregar_vehiculo(vehiculo1)
transporte.agregar_vehiculo(vehiculo2)
transporte.agregar_ruta(ruta1)
transporte.agregar_conductor(conductor1)
transporte.agregar_cliente(cliente1)
