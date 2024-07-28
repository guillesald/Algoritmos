class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        # Constructor de la clase NodoArbol
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        # Verifica si el nodo tiene un hijo izquierdo
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        # Verifica si el nodo tiene un hijo derecho
        return self.hijoDerecho is not None

    def esHijoIzquierdo(self):
        # Verifica si el nodo es el hijo izquierdo de su padre
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        # Verifica si el nodo es el hijo derecho de su padre
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        # Verifica si el nodo es la raíz del árbol
        return not self.padre

    def esHoja(self):
        # Verifica si el nodo es una hoja (sin hijos)
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        # Verifica si el nodo tiene al menos un hijo
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        # Verifica si el nodo tiene ambos hijos
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        # Reemplaza los datos del nodo con nuevos valores
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


class ArbolBinarioBusqueda:

    def __init__(self):
        # Constructor de la clase ArbolBinarioBusqueda
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        # Obtiene el tamaño del árbol
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self, clave, valor):
        # Agrega un nuevo nodo al árbol
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        # Método privado para agregar un nodo de manera recursiva
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        # Permite agregar elementos utilizando notación de corchetes
        self.agregar(c, v)

    def obtener(self, clave):
        # Obtiene el valor asociado con una clave
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        # Método privado para obtener un nodo de manera recursiva
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __contains__(self, clave):
        # Verifica si una clave está en el árbol
        return self._obtener(clave, self.raiz) is not None

    def eliminar(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        self.eliminar(clave)

    def remover(self, nodoActual):
        if nodoActual.esHoja():
            # Nodo es hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():
            # Nodo tiene dos hijos
            sucesor = self.encontrarSucesor(nodoActual)
            self.empalmar(sucesor)
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
        else:
            # Nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                                     nodoActual.hijoIzquierdo.cargaUtil,
                                                     nodoActual.hijoIzquierdo.hijoIzquierdo,
                                                     nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                                     nodoActual.hijoDerecho.cargaUtil,
                                                     nodoActual.hijoDerecho.hijoIzquierdo,
                                                     nodoActual.hijoDerecho.hijoDerecho)

    def encontrarSucesor(self, nodo):
        # Encuentra el sucesor del nodo actual
        suc = None
        if nodo.tieneHijoDerecho():
            suc = self.encontrarMin(nodo.hijoDerecho)
        else:
            if nodo.padre:
                if nodo.esHijoIzquierdo():
                    suc = nodo.padre
                else:
                    nodo.padre.hijoDerecho = None
                    suc = self.encontrarSucesor(nodo.padre)
                    nodo.padre.hijoDerecho = nodo
        return suc
    
    def encontrarMin(self, nodo):
      #Encuentra el menor valor del subarbol izquierdo
      actual = nodo
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual
    
    def empalmar(self, nodo):
        # Empalma el nodo actual en el árbol
        if nodo.esHoja():
            if nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = None
            else:
                nodo.padre.hijoDerecho = None
        elif nodo.tieneAlgunHijo():
            if nodo.tieneHijoIzquierdo():
                if nodo.esHijoIzquierdo():
                    nodo.padre.hijoIzquierdo = nodo.hijoIzquierdo
                else:
                    nodo.padre.hijoDerecho = nodo.hijoIzquierdo
                nodo.hijoIzquierdo.padre = nodo.padre
            else:
                if nodo.esHijoIzquierdo():
                    nodo.padre.hijoIzquierdo = nodo.hijoDerecho
                else:
                    nodo.padre.hijoDerecho = nodo.hijoDerecho
                nodo.hijoDerecho.padre = nodo.padre
