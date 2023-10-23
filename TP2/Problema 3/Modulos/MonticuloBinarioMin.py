class MonticuloBinarioMin():
    # Clase que representa un Montículo Binario Mínimo.
    # Esta clase es una modificación de la clase del ejercicio 1. Está adaptada para trabajar con vértices.

    def __init__(self):
        # Constructor de la clase MonticuloBinario.
        # Inicializa la lista de elementos, el tamaño actual del montículo y agrega
        # un elemento mínimo absoluto especificado.
        self.listaMonticulo = (0, 0)
        self.tamanoActual = 0

    def estaVacia(self):
        return self.tamanoActual == 0

    def insertar(self, k):
        # Inserta un nuevo elemento `k` en el montículo binario mínimo. El elemento se agrega
        # al final de la lista `listaMonticulo` y luego se realiza el proceso de "infiltración hacia arriba"
        # para mantener la propiedad de orden del montículo.
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltArriba(self, i):
        # Realiza el proceso de "infiltración hacia arriba" en el montículo. Este proceso se utiliza para mantener
        # la propiedad de orden del montículo binario mínimo después de insertar un elemento en la posición `i`.
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def infiltAbajo(self, i):
        # Realiza el proceso de "infiltración hacia abajo" en el montículo. Este proceso se utiliza para mantener
        # la propiedad de orden del montículo binario mínimo después de eliminar el elemento en la posición `i`.
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def eliminarMin(self):
        # Elimina y devuelve el elemento mínimo (raíz) del montículo binario mínimo.
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def hijoMin(self, p):
        # Obtiene el índice del hijo más pequeño de un nodo en el montículo binario mínimo. Compara los valores
        # de los hijos izquierdo (`i * 2`) y derecho (`i * 2 + 1`) del nodo en la posición `i` y devuelve el índice
        # del hijo con el valor más pequeño.
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        else:
            if self.listaMonticulo[p * 2][0] < self.listaMonticulo[p * 2 + 1][0]:
                return p * 2
            else:
                return p * 2 + 1

    def decrementarClave(self, valor, nuevaClave):
        # Decrementa la clave de un valor específico en el montículo binario.
        # Busca el valor en el montículo y actualiza su clave con el valor proporcionado.
        # Luego, realiza las operaciones necesarias para mantener la propiedad del montículo.
        for i, (clave, v) in enumerate(self.listaMonticulo[1:], start=1):
            if v == valor:
                self.listaMonticulo[i] = (nuevaClave, v)
                self.infiltArriba(i)

    def construirMonticulo(self, unaLista):
        # Construye un montículo binario a partir de una lista de valores.
        # Crea un nuevo montículo binario utilizando los valores proporcionados en la lista.
        # La lista debe contener pares de valores, donde el primer elemento del par representa la clave
        # y el segundo elemento representa el valor del elemento en el montículo.
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [(0, 0)]
        for dato in unaLista:
            self.listaMonticulo.append(dato)
        i = len(unaLista) // 2
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def __str__(self):
        linea = ''
        for i in range(self.tamanoActual):
            linea += self.listaMonticulo[i + 1].get_nombre() + self.listaMonticulo[i + 1].get_apellido() + self.listaMonticulo[i + 1].get_descripcion_riesgo() + str(self.listaMonticulo[i + 1].get_orden()) + '\n'
        return linea

    def __len__(self):
        return self.tamanoActual

    def __iter__(self):
        return iter(self.listaMonticulo[1:])
