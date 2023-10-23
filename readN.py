'''Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, 
borrar la terminal y e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido 
usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os
'''
import os
from readchar import readkey

#definimos la funcion para limpiar la terminal
def clean():
    os.system('cls' if os.name=='nt' else 'clear')


#definimos nuestra variable de tipo entero que almacenará el numero que va aumentando
number = 0

print("Presione la tecla 'n' para iniciar el conteo")

#realizamos el bucle
while True:
    key = readkey()

    if key == 'n':
        number += 1
        clean()
        print(f"Has presionado la tecla '{key}' {number} veces de 50 posibles, sigue así")

        if number == 50:
            clean()
            print(f"Felicitaciones, has presionado exitosamente la tecla 'n' {number} veces")
            break

    else:
        print(f"Has presionado la tecla {key} en lugar de 'n', intentalo de nuevo")        