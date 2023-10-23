
from Modulos.Funciones import cargar_grafo_pesos, cargar_archivo_peso_minimo, mostrarRuta, dijkstra, dijkstra_cuello, warshall_lista
from Modulos.Grafo import Grafo

# Se inicializa el grafo que nos interesa
grafo_peso = Grafo()
cargar_grafo_pesos("rutas.txt", grafo_peso)

# Se inicializa el grafo de costo mínimo
grafo_costo = Grafo()
peso_minimo = 0  # Esto se puede modificar según cada caso particular
cargar_archivo_peso_minimo("rutas.txt", grafo_costo, peso_minimo)

# Se corre el algoritmo de Dijkstra modificado para peso máximo
dijkstra_cuello(grafo_peso, grafo_peso.obtenerVertice("CiudadBs.As."))

# Se corre el algoritmo de Dijkstra para costo mínimo
dijkstra(grafo_costo, grafo_costo.obtenerVertice("CiudadBs.As."))

# Se aplica el algoritmo de Warshall para averiguar qué vértices son alcanzables desde CiudadBs.As.
vertices = warshall_lista(grafo_peso, "CiudadBs.As.")

# Se comunica el resultado, detallando la ruta para llegar a cada vértice
# junto con el peso máximo y el costo mínimo.
for vertice in vertices:
    if vertice != "CiudadBs.As.":
        print(f"Para llegar desde CiudadBs.As. hasta {vertice}:")

        # Ruta de peso máximo
        ruta_peso_maximo = mostrarRuta(grafo_peso.obtenerVertice("CiudadBs.As."), grafo_peso.obtenerVertice(vertice), grafo_peso)
        peso_maximo = grafo_peso.obtenerVertice(vertice).obtenerDistancia()
        print(f"Ruta de peso máximo: {ruta_peso_maximo}")
        print(f"Peso máximo: {peso_maximo}")

        # Verificar si el vértice está presente en el grafo de costo mínimo
        if grafo_costo.obtenerVertice(vertice) is not None:
            # Ruta de costo mínimo
            costo_minimo_vertice = grafo_costo.obtenerVertice(vertice)
            if costo_minimo_vertice._predecesor is not None:
                ruta_costo_minimo = mostrarRuta(grafo_costo.obtenerVertice("CiudadBs.As."), costo_minimo_vertice, grafo_costo)
                costo_minimo = costo_minimo_vertice.obtenerDistancia()
                print(f"Ruta de costo mínimo: {ruta_costo_minimo}")
                print(f"Costo mínimo: {costo_minimo}")
            else:
                print("Costo mínimo no disponible debido al peso mínimo configurado.")
        else:
            print("Costo mínimo no disponible debido al peso mínimo configurado.")

        print("------------------------------------------------------------------------------------------------------------------------------")
