from datetime import datetime
from arbolavl import ArbolAVL


class Temperaturas_DB:
    def __init__(self):
        # Crea una instancia de la clase ArbolAVL
        self.arbol_temperaturas = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol_temperaturas[fecha_obj] = temperatura

    def devolver_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        return self.arbol_temperaturas[fecha_obj]

    def max_temp_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        return self.arbol_temperaturas.maximo_rango(fecha1_obj, fecha2_obj)

    def min_temp_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        return self.arbol_temperaturas.minimo_rango(fecha1_obj, fecha2_obj)

    def temp_extremos_rango(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        max_temp = self.arbol_temperaturas.maximo_rango(fecha1_obj, fecha2_obj)
        min_temp = self.arbol_temperaturas.minimo_rango(fecha1_obj, fecha2_obj)
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        del self.arbol_temperaturas[fecha_obj]

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        rango_temperaturas = self.arbol_temperaturas.obtener_rango(fecha1_obj, fecha2_obj)
        
        rango_temperaturas.sort(key=lambda x: x[0])
        
        result = [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in rango_temperaturas]
        return result

    def cantidad_muestras(self):
        return len(self.arbol_temperaturas)

    for temp in rango_temperaturas:
        print(temp)

    # Obtener la cantidad de muestras en la base de datos
    print("Cantidad de muestras:", base_datos.cantidad_muestras())
