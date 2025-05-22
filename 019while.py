#Estructuras repetitivas = ciclos
#while--> Se usa cuando quiza ni una vez se entre al ciclo
#do - while (while True)--> Se usa cuando al menos 1 vez se debe ejecutar el ciclo
#For--> Cuando se inicia la ejecución, casi siempre ya sabemos cuantas veces se va a repetir este ciclo


#El programa pedira numeros y los ira sumando en una variable que tecnicamente se le conoce como acumulador

SUMA=0
numero=1

while numero!=0: #Mientras numero NO sea= a cero
    numero=int(input('iNGRESA UN NUMERO PARA SUMARLO, (INGRESA 0 PARA SALIR)'))
    SUMA+=numero #suma=suma+numero
print('La suma de los numeros introducidos es: ',SUMA)