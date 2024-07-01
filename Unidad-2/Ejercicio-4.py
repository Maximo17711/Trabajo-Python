class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre]

    def actualizar_tarea(self, nombre, nueva_descripcion):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.descripcion = nueva_descripcion

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(f"Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}")

# Ejemplo de uso 
lista = ListaTareas()
tarea1 = Tarea("Estudiar", "Estudiar para el examen de matemáticas")
tarea2 = Tarea("Hacer ejercicio", "Hacer 30 minutos de ejercicio")

lista.agregar_tarea(tarea1)
lista.agregar_tarea(tarea2)
lista.mostrar_tareas()
lista.actualizar_tarea("Estudiar", "Estudiar para el examen de historia")
lista.eliminar_tarea("Hacer ejercicio")
lista.mostrar_tareas()
