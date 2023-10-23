class Vertice:
    def __init__(self, clave):
        # Constructor de la clase Vertice
        self._id = clave
        self._conectadoA = {}
        self._distancia = float('inf')
        self._predecesor = None
        self._max_cuello = 0
        self.estado = "no visitado"

    def agregarVecino(self, vecino, ponderacion=0):
        # Agrega un vértice vecino y su ponderación al vértice actual
        self._conectadoA[vecino] = ponderacion

    def __str__(self):
        # Devuelve una representación en forma de cadena del vértice
        return str(self._id) + ' conectadoA: ' + str([x._id for x in self._conectadoA])

    @property
    def conexiones(self):
        # Devuelve los vértices vecinos del vértice actual
        return self._conectadoA.keys()

    @property
    def Id(self):
        # Devuelve el identificador del vértice
        return self._id

    @property
    def distancia(self):
        # Devuelve la distancia del vértice
        return self._distancia

    def ponderacion(self, vecino):
        # Devuelve la ponderación de la conexión entre el vértice actual y el vértice vecino
        return self._conectadoA[vecino]

    def setDistancia(self, valor):
        # Establece la distancia del vértice
        self._distancia = valor

    @property
    def predecesor(self):
        # Devuelve el predecesor del vértice
        return self._predecesor

    @predecesor.setter
    def predecesor(self, predecesor):
        # Establece el predecesor del vértice
        self._predecesor = predecesor

    def asignarDistancia(self, dist):
        # Asigna una distancia al vértice
        self._distancia = dist

    def obtenerDistancia(self):
        # Devuelve la distancia del vértice
        return self._distancia

    def obtenerConexiones(self):
        # Devuelve los vértices vecinos del vértice actual
        return self._conectadoA.keys()

    def obtenerPonderacion(self, vecino):
        # Devuelve la ponderación de la conexión entre el vértice actual y el vértice vecino
        return self._conectadoA[vecino]

    def asignarPredecesor(self, predecesor):
        # Asigna un predecesor al vértice
        self._predecesor = predecesor
