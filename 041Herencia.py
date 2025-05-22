#Crearemos la superclase figura, con un atributo, color y un metodo
#dibujar

class Figura:
    def __init__(self,color):
        self.Color=color
        
    def dibujar(self):
        print(f'Estamos dibujando una figura de color:{self.Color}')
        
#Crearemos una subclase llamada Rectangulo que hereda de figura
class Rectangulo(Figura):
    def __init__(self,color,ancho,alto):
        super().__init__(color) #el atributo viene de la super clase
        self.Ancho=ancho
        self.Alto=alto
        
    def Calcular_area(self):
        return self.Alto*self.Ancho
    
class Circulo(Figura):
    def __init__(self,color,radio):
        super().__init__(color) #el atributo viene de la super clase
        self.radio=radio
    
    def Calcular_area(self):
        return 3.1415*(self.radio**2)
    
#Construiremos los objetos
miRectangulo=Rectangulo('Azul',9,7)
MiCirculo=Circulo('Amarillo',14)
#Usaremos los metodos de la clase Rectangulo
miRectangulo.dibujar()
print('La figura es de tipo rectangulo')
print('El color de la figura es:', miRectangulo.Color)
print('El area del rectangulo es:', miRectangulo.Calcular_area())

MiCirculo.dibujar()
print('La figura es de tipo Circulo')
print('La color de la figura es:', MiCirculo.Color)
print('El area del Circulo es:', MiCirculo.Calcular_area())