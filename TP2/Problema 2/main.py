# Esto lo hice porque no encontraba los modulos
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modulos')))



from Modulos.Temperaturas import Temperaturas_DB
base_datos = Temperaturas_DB()

# Guardar temperaturas
base_datos.guardar_temperatura(22.5, "15/10/2023")
base_datos.guardar_temperatura(25.0, "16/10/2023")
base_datos.guardar_temperatura(23.7, "18/10/2023")
base_datos.guardar_temperatura(19.8, "19/10/2023")
base_datos.guardar_temperatura(24.2, "20/10/2023")
base_datos.guardar_temperatura(18.3, "21/10/2023")
base_datos.guardar_temperatura(22.1, "22/10/2023")
base_datos.guardar_temperatura(26.5, "23/10/2023")
base_datos.guardar_temperatura(21.4, "24/10/2023")
base_datos.guardar_temperatura(20.5, "17/10/2023")

# Consultar temperaturas
print("Temperatura el 15/10/2023:", base_datos.devolver_temperatura("15/10/2023"))
print()

# Consultar temperaturas en un rango
print("Consultar temperaturas en un rango")
max_temp = base_datos.max_temp_rango("16/10/2023", "19/10/2023")
min_temp = base_datos.min_temp_rango("16/10/2023", "19/10/2023")
print("Máxima temperatura en el rango 16/10/2023 a 19/10/2023:", max_temp)
print("Mínima temperatura en el rango 16/10/2023 a 19/10/2023:", min_temp)
print()

# Consultar temperaturas extremas en un rango
print("Consultar temperaturas extremas en un rango")
min_temp, max_temp = base_datos.temp_extremos_rango("15/10/2023", "24/10/2023")
print("Mínima temperatura en el rango 15/10/2023 a 24/10/2023:", min_temp)
print("Máxima temperatura en el rango 15/10/2023 a 24/10/2023:", max_temp)
print()

# Consultar temperaturas en un rango
print("Consultar todas las temperaturas en el rango 14/10/2023 a 24/10/2023")
rango_temperaturas = base_datos.devolver_temperaturas("14/10/2023", "24/10/2023")
for temp in rango_temperaturas:
    print(temp)
print()

# Obtener la cantidad de muestras en la base de datos
print("Cantidad de muestras:", base_datos.cantidad_muestras())
print()

# Borrar una temperatura
print("Borro la temperatura del 16/10/2023")
base_datos.borrar_temperatura("16/10/2023")
print()

# Consultar temperaturas en un rango
print("Consulto todas las temperaturas en en todo el rango")
rango_temperaturas = base_datos.devolver_temperaturas("15/10/2023", "24/10/2023")
for temp in rango_temperaturas:
    print(temp)
print()

# Obtener la cantidad de muestras en la base de datos
print("Cantidad de muestras:", base_datos.cantidad_muestras())
