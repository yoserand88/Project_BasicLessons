#el programa manipula una lista con numeros y los ordena usando el 
#metodo de la burbuja   

datos=[50,300,55, 157,5,18]
print('La lista original es: ', datos)
n=len(datos)
print('La longitud de la estructura es: ',n)
for i in range(n-1): # i=0,1
    for j in range(n-1): #j=0,1,2,3,4 =
        print(f'i vale:{i} y j vale: {j}')
        if(datos[j]>datos[j+1]):
            datos[j],datos[j+1]=datos[j+1],datos[j]
            print('Actualmente la lista es: ',datos)
print('\nLa lista ordenada es: \n', datos)

#LIFO (Last in First Out; el ultimo en entrar primero en salir) PILAS
#FIFO (First in First Out; primero en entrar primero en salir) COLAS