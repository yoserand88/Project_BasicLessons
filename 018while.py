#Simularemos el conteo regresivo del despegue de un cohete
import time #clase para manipular el tiempo de mi programa
contador=10
print ('Inicia el conteo regresivo...')
while contador>0:
    print(contador)
    time.sleep(1) #dormiremos el programa 1 segundo
    contador-=1  #contador=contador-1
print('El cohete ha despegado con exito...')