#El programa imprimirá un saludo de una forma particular

import time
print ('Imprimiremos la cadena de texto !Hola Mundo¡, usando el ciclo for')

for letra in '!Hola Mundo¡':
    time.sleep(1)
    print(letra, end="", flush=True)
    #print(letra, end=' ')