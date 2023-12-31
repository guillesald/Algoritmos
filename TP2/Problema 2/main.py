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
