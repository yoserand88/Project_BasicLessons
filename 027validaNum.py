#Este programa valida para que solo se introduzcan numeros

while True: #do -while
    try:
        datos=input('Por favor ingresa tu edad: ')
        edad= int(datos)
        if(edad<0) or (edad>110):
            print('La edad NO es valida')
        else:
            break
    except ValueError:
        print('Error al capturar, por favor ingresa un dato numerico.')
print ('Edad valida: ',edad)