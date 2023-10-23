from datetime import datetime
from ArbolAvl import ArbolAVL


class Temperaturas_DB:
    def __init__(self):
        # Crea una instancia de la clase ArbolAVL para almacenar temperaturas
        self.arbol_temperaturas = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha):
        # Convierte la fecha en un objeto datetime
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        
        # Almacena la temperatura en el árbol AVL usando la fecha como clave
        self.arbol_temperaturas[fecha_obj] = temperatura

    def devolver_temperatura(self, fecha):
        # Convierte la fecha en un objeto datetime
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        
        # Obtiene la temperatura correspondiente a la fecha proporcionada
        return self.arbol_temperaturas[fecha_obj]

    def max_temp_rango(self, fecha1, fecha2):
        # Convierte las fechas en objetos datetime
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        
        # Obtiene la temperatura máxima en el rango de fechas proporcionado
        return self.arbol_temperaturas.maximo_rango(fecha1_obj, fecha2_obj)

    def min_temp_rango(self, fecha1, fecha2):
        # Convierte las fechas en objetos datetime
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        
        # Obtiene la temperatura mínima en el rango de fechas proporcionado
        return self.arbol_temperaturas.minimo_rango(fecha1_obj, fecha2_obj)

    def temp_extremos_rango(self, fecha1, fecha2):
        # Convierte las fechas en objetos datetime
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        
        # Obtiene tanto la temperatura máxima como la mínima en el rango de fechas proporcionado
        max_temp = self.arbol_temperaturas.maximo_rango(fecha1_obj, fecha2_obj)
        min_temp = self.arbol_temperaturas.minimo_rango(fecha1_obj, fecha2_obj)
        
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        # Convierte la fecha en un objeto datetime y elimina la temperatura asociada
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        del self.arbol_temperaturas[fecha_obj]

    def devolver_temperaturas(self, fecha1, fecha2):
        # Convierte las fechas en objetos datetime
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        
        # Obtiene todas las temperaturas en el rango de fechas proporcionado
        rango_temperaturas = self.arbol_temperaturas.obtener_rango(fecha1_obj, fecha2_obj)
        
        # Ordena las temperaturas por fecha y las formatea para mostrarlas
        rango_temperaturas.sort(key=lambda x: x[0])
        result = [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in rango_temperaturas]
        
        return result

    def cantidad_muestras(self):
        # Obtiene la cantidad de muestras almacenadas en el árbol
        return len(self.arbol_temperaturas)








