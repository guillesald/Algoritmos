import sys
import os
# Esto lo hice porque no encontraba los modulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modulos')))

# Esto lo hice porque no encontraba el archivo
os.chdir('C:\\Users\\guill\\OneDrive\\Escritorio\\Algoritmos\\TPs\\TP2\\Problema 3')

from Modulos.Funciones import cargar_grafo_pesos, cargar_archivo_peso_minimo, mostrarRuta, dijkstra, dijkstra_cuello
from Modulos.Grafo import Grafo


# Se inicializa el grafo que nos interesa
grafo_peso = Grafo()
cargar_grafo_pesos("rutas.txt", grafo_peso)

# Se inicializa el grafo de costo mínimo
grafo_costo = Grafo()


# Se corre el algoritmo de Dijkstra modificado para peso máximo
dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice("CiudadBs.As."))


# Comunicar el resultado, detallando la ruta para llegar a cada vértice junto con el peso máximo y el costo mínimo.
for vertice in grafo_peso.obtenerVertices():
    if vertice != "CiudadBs.As.":
        vertice_actual = grafo_peso.obtenerVertice(vertice)
        if vertice_actual.obtenerDistancia() > 0:
            print(f"Para llegar desde CiudadBs.As. hasta {vertice}:")
            # Ruta de peso máximo
            ruta_peso_maximo = mostrarRuta(grafo_peso.obtenerVertice("CiudadBs.As."), vertice_actual, grafo_peso)
            peso_maximo = vertice_actual.obtenerDistancia()
            print(f"Ruta de peso máximo: {ruta_peso_maximo}")
            print(f"Peso máximo: {peso_maximo}")
            cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_maximo)
            # Se corre el algoritmo de Dijkstra para costo mínimo
            dijkstra(grafo_costo, grafo_costo.obtenerVertice("CiudadBs.As."))
            # Verificar si el vértice está presente en el grafo de costo mínimo
            if grafo_costo.obtenerVertice(vertice) is not None:
                # Ruta de costo mínimo
                costo_minimo_vertice = grafo_costo.obtenerVertice(vertice)
                if costo_minimo_vertice.obtenerDistancia() < float('inf'):
                    ruta_costo_minimo = mostrarRuta(grafo_costo.obtenerVertice("CiudadBs.As."), costo_minimo_vertice, grafo_costo)
                    costo_minimo = costo_minimo_vertice.obtenerDistancia()
                    print(f"Ruta de costo mínimo: {ruta_costo_minimo}")
                    print(f"Costo mínimo: {costo_minimo}")

            print("------------------------------------------------------------------------------------------------------------------------------")
        else:
            print(f"No hay ruta disponible desde CiudadBs.As. hasta {vertice}.")
            print("------------------------------------------------------------------------------------------------------------------------------")
