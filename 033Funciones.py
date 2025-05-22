#Una funcion es un segmento de codigo que se puede reutilizar
#El programa calculara el area de un circulo usando una función

import math

#este es el codigo de la función, radio es el metodo
def calcular_Area_circulo(radio):
    area=math.pi*radio**2
    return area

#este es el codigo del programa, primero se ejecutará este codigo
radio=float (input('Escribe el radio del circulo y calculare su área: '))

#llamaremos a la función
areaCir=calcular_Area_circulo(radio)
print('El area del circulo es: ', round (areaCir,2))