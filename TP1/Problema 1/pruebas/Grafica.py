from modulos.ListaDobleEnlazada import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt

lista_doble_enlazada = ListaDobleEnlazada()
lista = []
lista_de_tiempos = []

# Bloque para crear tiempos y guardarlos en un archivo
for l in range(1000):
    lista = random.sample(range(10000), l)
    lista_doble_enlazada = ListaDobleEnlazada()
    for k in range(len(lista)):
        lista_doble_enlazada.agregar_al_final(lista[k])
    tiempo_inicial = time.time()
    lista_doble_enlazada.ordenar()
    tiempo_final = time.time()
    lista_de_tiempos.append(tiempo_final - tiempo_inicial)
    del lista_doble_enlazada

with open("tiempos_para_alg_enlazada_de_0_a_1000_muestras.txt", "w") as archivo:
    for elemento in lista_de_tiempos:
        archivo.write(str(elemento) + "\n")

# Bloque para graficar los datos del archivo
def leer_archivo(nombre_archivo):
    lista_datos = []
    with open(nombre_archivo, 'r') as archivo:
        for i in range(1000):
            lista_datos.append(float(archivo.readline()))
    return lista_datos

x = list(range(1000))
y = leer_archivo("tiempos_para_alg_enlazada_de_0_a_1000_muestras.txt")
z = [i ** 1.9 / 5000000 for i in range(1000)]

# Plot
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y, label='Alg. Ordenamiento')
plt.xlabel('Muestras')
plt.ylabel('Tiempos')
plt.title('Tiempos para algoritmo de Ordenamiento')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y, color='blue', label='Alg. Ordenamiento')
plt.plot(x, z, color='red', label='x**2')
plt.xlabel('N muestras')
plt.ylabel('Tiempos')
plt.title('Tiempos y x**2')
plt.legend()

plt.tight_layout()
plt.show()
