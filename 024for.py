#El programa lee un arreglo de numeros y se detiene la cantidad de
#segundos que indica la posicion leida
#arreglo (guarda datos de un solo tipo) y lista (guarda datos de varios tipos)
import time
for i in [1,2,5,3,2,6,1]:
    print(f'habra un retraso de {i} segundos')
    time.sleep(i)