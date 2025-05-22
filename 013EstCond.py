#El programa determinara si el usuario podras votar o no, evaluando su edad
#Entrada de Datos
nombre=input('Escribe tu nombre: ')
edad=int(input('Escribe tu edad: '))

#Procesamiento de Datos
if (edad >=18): #estructura selectiva if
    print(nombre, 'Si puedes votar')
    print('Hasta luego')
else:
    print(nombre,'No puedes votar')
    print('Hasta luego')