from Modulos.MonticuloBinario import MonticuloBinario
import time
import Modulos.pacientes as pac
import random


cola_de_espera = MonticuloBinario()
n = 150  # cantidad de ciclos de simulación
orden_llegada = 1

# Ciclo que gestiona la simulación
for i in range(n):
    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    paciente.set_orden_de_llegada(orden_llegada)
    cola_de_espera.insertar(paciente)  # Agregar el paciente al montículo binario
    orden_llegada += 1

    print('*'*40)
    print('Llega el paciente:', paciente)
    print('*'*40)

    
    # Atención de paciente en este ciclo
    if random.random() < 0.3:  
        paciente_atendido = cola_de_espera.eliminarMin()  # Obtener el paciente con el riesgo más alto

        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido, ' Con orden de llegada:', paciente_atendido.get_orden_de_llegada())
        print('*'*40)
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))  
    for i, paciente in enumerate(cola_de_espera.listaMonticulo):
        if i == 0:
           continue  # Saltar el primer elemento, que es un marcador cero
        orden_de_llegada = paciente.get_orden_de_llegada()
        print('\t', paciente, ' Con orden de llegada:', orden_de_llegada)
    print('-*-'*15)
    




#FORMA DE MOSTRAR LA LISTA ORDENADA


# from Modulos.MonticuloBinario import MonticuloBinario
# import time
# import datetime
# import Modulos.pacientes as pac
# import random

# cola_de_espera = MonticuloBinario()
# n = 20  # cantidad de ciclos de simulación
# orden_llegada = 1

# # Ciclo que gestiona la simulación
#     # Se crea un paciente un paciente por segundo
#     paciente = pac.Paciente()
#     paciente.set_orden_de_llegada(orden_llegada)
#     cola_de_espera.insertar(paciente)  # Agregar el paciente al montículo binario
#     orden_llegada += 1

#     print('*'*40)
#     print('Llega el paciente:', paciente)
#     print('*'*40)

#     # Atención de paciente en este ciclo
#     if random.random() < 0.5:
#         paciente_atendido = cola_de_espera.eliminarMin()  # Obtener el paciente con el riesgo más alto

#         print('*'*40)
#         print('Se atiende el paciente:', paciente_atendido, ' Con orden de llegada:', paciente_atendido.get_orden_de_llegada())
#         print('*'*40)

#     print()

#     # Se muestran los pacientes restantes en la cola de espera
#     pacientes_en_espera = cola_de_espera.listaMonticulo[1:]  # Copiar la lista, excluyendo el primer elemento (0)
#     pacientes_ordenados = sorted(pacientes_en_espera)  # Ordenar los pacientes

#     print('Pacientes que faltan atenderse:', len(cola_de_espera))
#     for paciente in pacientes_ordenados:
#         orden_de_llegada = paciente.get_orden_de_llegada()
#         print('\t', paciente, ' Con orden de llegada:', orden_de_llegada)
#     print('-*-'*15)

#     time.sleep(1)
