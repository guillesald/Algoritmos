from MonticuloBinarioMax import MonticuloBinarioMax
from MonticuloBinarioMin import MonticuloBinarioMin


def cargar_grafo_pesos(nombre_archivo, grafo_peso):
    """
    Carga datos de un archivo de texto en un grafo basado en los pesos de las aristas.
    """
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_peso.agregarArista(inicio, destino, peso)

def cargar_archivo_peso_minimo(nombre_archivo, grafo_costo, peso_minimo):
    """
    Carga datos de un archivo de texto en un grafo basado en los costos de las aristas, pero solo agrega las aristas
    cuyo peso sea igual o mayor al peso mínimo especificado.
    """
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            inicio, destino, peso, costo = linea.strip().split(',')
            grafo_costo.agregarVertice(inicio)
            grafo_costo.agregarVertice(destino)
            if int(peso) >= int(peso_minimo):
                grafo_costo.agregarArista(inicio, destino, costo)

def mostrarRuta(vertice_inicio, vertice_fin, grafo):
    """
    Retorna una cadena de caracteres que representa la ruta desde el vértice de inicio hasta el vértice de destino en el grafo.
    """
    ruta = ""
    recorrido = []
    vertice_actual = vertice_fin
    recorrido.append(vertice_actual)
    while vertice_actual is not vertice_inicio:
        recorrido.insert(0, vertice_actual.obtenerPredecesor())
        vertice_actual = vertice_actual.obtenerPredecesor()
    for vertice in recorrido:
        ruta += str(vertice.obtenerId()) + ' -> '
    ruta = ruta[:-4]
    return ruta

def dijkstra(unGrafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar el camino más barato desde un vértice de inicio hasta todos los demás vértices en un grafo.
    """
    # Paso 1: Inicialización de la cola de prioridad
    cp = MonticuloBinarioMin()
    
    # Paso 2: Asignar distancia cero al vértice de inicio y construir el montículo binario
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    
    # Paso 3: Bucle principal del algoritmo
    while not cp.estaVacia():
        # Paso 4: Extraer el vértice con la distancia mínima actual desde la cola de prioridad
        verticeActual = cp.eliminarMin()[1]
        
        # Paso 5: Iterar sobre los vecinos del vértice actual
        for verticeSiguiente in verticeActual.obtenerConexiones():
            # Paso 6: Calcular la nueva distancia tentativa hacia el vértice siguiente
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            
            # Paso 7: Actualizar la distancia y el predecesor si se encuentra un camino más corto
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                
                # Paso 8: Actualizar la clave en la cola de prioridad con la nueva distancia
                cp.decrementarClave(verticeSiguiente, nuevaDistancia)


def dijkstra_cuello(unGrafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar el camino de cuello de botella desde un vértice de inicio hasta todos los demás vértices en un grafo.
    """
    # Crear un montículo binario máximo para almacenar los vértices según sus distancias máximas.
    cp = MonticuloBinarioMax()

    # Inicializar las distancias de todos los vértices en el grafo.
    for v in unGrafo:
        v.asignarDistancia(0)
    
    # Inicializar la distancia del vértice de inicio con un valor muy alto (representa el máximo posible en el grafo).
    inicio.asignarDistancia(float('inf'))
    
    # Construir el montículo binario máximo con las distancias actuales de los vértices.
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

    # Procesar el montículo hasta que esté vacío.
    while not cp.estaVacia():
        # Obtener y eliminar el vértice con la máxima distancia del montículo.
        verticeActual = cp.eliminarMax()[1]

        # Iterar sobre los vértices adyacentes al vértice actual.
        for verticeSiguiente in verticeActual.obtenerConexiones():
            # Obtener el peso máximo de la arista entre verticeActual y verticeSiguiente.
            ponderacion = verticeActual.obtenerPonderacion(verticeSiguiente)
            
            # Si el vértice siguiente aún no ha sido visitado.
            if verticeSiguiente.estado == "no visitado":
                # Asignar verticeActual como predecesor de verticeSiguiente.
                verticeSiguiente.asignarPredecesor(verticeActual)
                # Marcar verticeSiguiente como visitado.
                verticeSiguiente.estado = "visitado"
                
                # Si verticeActual es el inicio, asignar la ponderación como la nueva distancia de verticeSiguiente.
                if verticeActual == inicio:
                    verticeSiguiente.asignarDistancia(ponderacion)
                    # Incrementar la clave en el montículo con la nueva distancia.
                    cp.incrementarClave(verticeSiguiente, ponderacion)
                else:
                    # Si no es el inicio, actualizar la distancia como el mínimo entre la distancia actual y la ponderación.
                    verticeSiguiente.asignarDistancia(min(verticeActual.obtenerDistancia(), ponderacion))
                    # Incrementar la clave en el montículo con la nueva distancia.
                    cp.incrementarClave(verticeSiguiente, verticeSiguiente.obtenerDistancia())
            
            # Si el vértice siguiente ya fue visitado y su distancia actual es menor que la ponderación actual.
            elif (verticeSiguiente.estado == "visitado" and
                  verticeActual.obtenerDistancia() > verticeSiguiente.obtenerDistancia() and
                  verticeSiguiente.obtenerDistancia() < ponderacion):
                # Actualizar el predecesor y la distancia de verticeSiguiente.
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(min(verticeActual.obtenerDistancia(), ponderacion))

# def dijkstra_cuello(unGrafo, inicio):
#     """
#     Algoritmo de Dijkstra para encontrar el camino de cuello de botella desde un vértice de inicio hasta todos los demás vértices en un grafo.
#     """
#     # Crear un montículo binario máximo para almacenar los vértices según sus distancias máximas.
#     cp = MonticuloBinarioMax()

#     # Inicializar las distancias de todos los vértices en el grafo.
#     for v in unGrafo:
#         v.asignarDistancia(0)
    
#     # Inicializar la distancia del vértice de inicio con un valor muy alto (representa el máximo posible en el grafo).
#     inicio.asignarDistancia(float('inf'))
    
#     # Construir el montículo binario máximo con las distancias actuales de los vértices.
#     cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

#     # Procesar el montículo hasta que esté vacío.
#     while not cp.estaVacia():
#         # Obtener y eliminar el vértice con la máxima distancia del montículo.
#         verticeActual = cp.eliminarMax()[1]

#         # Iterar sobre los vértices adyacentes al verticeActual.
#         for verticeSiguiente in verticeActual.obtenerConexiones():
#             # Obtener el peso de la arista entre verticeActual y verticeSiguiente.
#             ponderacion = verticeActual.obtenerPonderacion(verticeSiguiente)

#             # Calcular la nueva distancia como el mínimo entre la distancia actual del vértice y la ponderación.
#             nuevaDistancia = min(verticeActual.obtenerDistancia(), ponderacion)

#             # Si la nueva distancia es mayor que la distancia conocida, actualizarla.
#             if nuevaDistancia > verticeSiguiente.obtenerDistancia():
#                 verticeSiguiente.asignarDistancia(nuevaDistancia)
#                 verticeSiguiente.asignarPredecesor(verticeActual)
#                 cp.incrementarClave(verticeSiguiente, nuevaDistancia)


# def warshall_lista(grafo, inicio):
#     """
#     Implementa el algoritmo de Warshall para determinar los nodos alcanzables desde un vértice de inicio en un grafo.
#     """
#     mapeo_nodos = {}
#     indice = 0
#     for nodo in grafo.obtenerVertices():
#         mapeo_nodos[nodo] = indice
#         indice += 1

#     n = len(grafo.obtenerVertices())
#     distancias = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

#     for nodo in grafo.obtenerVertices():
#         for vecino in grafo.obtenerVertice(nodo).obtenerConexiones():
#             i = mapeo_nodos[nodo]
#             j = mapeo_nodos[vecino.obtenerId()]
#             distancias[i][j] = 1  

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

#     nodos_alcanzables = []
#     indice_inicio = mapeo_nodos[inicio]
#     for i, distancia in enumerate(distancias[indice_inicio]):
#         if distancia != float('inf'):
#             nodos_alcanzables.append(list(mapeo_nodos.keys())[list(mapeo_nodos.values()).index(i)])

#     return nodos_alcanzables


# def warshall(grafo, inicio, fin):
#     # Implementa el algoritmo de Warshall para determinar si hay un camino entre dos vértices en un grafo.
#     mapeo_nodos = {}
#     indice = 0
#     for nodo in grafo.obtenerVertices():
#         mapeo_nodos[nodo] = indice
#         indice += 1

#     n = len(grafo.obtenerVertices())
#     distancias = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

#     for nodo in grafo.obtenerVertices():
#         for vecino in grafo.obtenerVertice(nodo).conexiones:
#             i = mapeo_nodos[nodo]
#             j = mapeo_nodos[vecino.Id]
#             distancias[i][j] = 1  

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

#     return distancias[mapeo_nodos[inicio]][mapeo_nodos[fin]] != float('inf')
