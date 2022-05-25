class FiguraGeometrica():
    tipo = 'Indeterminado1'
    def  __init__(self, color):
        self.set_color(color)
        
    def area(self):
        pass

    def perimetro(self):
        pass

    def set_color(self, color):
        self.color = color
        self.primario = self.color in ('amarillo', 'rojo', 'azul')

    def get_color(self):
        return self.color

    def get_tipo(self):
        return self.tipo

    def get_primario(self):
        return self.primario

class Cuadrado(FiguraGeometrica):
    tipo = 'Cuadrado'
    def __init__(self, color, lado):
       
        FiguraGeometrica.__init__(self, color)
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4    

# Invocaciones generales
c = Cuadrado('rojo', 10)
c = Cuadrado('rojo', 10)
c = Cuadrado('rojo', 10)
print(c.get_color())
print(c.get_tipo())
print(c.get_primario())
c.set_color('rosa')
print(c.get_primario())
print(c.perimetro())
print(Cuadrado.tipo)

f = FiguraGeometrica('verde')
print(f.get_color())