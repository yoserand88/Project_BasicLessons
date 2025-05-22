#Crearemos la clase persona (molde)

class Persona: #Definimos la clase, Self te ahorra codigo duplicado
    def __init__(self,nombre,edad,apellido):   #Iniciamos el constructor de la clase, esta protegido doble guion bajo atributos, publica son los metodos    
        self.nombre=nombre  #Asignamos un valor a un atributo de la clase, Esta es el atributo=variable
        self.edad=edad      #OJO lado izquierdo atributo, derecho esta la variable de la clase
        
    def Saludar(self):  #Iniciamos la construccion de un Método
        print(f'Hola, mi nombre es==> {self.nombre} y mi edad ==>{self.edad}')
        
#Crearemos los objetos de la clase persona
persona1=Persona('Mario',25)  #Construimos un objeto del tipo clase Persona
persona2=Persona('Ana',31)
print ('Se construyeron 2 objetos, persona1 y persona2\n')
#Accederemos a un atributo de un objeto
print('El nombre de la persona1 es:',persona1.nombre)
print ('La Edad de la persona1 es:',persona1.edad)
print(f'\nEl nombre de la persona2 es-->{persona2.nombre}'
      f' la edad de la persona2 es-->{persona2.edad}' )
#Accederemos a los metodos o funciones de cada objeto
persona1.Saludar() #Accedemos a un metodo de un objeto
persona2.Saludar()