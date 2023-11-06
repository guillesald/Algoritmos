
import random
import os
import math

def generar_numeros_aleatorios(nombre_archivo, cant_megas):
   
    tamano_deseado = cant_megas * 1024 * 1024  # 101 MB en bytes
    tamano_actual = 0
    with open(nombre_archivo, 'w') as f:
        while tamano_actual < tamano_deseado:
            numero = random.randint(10**39, 10**40 - 1)  # Número aleatorio de 40 cifras (lo uso para probar un archivo de 10MB)
            #numero = random.randint(10**159, 10**160 - 1)  # Número aleatorio de 160 cifras (lo uso para probar un archivo de 100MB)
            f.write(str(numero) + '\n')  # Escribir el número en el archivo
            tamano_actual = os.stat(nombre_archivo).st_size  # Obtener el tamaño actual del archivo

def contar_lineas_archivo(archivo):

    contador = 0
    with open(archivo, 'r') as f:
        for linea in f:
            contador += 1
    return contador

def dividir_archivo(archivo_entrada, archivo_salida1, archivo_salida2, cant_datos):

    with open(archivo_entrada, 'r') as entrada, \
         open(archivo_salida1, 'w') as salida1, \
         open(archivo_salida2, 'w') as salida2:
        for i in range(cant_datos):
            linea = entrada.readline()
            if not linea:
                break  
            if (linea.strip()):
                salida1.write(linea)
       
        destino = salida2
        contador_lineas = 0
        for linea in entrada:
            if (linea.strip()):
                destino.write(linea)
            contador_lineas += 1
            if contador_lineas == cant_datos:
                destino = salida1 if destino == salida2 else salida2
                contador_lineas = 0



def unir_archivo(archivo_entrada_1, archivo_entrada_2, archivo_salida, cant_datos):
    # Se abren los archivos de entrada y salida
    with open(archivo_entrada_1, 'r') as archivo_entrada1, \
        open(archivo_entrada_2, 'r') as archivo_entrada2, \
        open(archivo_salida, 'w') as archivo_salida:
        
        # Inicialización de variables para controlar las líneas y datos restantes
        datos_restantes_entrada1 = cant_datos - 1
        datos_restantes_entrada2 = cant_datos - 1
        
        # Lectura de la primera línea de cada archivo
        entrada1 = archivo_entrada1.readline()
        entrada2 = archivo_entrada2.readline()
        
        # Se verifica si las líneas leídas son enteros válidos y se convierten a entero si es así
        if(entrada1 != ''):
            entrada1 = int(entrada1)
        if (entrada2 != ''):
            entrada2 = int(entrada2)
        
        # Proceso para fusionar los archivos en el archivo de salida
        while(entrada1 != '' or entrada2 != ''):
            # Se verifica si se han llegado al final de ambos archivos
            if((entrada1 == '\n' or entrada1 == '' or entrada1 == '\r\n') and (entrada2 == '\n' or entrada2 == '' or entrada2 == '\r\n')):
                break
            # Se compara el valor de las líneas y se escribe en el archivo de salida
            elif (entrada1 != '' and entrada2 != '' and entrada1 != '\n' and entrada2 != '\n'):
                if (entrada1 <= entrada2 and datos_restantes_entrada1 >= 0 and datos_restantes_entrada2 >= 0):
                    archivo_salida.write(str(entrada1) + '\n')
                    datos_restantes_entrada1 -= 1
                    # Se lee la siguiente línea del archivo y se convierte a entero si es un número válido
                    if (datos_restantes_entrada1 >= 0):
                        entrada1 = archivo_entrada1.readline()
                        if(entrada1.split()):
                            entrada1 = int(entrada1)
                    elif (datos_restantes_entrada1 == -1):
                        entrada1 = ''
                elif (entrada2 < entrada1 and datos_restantes_entrada1 >= 0 and datos_restantes_entrada2 >= 0):
                    archivo_salida.write(str(entrada2) + '\n')
                    datos_restantes_entrada2 -= 1
                    # Se lee la siguiente línea del archivo y se convierte a entero si es un número válido
                    if (datos_restantes_entrada2 >= 0):
                        entrada2 = archivo_entrada2.readline()
                        if (entrada2.split()):
                            entrada2 = int(entrada2)
                    elif (datos_restantes_entrada2 == -1):
                        entrada2 = ''
            # Se procesan casos donde hay líneas vacías o finales de archivo
            # para asegurar que no haya datos inválidos o líneas vacías
            elif (datos_restantes_entrada1 == -1 and datos_restantes_entrada2 >= 0 and entrada2 != '' and entrada2 != '\n' and entrada2 != '\r\n'):
                while datos_restantes_entrada2 >= 0:
                    if (entrada2 != ''):
                        archivo_salida.write(str(entrada2) + '\n')
                    datos_restantes_entrada2 -= 1
                    if (datos_restantes_entrada2 >= 0):
                        entrada2 = archivo_entrada2.readline()
                        if (entrada2.split()):
                            entrada2 = int(entrada2)
            elif (datos_restantes_entrada2 == -1 and datos_restantes_entrada1 >= 0 and entrada1 != '' and entrada1 != '\n' and entrada1 != '\r\n'):
                while datos_restantes_entrada1 >= 0:
                    if (entrada1 != ''):
                        archivo_salida.write(str(entrada1) + '\n')
                    datos_restantes_entrada1 -= 1
                    if (datos_restantes_entrada1 >= 0):
                        entrada1 = archivo_entrada1.readline()
                        if (entrada1.split()):
                            entrada1 = int(entrada1)
            elif (datos_restantes_entrada1 == -1 and datos_restantes_entrada2 == -1):
                # Se reinician los contadores cuando se llega al final de ambos archivos
                datos_restantes_entrada1 = cant_datos - 1
                datos_restantes_entrada2 = cant_datos - 1
                entrada1 = archivo_entrada1.readline()
                if (entrada1.split()):
                    entrada1 = int(entrada1)
                entrada2 = archivo_entrada2.readline()
                if (entrada2.split()):
                    entrada2 = int(entrada2)
            # Se manejan los casos de líneas vacías o finales de archivo
            elif ((entrada1 == '' or entrada1 == '\n') and (entrada2 != '' and entrada2 != '\n')):
                archivo_salida.write(str(entrada2) + '\n')
                entrada2 = archivo_entrada2.readline()
                if (entrada2.split()):
                    entrada2 = int(entrada2)
            elif ((entrada2 == '' or entrada2 == '\n') and (entrada1 != '' and entrada1 != '\n')):
                archivo_salida.write(str(entrada1) + '\n')
                entrada1 = archivo_entrada1.readline()
                if (entrada1.split()):
                    entrada1 = int(entrada1)



def ordenamiento_inicial(archivo_entrada, archivo_salida1, archivo_salida2, cant_datos):
    # Se abren los archivos de entrada y salida
    with open(archivo_entrada, 'r') as entrada, \
         open(archivo_salida1, 'w') as salida1, \
         open(archivo_salida2, 'w') as salida2:
        
        # Listas para almacenar líneas ordenadas
        linea_salida1 = []
        linea_salida2 = []
        
        # Se leen las primeras líneas del archivo de entrada y se almacenan en la lista correspondiente
        for i in range(cant_datos):
            linea = entrada.readline()
            if not linea:
                break
            if (linea.strip()):
                linea_salida1.append(linea)
                
        # Se ordenan las líneas almacenadas en la lista de salida 1
        linea_salida1.sort()
        for k in range(len(linea_salida1)):
            salida1.write(linea_salida1[k])
        
        # Limpieza de la lista de salida 1
        linea_salida1 = []
        
        # Selección del destino de salida (inicialmente la lista de salida 2)
        destino = linea_salida2
        contador_lineas = 0
        
        # Se procesa cada línea del archivo de entrada
        for linea in entrada:
            if (linea.strip()):
                destino.append(linea)
            contador_lineas += 1
            
            # Cuando se llena el número de líneas para un destino, se ordena y se escribe en el archivo correspondiente
            if contador_lineas == cant_datos:
                destino.sort()
                for k in range(len(destino)):
                    if destino == linea_salida1:
                        salida1.write(destino[k])
                    elif destino == linea_salida2:
                        salida2.write(destino[k])
                
                # Cambio entre listas de salida y limpieza de listas
                if destino == linea_salida1:
                    linea_salida1 = []
                    destino = linea_salida2
                elif destino == linea_salida2:
                    linea_salida2 = []
                    destino = linea_salida1
                contador_lineas = 0
        
        # Escritura de las líneas restantes en los archivos de salida
        for dato in linea_salida1:
            salida1.write(dato)
        for dato in linea_salida2:
            salida2.write(dato)




def ordenar(archivo):
   
    cantidad_datos=contar_lineas_archivo(archivo)
    ordenamiento_inicial(archivo, "salida1.txt", "salida2.txt", 10)
    unir_archivo("salida1.txt", "salida2.txt", archivo, 10)
    for ronda in range(int(math.log2(cantidad_datos/10)+1)):
        dividir_archivo(archivo, "salida1.txt", "salida2.txt", int(math.pow(2, ronda)*10))
        unir_archivo("salida1.txt", "salida2.txt", archivo, int(math.pow(2, ronda)*10))
