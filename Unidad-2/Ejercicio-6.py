class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

class SalaCine:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.asientos_reservados = 0

    def reservar_asiento(self):
        if self.asientos_reservados < self.capacidad:
            self.asientos_reservados += 1
            return True
        else:
            return False

class Reserva:
    def __init__(self, pelicula, sala):
        self.pelicula = pelicula
        self.sala = sala

    def realizar_reserva(self):
        if self.sala.reservar_asiento():
            print(f"Reserva realizada para la película {self.pelicula.titulo} en la sala {self.sala.numero}")
        else:
            print("No hay asientos disponibles")

# Ejemplo de uso
pelicula = Pelicula("Avengers", 180)
sala = SalaCine(1, 100)
reserva = Reserva(pelicula, sala)

for _ in range(101):
    reserva.realizar_reserva()
