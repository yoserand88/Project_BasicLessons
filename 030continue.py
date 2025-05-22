#ejemplificaremos el uso de continue
#el programa solamente imprimirá el valor de la variable , cuando esta tome un valor impar.

for i in range (1,11):
    if i%2==0:
        print('Impresion omitida por ser numero par...')
        continue
    print(f'La variable i, vale:{i}')