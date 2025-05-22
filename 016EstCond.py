#El programa pedira una cantidad en pesos mexicanos y mostrara un menu de opciones para convertir a dolares o soles peruanos

pesos=float(input('Ingresa la cantidad en pesos mexicanos: '))
opcion= int(input('\nElige a cual moneda deseas convertir: '
                  '\n1. Dolares $17'
                  '\n2. Soles S/.4\n'))

mensaje1='La cantidad convertida en dolares americanos es: '
mensaje2='La cantidad convertidad en soles peruanos es: '
ancho=80 #80 letras en el espacio donde se va a centrar'

if (opcion==1):
    total=pesos/17
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,round(total,3))
elif(opcion==2):
    total=pesos/4.61
   # mensaje2=mensaje2.center(ancho)
    print(mensaje2,round(total,3))
else:
    print('Elegiste una opcion ivalida..')