#El programa contiene un número secreto que el usuario debe adivinar
#tendra 3 oportunidades
numero_secreto=9
adivinado=False #
intentos=0
quedan=3 #nro de intentos

print('Solo tienes 3 intentos')
while not(adivinado) and (intentos<3):   #while (adivinado==false) mientras adivinado no sea true y intentos sea menor que 3
    dato=int(input('Adivina el numero (Es menor que 10): '))
    if(dato==numero_secreto):
        print('Felicitaciones has adivinado el numero...')
        adivinado=True
    else:  #Si no lo adivino
        intentos+=1
        if( 
              
              3): #Si intentos ya llego a 3
            print('El juego ha terminado...')
        else: #en caso todavia no llegue a 3
            print('intenta de nuevo por favor...')
            quedan-=1
            print(f'Te quedan {quedan} intentos')

