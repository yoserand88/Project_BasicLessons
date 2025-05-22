#Convetiremos de metros a kilómetros y a centimetros según lo solicite el usuario

distencia=float(input('Escribe la cantidad en metros: '))
opcion= input('\n ¿A cual unidad los quieres convertir?'
              '\n a convertir a kilometors'
              '\n b convertir a centimetros')

'''if (opcion=='a'): se coloca comillas porque es no se ha declarado como entero "int"'''

if (opcion=='a'):
    total=distencia/1000
    print('La cantidad convertidad a kilometros es: ',total)
elif(opcion=='b'):
    total=distencia*100
    print('La cantidad convertidad a centimetros es: ',total)
else:
    print('Opcion no valida...')