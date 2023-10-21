

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def __iter__(self):
      for i in self.listaMonticulo:
        yield i

    def __str__(self):
      return str(self.listaMonticulo)
    
    def __len__(self):
      return self.tamanoActual
    
    def ordenarMonticulo(self):
        for i in range(self.tamanoActual // 2, 0, -1):
            self.infiltAbajo(i)


    def infiltArriba(self,i): #infiltra un nuevo ítem hacia arriba en el árbol hasta donde sea necesario para mantener la propiedad de montículo.
     while i // 2 > 0:
      if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
         tmp = self.listaMonticulo[i // 2]
         self.listaMonticulo[i // 2] = self.listaMonticulo[i]
         self.listaMonticulo[i] = tmp
      i = i // 2
    
    def insertar(self,k):
     self.listaMonticulo.append(k)
     self.tamanoActual = self.tamanoActual + 1
     self.infiltArriba(self.tamanoActual)
    
    def infiltAbajo(self,i):
     while (i * 2) <= self.tamanoActual:
        hm = self.hijoMin(i)
        if self.listaMonticulo[i] > self.listaMonticulo[hm]:
            tmp = self.listaMonticulo[i]
            self.listaMonticulo[i] = self.listaMonticulo[hm]
            self.listaMonticulo[hm] = tmp
        i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
        return i * 2
      else:
        if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1
    
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)  # Aquí es donde se produce el problema

        return valorSacado   
    

    
    

    