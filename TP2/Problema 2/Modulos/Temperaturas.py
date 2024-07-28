from datetime import datetime
from ArbolBalanceado import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        self.arbol_temperaturas = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol_temperaturas[fecha_obj] = temperatura

    def devolver_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        return self.arbol_temperaturas[fecha_obj]
    
    def recorrer_rango(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        if fecha1 <= nodo.clave <= fecha2:
            resultados.append(nodo.cargaUtil)

        if fecha1 <= nodo.clave:
            self.recorrer_rango(nodo.hijoIzquierdo, fecha1, fecha2, resultados)

        if nodo.clave <= fecha2:
            self.recorrer_rango(nodo.hijoDerecho, fecha1, fecha2, resultados)
            
    def max_temp_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        resultados = []
        self.recorrer_rango(self.arbol_temperaturas.raiz, fecha1_obj, fecha2_obj, resultados)
        return max(resultados, default=None)

    def min_temp_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        resultados = []
        self.recorrer_rango(self.arbol_temperaturas.raiz, fecha1_obj, fecha2_obj, resultados)
        return min(resultados, default=None)


    def temp_extremos_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        max_temp = self.max_temp_rango(fecha1, fecha2)
        min_temp = self.min_temp_rango(fecha1, fecha2)
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        del self.arbol_temperaturas[fecha_obj]

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        rango_temperaturas = []
        self.recorrer_rango_fechas(self.arbol_temperaturas.raiz, fecha1_obj, fecha2_obj, rango_temperaturas)
        rango_temperaturas.sort(key=lambda x: x[0])
        result = [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in rango_temperaturas]
        return result

    def recorrer_rango_fechas(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return

        if fecha1 <= nodo.clave <= fecha2:
            resultados.append((nodo.clave, nodo.cargaUtil))

        if fecha1 <= nodo.clave:
            self.recorrer_rango_fechas(nodo.hijoIzquierdo, fecha1, fecha2, resultados)

        if nodo.clave <= fecha2:
            self.recorrer_rango_fechas(nodo.hijoDerecho, fecha1, fecha2, resultados)

    def cantidad_muestras(self):
        return len(self.arbol_temperaturas)









