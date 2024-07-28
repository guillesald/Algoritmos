class MonticuloBinarioMin():
    # Clase que representa un Montículo Binario Mínimo.
    # Esta clase es una modificación de la clase del ejercicio 1. Está adaptada para trabajar con vértices.

    def __init__(self):
        """
        Constructor de la clase MonticuloBinario.
        Inicializa un montículo binario con una lista.
        """
        self.listaMonticulo = (0, 0)
        self.tamanoActual = 0

    def __iter__(self):
        """
        Permite la iteración sobre los elementos del montículo.
        """
        for i in self.listaMonticulo:
            yield i

    def __str__(self):
        """
        Devuelve una representación en cadena del montículo.
        """
        return str(self.listaMonticulo)

    def __len__(self):
        """
        Devuelve el número de elementos en el montículo.
        """
        return self.tamanoActual

    def ordenarMonticulo(self):
        """
        Ordena el montículo para cumplir con la propiedad de montículo binario.
        """
        for i in range(self.tamanoActual // 2, 0, -1):
            self.infiltAbajo(i)

    def estaVacia(self):
        return self.tamanoActual == 0

    def insertar(self, k):
        """
        Inserta un nuevo elemento `k` en el montículo y lo ajusta para mantener la propiedad de montículo.
        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltArriba(self, i):
        """
        Infiltra un nuevo ítem hacia arriba en el árbol para mantener la propiedad de montículo.
        """
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
            

    def infiltAbajo(self, i):
        """
        Infiltra un elemento hacia abajo en el árbol para mantener la propiedad de montículo.
        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def eliminarMin(self):
        """
        Elimina y devuelve el elemento mínimo del montículo.
        """
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def hijoMin(self, p):
        """
        Devuelve el índice del hijo más pequeño del elemento en el índice `i`.
        """
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        else:
            if self.listaMonticulo[p * 2][0] < self.listaMonticulo[p * 2 + 1][0]:
                return p * 2
            else:
                return p * 2 + 1

    def decrementarClave(self, valor, nuevaClave):
        """
        Decrementa la clave de un valor específico en el montículo binario.
        Busca el valor en el montículo y actualiza su clave con el valor proporcionado.
        Luego, realiza las operaciones necesarias para mantener la propiedad del montículo.
        """
        for i, (clave, v) in enumerate(self.listaMonticulo[1:], start=1):
            if v == valor:
                self.listaMonticulo[i] = (nuevaClave, v)
                self.infiltArriba(i)

    def construirMonticulo(self, unaLista):
        """
        Construye un montículo binario a partir de una lista de valores.
        Crea un nuevo montículo binario utilizando los valores proporcionados en la lista.
        La lista debe contener pares de valores, donde el primer elemento del par representa la clave
        y el segundo elemento representa el valor del elemento en el montículo.
        """
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [(0, 0)]
        for dato in unaLista:
            self.listaMonticulo.append(dato)
        i = len(unaLista) // 2
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
