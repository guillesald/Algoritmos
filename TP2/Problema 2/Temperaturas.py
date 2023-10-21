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
        result = [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in rango_temperaturas]
        return result

    def cantidad_muestras(self):
        return len(self.arbol_temperaturas)




miArbol = ArbolAVL()
miArbol[3]="rojo"
miArbol[4]="azul"
miArbol[6]="amarillo"
miArbol[2]="en"
del miArbol[6]
print(miArbol[6])
print(miArbol[2])
print('\n')



# Ejemplo de uso del programa
if __name__ == "__main__":
    base_datos = Temperaturas_DB()

    # Guardar temperaturas
    base_datos.guardar_temperatura(22.5, "15/10/2023")
    base_datos.guardar_temperatura(25.0, "16/10/2023")
    base_datos.guardar_temperatura(20.5, "17/10/2023")
    base_datos.guardar_temperatura(23.7, "18/10/2023")
    base_datos.guardar_temperatura(19.8, "19/10/2023")
    base_datos.guardar_temperatura(24.2, "20/10/2023")
    base_datos.guardar_temperatura(18.3, "21/10/2023")
    base_datos.guardar_temperatura(22.1, "22/10/2023")
    base_datos.guardar_temperatura(26.5, "23/10/2023")
    base_datos.guardar_temperatura(21.4, "24/10/2023")

    # Consultar temperaturas
    print("Temperatura el 15/10/2023:", base_datos.devolver_temperatura("15/10/2023"))

    # Consultar temperaturas en un rango
    max_temp = base_datos.max_temp_rango("16/10/2023", "19/10/2023")
    min_temp = base_datos.min_temp_rango("16/10/2023", "19/10/2023")
    print("Máxima temperatura en el rango:", max_temp)
    print("Mínima temperatura en el rango:", min_temp)

    # Consultar temperaturas extremas en un rango
    min_temp, max_temp = base_datos.temp_extremos_rango("15/10/2023", "24/10/2023")
    print("Mínima temperatura en el rango:", min_temp)
    print("Máxima temperatura en el rango:", max_temp)

    # Consultar temperaturas en un rango
    rango_temperaturas = base_datos.devolver_temperaturas("15/10/2023", "24/10/2023")
    for temp in rango_temperaturas:
        print(temp)

    # Obtener la cantidad de muestras en la base de datos
    print("Cantidad de muestras:", base_datos.cantidad_muestras())

    # Borrar una temperatura
    base_datos.borrar_temperatura("16/10/2023")

    # Consultar temperaturas en un rango
    rango_temperaturas = base_datos.devolver_temperaturas("15/10/2023", "24/10/2023")
    for temp in rango_temperaturas:
        print(temp)

    # Obtener la cantidad de muestras en la base de datos
    print("Cantidad de muestras:", base_datos.cantidad_muestras())