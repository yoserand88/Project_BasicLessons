#CRUD
#Crearemos un programa que nos permita manipular iuna lista realizando las operaciones basicas
#CRUD => Sistema Transaccional => CRM => ERP

import os #nos permite usar instrucciones de nuestro S.O
import time
lista=[]
while True:
    print ('---MENU PRINCIPAL---'
           '\n1. Insertar un dato.' 
           '\n2. Eliminar un dato.' 
           '\n3. Buscar un dato.' 
           '\n4. Sobreescribir un dato.' 
           '\n5. Mostrar el contenido de la lista.' 
           '\n6. Salir.' 
           )
    opcion=int(input ('Elige una opción: '))
    if(opcion==1): #Create (Insertar)
        dato=input('Ingresar el nombre a insertar: ')
        lista.append(dato) # append es un temodo que permite agregar a una lista el dato que esta entre los parentesis.
        print ('Dato insertado correctamente...')
        time.sleep(2) #Para que no se vaya tan rapido el mensaje lo detiene 2 segundos
        os.system('cls') #limpie la pantalla y vuelve a pintar el menu
    elif(opcion==2): #Delete (Eliminar)
            dato=input('Ingresar el dato a eliminar: ')
            if (dato in lista):
                lista.remove(dato)
                print('Dato eliminado correctamente...')    
                time.sleep(2) 
                os.system('cls') 
            else:
                print('El dato a elimi1nar no esta en la lista...')
                time.sleep(2) 
                os.system('cls') 
    elif(opcion==3):
        dato=input('Ingresar el nombre a buscar: ')
        if(dato in lista):
            print('El nombre existe en la lista, esta en la posición:', lista.index(dato)) #index muestra la posición de un dato  
            time.sleep(2) 
            os.system('cls')       
        else: #si no se encuentra
                print('El dato a elimi1nar no esta en la lista...')
                time.sleep(2) 
                os.system('cls')         
    elif(opcion==4): #Udpate
        datoAnterior=input('Ingresa el nombre a sobreescribir: ')
        if(datoAnterior in lista):
                indice=lista.index(datoAnterior)
                datoNuevo=input('Ingresa el nuevo dato: ')
                lista[indice]=datoNuevo
                print ('El dato se sobreescribio correctamente: ' '')
                time.sleep(2) 
                os.system('cls')        
        else: #si no se encuentra
            print(f'El nombre: {datoAnterior}no existe en la lista...')
            time.sleep(2) 
            os.system('cls')    
    elif(opcion==5): #Read
        print('El contenido de la lista es: ')
        print(lista)
        time.sleep(2) 
        os.system('cls')
    elif(opcion==6): #Salid
        respuesta=input('Estas seguro? (s/n): ')
        if(respuesta.upper()=='S'):
           print('Saliendo del sistema...')
           time.sleep(2)
           os.system('cls')
           break
        time.sleep(2)
        os.system('cls')    
    else:
        print('opcion no valida, intenta nuevamente')
        time.sleep(2)
        os.system('cls')