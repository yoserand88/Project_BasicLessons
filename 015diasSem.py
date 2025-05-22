#El usuario indicará el número de día y se imprimirá el nombre de ese día
nombre= input ('Escribe tu nombre: ')
dia=int(input('Escribe el numero de día que vendras a trabajar: '))
# = asignación
# == comparación

if (dia==1):
    print(nombre, 'Vendras a trabajar le dia lunes')
elif (dia==2):
    print(nombre, 'Vendras a trabajar le dia martes')
elif (dia==3):
    print(nombre, 'Vendras a trabajar le dia miercoles')
elif (dia==4):
    print(nombre, 'Vendras a trabajar le dia jueves')
elif (dia==5):
    print(nombre, 'Vendras a trabajar le dia viernes')
elif (dia==6):
    print(nombre, 'Vendras a trabajar le dia sabado')
elif (dia==7):
    print(nombre, 'Vendras a trabajar le dia domingo')
else:
    print(nombre, 'ese dia no existe')