from MonticuloBinarioMax import MonticuloBinarioMax
from MonticuloBinarioMin import MonticuloBinarioMin

def leer_archivo_grafo(nombre_archivo, grafo_peso, grafo_costo):
    # Lee un archivo de texto que contiene información sobre aristas de un grafo y carga los datos en dos grafos diferentes:
    # uno que representa el grafo basado en los pesos de las aristas y otro basado en los costos de las aristas.
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_peso.agregarArista(inicio, destino, peso)
            grafo_costo.agregarArista(inicio, destino, costo)

def cargar_grafo_pesos(nombre_archivo, grafo_peso):
    # Carga datos de un archivo de texto en un grafo basado en los pesos de las aristas.
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_peso.agregarArista(inicio, destino, peso)

def cargar_archivo_peso_minimo(nombre_archivo, grafo_costo, peso_minimo):
    # Carga datos de un archivo de texto en un grafo basado en los costos de las aristas, pero solo agrega las aristas
    # cuyo peso sea igual o mayor al peso mínimo especificado.
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_costo.agregarVertice(inicio)
            grafo_costo.agregarVertice(destino)
            if int(peso) >= int(peso_minimo):
                grafo_costo.agregarArista(inicio, destino, costo)

def mostrarRuta(vertice_inicio, vertice_fin, grafo):
    # Retorna una cadena de caracteres que representa la ruta desde el vértice de inicio hasta el vértice de destino en el grafo.
    ruta = ""
    recorrido = []
    vertice_actual = vertice_fin
    recorrido.append(vertice_actual)
    while vertice_actual is not vertice_inicio:
        recorrido.insert(0, vertice_actual._predecesor)
        vertice_actual = vertice_actual._predecesor
    for vertice in recorrido:
        ruta += str(vertice.Id) + ' -> '
    ruta = ruta[:-4]
    return ruta

def dijkstra(unGrafo, inicio):
    # Algoritmo de Dijkstra para encontrar el camino más barato desde un vértice de inicio hasta todos los demás vértices en un grafo.
    cp = MonticuloBinarioMin()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1]
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente, nuevaDistancia)

def dijkstra_cuello(unGrafo, inicio):
    # Algoritmo de Dijkstra para encontrar el camino de cuello de botella desde un vértice de inicio hasta todos los demás vértices en un grafo.
    cp = MonticuloBinarioMax()

    for v in unGrafo:
        v.asignarDistancia(0)
    inicio.asignarDistancia(float(1))
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()[1]

        for verticeSiguiente in verticeActual.obtenerConexiones():
            ponderacion = verticeActual.obtenerPonderacion(verticeSiguiente)
            if verticeSiguiente.estado == "no visitado":
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.estado = "visitado"
                if verticeActual == inicio:
                    verticeSiguiente._distancia = ponderacion
                    cp.incrementarClave(verticeSiguiente, ponderacion)
                else:
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    verticeSiguiente._distancia = min(verticeActual._distancia, ponderacion)
                    cp.incrementarClave(verticeSiguiente, verticeSiguiente._distancia)
            elif (verticeSiguiente.estado == "visitado" and verticeActual._distancia > verticeSiguiente._distancia and verticeSiguiente._distancia < ponderacion):
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente._distancia = min(verticeActual._distancia, ponderacion)

def warshall(grafo, inicio, fin):
    # Implementa el algoritmo de Warshall para determinar si hay un camino entre dos vértices en un grafo.
    mapeo_nodos = {}
    indice = 0
    for nodo in grafo.obtenerVertices():
        mapeo_nodos[nodo] = indice
        indice += 1

    n = len(grafo.obtenerVertices())
    distancias = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for nodo in grafo.obtenerVertices():
        for vecino in grafo.obtenerVertice(nodo).conexiones:
            i = mapeo_nodos[nodo]
            j = mapeo_nodos[vecino.Id]
            distancias[i][j] = 1 

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias[mapeo_nodos[inicio]][mapeo_nodos[fin]] != float('inf')

def warshall_lista(grafo, inicio):
    # Implementa el algoritmo de Warshall para determinar los nodos alcanzables desde un vértice de inicio en un grafo.
    mapeo_nodos = {}
    indice = 0
    for nodo in grafo.obtenerVertices():
        mapeo_nodos[nodo] = indice
        indice += 1

    n = len(grafo.obtenerVertices())
    distancias = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for nodo in grafo.obtenerVertices():
        for vecino in grafo.obtenerVertice(nodo).conexiones:
            i = mapeo_nodos[nodo]
            j = mapeo_nodos[vecino.Id]
            distancias[i][j] = 1  

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    nodos_alcanzables = []
    indice_inicio = mapeo_nodos[inicio]
    for i, distancia in enumerate(distancias[indice_inicio]):
        if distancia != float('inf'):
            nodos_alcanzables.append(list(mapeo_nodos.keys())[list(mapeo_nodos.values()).index(i)])

    return nodos_alcanzables

