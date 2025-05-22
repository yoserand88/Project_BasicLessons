#El programa manipula un arreglo bidimensional, tambien llamado matriz
#o lista de listas

#Crearemos la matriz
matriz=[[1,2,3],
      [4,5,6],
      [7,8,9]]

#como accedemos a un determinado elemento de una matriz:
elemento=matriz[1][2]
print('El elemento que esta en la fila 1, columna 2 es: ', elemento)
print ('\n Ahora recorreremos la estructura:')
for fila in matriz:
      for elemento in fila:
            print(elemento, end=' ')
      print()