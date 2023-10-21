# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n - 1)]
        self.__apellido = apellidos[randint(0, n - 1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo - 1]
        self.__orden_de_llegada = 0  # Nuevo atributo para el orden de llegada

    def __lt__(self, other):
        #Para mantener el orden por riesgo y orden de llegada
        if self.__riesgo==other.__riesgo:
            return (self.__orden_de_llegada < other.__orden_de_llegada)
        return (
            self.__riesgo < other.__riesgo
        )

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo

    def get_descripcion_riesgo(self):
        return self.__descripcion

    def get_orden_de_llegada(self):  # Nuevo método para obtener el orden de llegada
        return self.__orden_de_llegada

    def set_orden_de_llegada(self, orden):  # Nuevo método para establecer el orden de llegada
        self.__orden_de_llegada = orden

    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad

        
        
        
        