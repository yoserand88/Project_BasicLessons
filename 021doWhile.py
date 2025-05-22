#El programa pedira numeros para promediarlos
contador=0
suma=0
numero=0

#el do -- while no existe en python se implementa con un while True

while True:
    numero=float(input('Escribe un número para sumarlo (ingresa 0 para salir)'))
    if(numero==0):
        break
    suma+=numero #suma=suma+numero
    contador+=1 #contador=contador+1
#salimos del ciclo
if(contador>0):
    promedio=suma/contador
    print('La suma de los numeros es: ',suma)
    print('El total de numeros introducidos por el usuario es:', contador)
    print('El promedio de los numeros ingresados es:', promedio)
else:
    print('No se ingresaron numeros validos...')