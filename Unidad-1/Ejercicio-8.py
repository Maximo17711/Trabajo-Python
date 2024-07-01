class Figura:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Ejemplo de uso
triangulo1 = Triangulo(10, 5, 10, 8, 8)
print("Área del triángulo:", triangulo1.calcular_area())
print("Perímetro del triángulo:", triangulo1.calcular_perimetro())

cuadrado1 = Cuadrado(4)
print("Área del cuadrado:", cuadrado1.calcular_area())
print("Perímetro del cuadrado:", cuadrado1.calcular_perimetro())
