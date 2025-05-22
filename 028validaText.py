#este programa valida entradas de tipo texto.

while True:
    try:
        dato=input('Ingresa tu nombre de usuario:')
        nombre=int(dato)
        print ('Error por favor ingreso solo texto, no números.')
    except ValueError:
        break
print('Nombre de usuario valido: ',dato)