class Nodo:
    # Clase Nodo que define los nodos individuales de la lista
    def __init__(self, dato=None, siguiente=None, anterior=None):
        # Inicialización de un nodo con su respectivo dato y referencias al nodo anterior y siguiente.
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def obtenerDato(self):
        # Método para obtener el dato del nodo.
        return self.dato

    def obtenerSiguiente(self):
        # Método para obtener el nodo siguiente.
        return self.siguiente

    def asignarDato(self, nuevodato):
        # Método para asignar un nuevo dato al nodo.
        self.dato = nuevodato

    def asignarSiguiente(self, nuevosiguiente):
        # Método para asignar un nuevo nodo siguiente.
        self.siguiente = nuevosiguiente

    def __str__(self):
        # Método para la representación en cadena de un nodo.
        linea = str(self.dato)
        return linea


class ListaDobleEnlazada:
    # Clase ListaDobleEnlazada que define la estructura de la lista doblemente enlazada.
    def __init__(self):
        # Inicialización de la lista doblemente enlazada.
        self.cabeza = None  # Primer nodo de la lista
        self.cola = None    # Último nodo de la lista
        self.tamanio = 0    # Tamaño de la lista

    def __str__(self):
    # Método para la representación en cadena de la lista.
        linea="None "
        for i in self:
            linea=linea+str(i)+" "
        linea=linea+"None"
        return linea

    def __iter__(self):
    # Iterador para recorrer los elementos de la lista.
        actual=self.cabeza
        while actual is not None: 
            yield actual.dato
            actual=actual.siguiente
          
    def __len__(self):
    # Devuelve el tamaño de la lista.
        return self.tamanio
    
    def esta_vacia(self):
    # Verifica si la lista está vacía.
        return self.tamanio == 0
    
    def tamanio(self):
    # Devuelve el tamaño de la lista.
        return self.tamanio
    
    def agregar_al_inicio(self, dato):
    # Agrega un nuevo nodo al principio de la lista.
        nuevo = Nodo(dato, self.cabeza, None)
        if self.cabeza != None:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato):
    # Agrega un nuevo nodo al final de la lista.
        nuevo = Nodo(dato, None, self.cola)
        if self.cola != None:
            self.cola.siguiente = nuevo
        else:
            self.cabeza = nuevo
            
        self.cola = nuevo
        self.tamanio += 1

    def insertar(self,dato, posicion=None):
    # Inserta un nodo con el dato en una posición determinada.
        if posicion == None:
            self.agregar_al_final(dato)
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        elif 0<posicion<self.tamanio:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            nuevo = Nodo(dato, actual, actual.anterior)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
        else:
            self.agregar_al_final(dato)

    def extraer(self, posicion=None):
    # Elimina un nodo de la lista en una posición determinada.
        if self.tamanio == 0:
            raise ValueError("La lista está vacía")  # Generar una excepción si la lista está vacía

        if posicion is None or posicion == -1:
            nodo_extraido = self.cola
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None  # Si el nodo extraído es el único elemento en la lista
            self.tamanio -= 1
            return nodo_extraido.dato

        if posicion == 0:
            nodo_extraido = self.cabeza
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None  # Si el nodo extraído es el único elemento en la lista
            self.tamanio -= 1
            return nodo_extraido.dato

        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")  # Generar una excepción si la posición es inválida

        nodo_actual = self.cabeza
        for _ in range(posicion):
            nodo_actual = nodo_actual.siguiente

        nodo_extraido = nodo_actual
        nodo_actual.anterior.siguiente = nodo_actual.siguiente
        if nodo_actual.siguiente:
            nodo_actual.siguiente.anterior = nodo_actual.anterior
        else:
            self.cola = nodo_actual.anterior  # Actualizar la cola si se elimina el último elemento
        self.tamanio -= 1
        return nodo_extraido.dato

        
    def copiar(self):
    # Crea una copia de la lista doblemente enlazada.
        copia=ListaDobleEnlazada()
        actual=self.cabeza
        if actual == None:
            return copia
        while actual.siguiente != None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        copia.agregar_al_final(actual.dato)
        return copia
    
    def invertir(self):
        nodo_actual = self.cabeza
        auxiliar = None

        while nodo_actual is not None:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = auxiliar
            nodo_actual.anterior = siguiente_nodo

            auxiliar = nodo_actual
            nodo_actual = siguiente_nodo

        self.cola = self.cabeza
        self.cabeza = auxiliar


    def ordenar(self):
        if self.tamanio <= 1:
            # La lista ya está ordenada o es vacía, no es necesario ordenar.
            return

        actual = self.cabeza.siguiente  # Comenzar desde el segundo nodo.

        while actual:
            valor_actual = actual.dato
            nodo_anterior = actual.anterior

            while nodo_anterior and nodo_anterior.dato > valor_actual:
                nodo_anterior.siguiente.dato = nodo_anterior.dato
                nodo_anterior = nodo_anterior.anterior

            if nodo_anterior is None:
                self.cabeza.dato = valor_actual
            else:
                nodo_anterior.siguiente.dato = valor_actual

            actual = actual.siguiente



    def concatenar(self,Lista): 
        aux=Lista.cabeza
        while aux != None:
            self.agregar_al_final(aux.dato)
            aux=aux.siguiente


    def __add__(self, Lista): #SOBRECARGA EL +
        # Método para concatenar listas, devuelve una nueva lista sin modificar las originales
        nueva_lista = self.copiar()  # Hacer una copia de la lista actual

        aux = Lista.cabeza
        while aux is not None:
            nueva_lista.agregar_al_final(aux.dato)
            aux = aux.siguiente

        return nueva_lista

