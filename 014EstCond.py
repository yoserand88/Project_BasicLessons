
#El programa evaluará la estatura de un usuario y si la estatura es menor a 160 imprimira "Eres baji
#Si la estatura es entre 160 y 175 cms imprimirá "Eres de talla maediana"
#Si la estatura es mayor a 175 cms imprimirá "Eres alto"
Nombre= input('Escribe tu nombre: ')
estatura=int (input('Escribe tu estatura en centimetros: '))

if (estatura<160):
    print(f'{Nombre}Eres bajit@')
elif (estatura>=160) and (estatura<=175):
    print(Nombre,'Eres de estatura mediana')
elif (estatura>175):
    print(Nombre,'Eres de estatura alta')