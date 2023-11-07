import os
import msvcrt

def convertir_mapa(laberinto):
    #primero Dividimos el laberinto por filas 
    rows = laberinto.split("\n")
    matriz = [list(row) for row in rows]
    return matriz

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def principal(mapa, p_inicial, p_final):
    px, py = p_inicial
    while (px, py) != p_final:
        mapa[py][px] = "P"
        mostrar_laberinto(mapa)
        
        # Leer la tecla pulsada
        key = msvcrt.getch().decode('utf-8')
        
        # Calcular la nueva posición
        nueva_px, nueva_py = px, py
        if key == "w":
            nueva_py -= 1
        elif key == "s":
            nueva_py += 1
        elif key == "a":
            nueva_px -= 1
        elif key == "d":
            nueva_px += 1
        
        # Verificar si posición es válida
        if 0 <= nueva_px < len(mapa[0]) and 0 <= nueva_py < len(mapa) and mapa[nueva_py][nueva_px] != "#":
            # Actualizar la posición y restaurar la posición anterior
            mapa[py][px] = "."
            px, py = nueva_px, nueva_py
        else:
            continue

def mostrar_laberinto(mapa):
    limpiar_terminal()
    for row in mapa:
        print("".join(row))

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

principal(mapa, posicion_inicial, posicion_final)