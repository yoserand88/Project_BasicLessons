#Crearemos una clase Triángulo con un método para calcular su área
class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def Area(self):
        return (self.base*self.altura)/2

#pediremos los datos necesarios para crear objetos de la clase Triangulo
base=float(input('Escribe la base del triangulo en CM: '))
altura=float(input('Ahora escribe la altura del triangulo en CM: '))       

#Construiremos el objeto
triangulo=Triangulo(base,altura)
#invocaremos el metodo para calcular el area del triangulo
print('El area del triangulo en CM es: ', triangulo.Area())
