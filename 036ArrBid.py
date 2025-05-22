#Crearemos una lista de listas que llamaremos desde el teclado

filas=3
columna=3
matriz=[[5]*columna for _ in range(filas)]

for i in range(filas):
    for j in range (columna):
        dato=input('Ingresa el dato en la posicion ({},{})'.format(i,j))
        matriz[i][j]=dato

print('\n los datos de la matriz son: ')
for fila in matriz:
    print(fila)

#imprimiremos la diagonal principal
print('Impriremos la diagonal principal')
for i in range(3):
    for j in range(3):
        if i==j:
            print(matriz[i][j])
            
#Imprimiremos la diagonal principal en orden inverso
print('Impriremos la diagonal principal en orden inverso')
for filas in range (2,-1,-1):
    for columnas in range (2,-1,-1):
        if filas==columnas:
            print(matriz[filas][columnas])