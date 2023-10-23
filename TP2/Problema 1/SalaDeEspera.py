from Modulos.MonticuloBinario import MonticuloBinario
import time
import datetime
import Modulos.pacientes as pac
import random


cola_de_espera = MonticuloBinario()
n = 20  # cantidad de ciclos de simulación
orden_llegada = 1

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

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
    if random.random() < 0.5:  
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
    
    time.sleep(1)
