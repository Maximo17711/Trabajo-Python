class Evento:
    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.eventos = []

    def registrar_evento(self, evento):
        self.eventos.append(evento)

class SistemaEventos:
    def __init__(self):
        self.eventos = []
        self.usuarios = []

    def crear_evento(self, nombre, fecha, lugar):
        evento = Evento(nombre, fecha, lugar)
        self.eventos.append(evento)
        return evento

    def registrar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        return usuario

# Ejemplo de uso
sistema = SistemaEventos()
evento1 = sistema.crear_evento("Conferencia Python", "2024-07-10", "Buenos Aires")
usuario1 = sistema.registrar_usuario("Ana García", "ana@example.com")
usuario1.registrar_evento(evento1)
