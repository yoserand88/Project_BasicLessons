#Crearemos una clase que manipula información de vehiculos
#Usaremos un método para imprimir su ficha tecnica

class Vehiculo:
    def __init__(self,marca,tipo,modelo,color):
        self.marca=marca
        self.tipo=tipo
        self.color=color
        self.modelo=modelo
    def ficha_tecnica(self): #metodo
        print('\n------FICHA TECNICA DEL VEHICULO------\n')
        print('La marca del vehiculo es:', self.marca)
        print('El tipo del vehiculo es:', self.tipo)
        print('El modelo del vehiculo es:', self.modelo)
        print('El color del vehiculo es:', self.color)  

#el programa comienza aqui
#crearemos nuestro primer objetipo de clase Vehiculo
vehiculo1=Vehiculo('KIA','Picanto','2016','Negro')
#Invocaremos el metodo ficha tecnica del objeto vehiculo
vehiculo1.ficha_tecnica()
#El usuario construirá su objeto, con datos desde el teclado
marca=input('Escribe la marca del vehiculo: ')
tipo=input('Escribe el tipo del vehiculo: ')
modelo=input('Escribe el modelo del vehiculo: ')
color=input('Escribe el color del vehiculo: ')
Vehiculo_Usuario=Vehiculo('marca','tipo','modelo','modelo')
Vehiculo_Usuario.ficha_tecnica()
