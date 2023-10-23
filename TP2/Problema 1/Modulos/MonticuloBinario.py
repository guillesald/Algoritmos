class MonticuloBinario:
    def __init__(self):
        """
        Constructor de la clase MonticuloBinario.
        Inicializa un montículo binario con una lista de un solo elemento.
        """
        self.listaMonticulo = [0]
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

    def infiltArriba(self, i):
        """
        Infiltra un nuevo ítem hacia arriba en el árbol para mantener la propiedad de montículo.
        """
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def insertar(self, k):
        """
        Inserta un nuevo elemento `k` en el montículo y lo ajusta para mantener la propiedad de montículo.
        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
    
    def infiltAbajo(self, i):
        """
        Infiltra un elemento hacia abajo en el árbol para mantener la propiedad de montículo.
        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self, i):
        """
        Devuelve el índice del hijo más pequeño del elemento en el índice `i`.
        """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
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


    
    

    