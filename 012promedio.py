#El programa calcula y muestra el promedio de 3 calificacione de un alumno

print ('El programa calcula el promedio de 3 calificaciones del alumnno\n')
nombre=input('Escribe tu nombre Alumno:  ')
mat=float(input('Escribe tu calificación de matematicas: '))
fis=float(input('Escribe tu calificacion de fisica: '))
quim=float(input('Escribe tu calificacion de quimica: '))

'''
prioridad de operadores
exponenciacion ** y () en primer lugar
* y /                  en segundo lugar
+ y -                  en tercer lugar

'''

#procesamiento de datos
prom=(mat+fis+quim)/3

if(prom>=6):
    print(f'{nombre} tu promedio es: {round(prom,3)}, Felicidades, APROBADO')
else:    
     print(f'{nombre} tu promedio es: {round(prom,3)}, JALASTE')

'la f es para imprimir varibles dentro de la comillas junto con texto'