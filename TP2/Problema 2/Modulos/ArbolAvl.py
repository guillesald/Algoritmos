from ArbolBinario import NodoArbol
from ArbolBinario import ArbolBinarioBusqueda



class ArbolAVL(ArbolBinarioBusqueda):
    def __init__(self):
        """
        Constructor de la clase ArbolAVL.
        Inicializa un árbol AVL como una extensión de un árbol binario de búsqueda.
        """
        super().__init__()

    def _agregar(self, clave, valor, nodo_actual):
        """
        Agrega un nuevo nodo con la clave y el valor especificados al árbol AVL y ajusta el equilibrio.
        """
        if clave < nodo_actual.clave:
            # Agrega a la izquierda y ajusta el equilibrio
            if nodo_actual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodo_actual.hijoIzquierdo)
            else:
                nodo_actual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodo_actual)
                self.actualizarEquilibrio(nodo_actual.hijoIzquierdo)
        else:
            # Agrega a la derecha y ajusta el equilibrio
            if nodo_actual.tieneHijoDerecho():
                self._agregar(clave, valor, nodo_actual.hijoDerecho)
            else:
                nodo_actual.hijoDerecho = NodoArbol(clave, valor, padre=nodo_actual)
                self.actualizarEquilibrio(nodo_actual.hijoDerecho)

    def actualizarEquilibrio(self, nodo):
        """
        Actualiza el factor de equilibrio del nodo y, si es necesario, rebalancea el árbol.
        """
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self, nodo):
        """
        Reequilibra el árbol si el factor de equilibrio de un nodo se sale de los límites.
        """
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def rotarIzquierda(self, rotRaiz):
        """
        Realiza una rotación hacia la izquierda en el árbol AVL.
        """
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo is not None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self, rotRaiz):
        """
        Realiza una rotación hacia la derecha en el árbol AVL.
        """
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)

    def maximo_rango(self, fecha1, fecha2):
        """
        Encuentra el valor máximo en un rango de claves (fechas) dado en el árbol AVL.
        """
        resultados = []
        fecha1_obj = fecha1
        fecha2_obj = fecha2
        self._maximo_rango(self.raiz, fecha1_obj, fecha2_obj, resultados)
        return max(resultados, default=None)

    def _maximo_rango(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        if fecha1 <= nodo.clave <= fecha2:
            resultados.append(nodo.cargaUtil)

        if fecha1 <= nodo.clave:
            self._maximo_rango(nodo.hijoIzquierdo, fecha1, fecha2, resultados)

        if nodo.clave <= fecha2:
            self._maximo_rango(nodo.hijoDerecho, fecha1, fecha2, resultados)

    def minimo_rango(self, fecha1, fecha2):
        """
        Encuentra el valor mínimo en un rango de claves (fechas) dado en el árbol AVL.
        """
        resultados = []
        fecha1_obj = fecha1
        fecha2_obj = fecha2
        self._minimo_rango(self.raiz, fecha1_obj, fecha2_obj, resultados)
        return min(resultados, default=None)

    def _minimo_rango(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        if fecha1 <= nodo.clave <= fecha2:
            resultados.append(nodo.cargaUtil)

        if fecha1 <= nodo.clave:
            self._minimo_rango(nodo.hijoIzquierdo, fecha1, fecha2, resultados)

        if nodo.clave <= fecha2:
            self._minimo_rango(nodo.hijoDerecho, fecha1, fecha2, resultados)

    def obtener_rango(self, fecha1, fecha2):
        """
        Obtiene todos los elementos en un rango de claves (fechas) dado en el árbol AVL.
        """
        rango_temperaturas = []
        fecha1_obj = fecha1
        fecha2_obj = fecha2
        self._obtener_rango(self.raiz, fecha1_obj, fecha2_obj, rango_temperaturas)
        return rango_temperaturas

    def _obtener_rango(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        if fecha1 <= nodo.clave <= fecha2:
            resultados.append((nodo.clave, nodo.cargaUtil))

        if fecha1 <= nodo.clave:
            self._obtener_rango(nodo.hijoIzquierdo, fecha1, fecha2, resultados)

        if nodo.clave <= fecha2:
            self._obtener_rango(nodo.hijoDerecho, fecha1, fecha2, resultados)