#Crearemos la clase y el objeto normales para manipular
class Usuario:
    def __init__(self,id,alias,nombre,apellidos):
        self.id=id
        self.alias=alias
        self.nombre=nombre
        self.apellidos=apellidos
    
    def muestra_datos(self):
        print('El id del usuario es:',self.id)
        print('El alias del usuario es:',self.alias)
        print('El nombre del usuario es:',self.nombre)
        print('El apellido del usuario es:',self.apellidos)
    #Crearemos un objeto de esta clase y usaremos su metodo
  #user1=Usuario(1,'cristian.social','CHRISTIAN','ZAPATA')
  #user1.muestra_datos()