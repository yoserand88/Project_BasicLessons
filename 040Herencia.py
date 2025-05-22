#Mostraremos como se comporta la herencia en python
#Crearemos la super clase , clase base o clase Padre
#Herencia 1)Elimina la redundancia 2)Realizar modificaciones rapida y flexible 3) Permite optimizar la construccion de codigo 

class Animal:
    def __init__(self,nombre):
        self.Nombre=nombre
            
    def Comer(self):
        print(f'{self.Nombre} esta comiendo')
        
#Crearemos la sub clase, clase derivada o clase hija
class Perro(Animal): #Aqui hay herencia
    def __init__(self,nombre,raza):
        super().__init__(nombre)
        self.raza=raza
    
    def Ladrar(self):
        print(f'{self.Nombre} es de la raza {self.raza} y esta ladrando')
        
print('Crearemos el objeto miPerro, de clase Perro\n'
      'que hereda atributos de la super clase Animal\n'
      'su nombre es Doki y su raza es Yorkshire\n')
miPerro=Perro('Doki','Yorkshire')
miPerro.Comer() #Este metodo es de la Super Clase
miPerro.Ladrar() #Este metodo es de la sub Clase