#El programa pedira numeros mientras los ingresados esten entre el 0 y 99

edad=0

while True:   #implementación del do -- while de otros lenguajes
    edad=int(input('Escribe tu edad: '))
    if(edad>0) and (edad<99):
        break
    print('Edad no válida, intenta de nuevo por favor...')
print ('Tu edad es: ',edad)