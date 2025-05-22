#Crearemos una funcion para determinar si el numero es par o impar

def es_par(num): #lleve o no lleva parametros va :
    if num%2==0:
        return True
    else:
        return False   
#inicia el programa  ten cuidado con los espacios puede saltarte error al compilar
while True: #para que vuelva a preguntar por el numero
    numero=int(input('Escribe un numero y determinare si es par o impar:'
                     '\n presione 0 para salir: '))
    if numero==0:
         break
    if es_par(numero): # si al invocar es_par me devuelve True
        print(f'El numero {numero} es par')
    else: #en caso contrario es impar
        print(f'El numero {numero} es impar')

   # 3%2=1 (porque tiene decimales)
   # 2%2=0 (porque no tiene decimales)'''


edad= 25    #variable publica todo bien
_miEdad=45  #variable privada cuidado al manipular
__tuEdad=25 #variable protegida precaci{on extrema al manejarla}