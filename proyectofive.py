import os
from readchar import readkey, key
from pydantic import BaseModel
import random

class Juego:
    def __init__(self, path_mapas):
        self.path_mapas = path_mapas
        self.mapa = ""
        self.posicion_inicial = (0, 0)
        self.posicion_final = (0, 0)
        self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos = os.listdir(self.path_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.path_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()
            self.mapa, coordenadas = self.obtener_mapa_y_coordenadas(contenido)
            self.posicion_inicial, self.posicion_final = self.obtener_coordenadas(coordenadas)

    def obtener_mapa_y_coordenadas(self, contenido):
        lineas = contenido.strip().split('\n')
        coordenadas = lineas[0]
        mapa = [list(fila) for fila in lineas[1:]]
        return mapa, coordenadas

    def obtener_coordenadas(self, coordenadas):
        try:
            # Separar las coordenadas en dos partes
            coords_partes = coordenadas.split(',')
            inicial = tuple(map(int, coords_partes[:2]))
            final = tuple(map(int, coords_partes[2:]))
            return inicial, final
        except ValueError:
            raise ValueError("Formato de coordenadas incorrecto: {}".format(coordenadas))

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
            print(''.join(fila))

    def main_loop(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:
            self.mapa[py][px] = "P"
            self.mostrar_mapa()

            # Leer la tecla presionada
            tecla = readkey()

            # Restaurar la posición anterior antes de verificar si la nueva posición es válida
            self.mapa[py][px] = "."

            # Calcular la nueva posición tentativa
            nueva_px, nueva_py = px, py

            if tecla == key.UP and py > 0 and self.mapa[py - 1][px] != '#':
                nueva_py -= 1  # Flecha arriba
            elif tecla == key.DOWN and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                nueva_py += 1  # Flecha abajo
            elif tecla == key.LEFT and px > 0 and self.mapa[py][px - 1] != '#':
                nueva_px -= 1  # Flecha izquierda
            elif tecla == key.RIGHT and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                nueva_px += 1  # Flecha derecha

            # Verificar si la nueva posición es válida
            if 0 <= nueva_px < len(self.mapa[0]) and 0 <= nueva_py < len(self.mapa) and self.mapa[nueva_py][nueva_px] != "#":
                # Actualizar la posición y restaurar la posición anterior
                px, py = nueva_px, nueva_py
            else:
                continue

        print("¡Ganaste!")

if __name__ == "_main_":
    # Reemplaza 'path_a_tus_mapas' con la ruta correcta a tu carpeta de mapas
    juego = Juego(path_mapas="Depsys-pc\\Desktop\\Protalento\\ProyectoIntegrador\\proyecto_integrador_ada\\mapas")
    juego.main_loop()