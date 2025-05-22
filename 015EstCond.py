#El usuario ingresará un numero correspondiente al dia de la semana y el programa imprimira el nombre de ese dia
nombre= input('Escribe tu nombre: ')
dia=int(input('Escribe el numero de dia que vendras a trabajar: '))
# = asignacion == comparacion
if(dia==1):
    print(f'{nombre} felicidades vendras a trabajar el dia Lunes')
elif(dia==2):
    print(f'{nombre} felicidades vendras a trabajar el dia Martes')    
elif(dia==3):
    print(f'{nombre} felicidades vendras a trabajar el dia Miercoles')  
elif(dia==4):
    print(f'{nombre} felicidades vendras a trabajar el dia Jueves')  
elif(dia==5):
    print(f'{nombre} felicidades vendras a trabajar el dia Viernes') 
elif(dia==6):
    print(f'{nombre} felicidades vendras a trabajar el dia Sabado')  
elif(dia==7):
    print(f'{nombre} felicidades vendras a trabajar el dia Domingo')   
else:
    print(f'{nombre} lo sentimos ese dia laboral no existe..')
