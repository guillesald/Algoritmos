from Vertice import Vertice

class Grafo:
    # Representa un grafo mediante un diccionario, donde las etiquetas de los vértices son las claves y los objetos vértices son los valores.
    def __init__(self):
        # Inicializa un objeto Grafo.
        self._listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        # Añade un nuevo vértice al grafo y devuelve el objeto vértice creado.
        nuevoVertice = None
        if clave not in self.obtenerVertices():
            self.numVertices += 1
            nuevoVertice = Vertice(clave)
            self._listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, clave):
        # Recupera el objeto vértice correspondiente a una clave específica.
        if clave in self._listaVertices:
            return self._listaVertices[clave]
        else:
            return None

    def __contains__(self, clave):
        # Comprueba la presencia de un vértice en el grafo.
        return clave in self._listaVertices

    def agregarArista(self, origen, destino, costo=0):
        # Establece una conexión (arista) entre dos vértices en el grafo. Si los vértices no existen, se crean automáticamente.
        if origen not in self._listaVertices:
            nv = self.agregarVertice(origen)
        if destino not in self._listaVertices:
            nv = self.agregarVertice(destino)
        self._listaVertices[origen].agregarVecino(self._listaVertices[destino], int(costo))

    def obtenerVertices(self):
        # Obtiene una lista con las claves de todos los vértices en el grafo.
        return list(self._listaVertices.keys())

    def __iter__(self):
        # Devuelve un iterador que permite recorrer los objetos vértice del grafo.
        return iter(self._listaVertices.values())

    def decrementarClave(self, valor, nuevaClave):
        # Disminuye la clave de un valor específico en el montículo binario y ajusta el montículo según sea necesario.
        for i, (clave, v) in enumerate(self.listaMonticulo[1:], start=1):
            if v == valor:
                self.listaMonticulo[i] = (nuevaClave, v)
                self.infiltArriba(i)
                return
