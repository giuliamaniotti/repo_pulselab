def parsear_linea(linea: str) -> list:
    """
    Procesa una línea de texto del archivo de datos, separando sus componentes 
    y convirtiéndolos a los tipos de datos adecuados.

    Esta función toma una cadena de caracteres que representa una fila del 
    registro (id_participante, tiempo, valor, fase, condicion_experimental, hit) 
    y realiza la conversión técnica necesaria para su procesamiento posterior.

    Args:
        linea (str): Una cadena de texto con los campos separados por comas.

    Returns:
        list: Una lista con los valores convertidos:
            - id_participante (int)
            - tiempo (float)
            - valor (float)
            - fase (str)
            - condicion_experimental (str)
            - hit (int)
    """
    partes = linea.strip().split(",")

    id_participante = int(partes[0])
    tiempo = float(partes[1])
    valor = float(partes[2])
    fase = partes[3]
    condicion_experimental = partes[4]
    hit = int(partes[5])

    return [
        id_participante,
        tiempo,
        valor,
        fase,
        condicion_experimental,
        hit
    ]


def cargar_datos(ruta) -> list:
    """
    Carga y estructura los datos fisiológicos y conductuales desde un archivo 
    de texto siguiendo el modelo de datos del proyecto PulseLab.

    La función se encarga de abrir el archivo, recorrer cada línea aplicando 
    el parseo correspondiente y agrupar la información por participante en 
    un formato de diccionario.

    parametros:
        ruta (str): La ruta local del archivo que contiene los registros.

    returns:
        list: Una lista de diccionarios (registros de participantes). Cada 
        diccionario contiene las siguientes claves:
            - "id_participante": int
            - "tiempo": lista de floats
            - "valor": lista de floats (señal ECG)
            - "fase": lista de strings ("baseline" o "tarea")
            - "condicion_experimental": lista de strings
            - "hit": lista de ints (eventos conductuales)
    """

    participantes = {}

    with open(ruta, "r") as archivo:
        next(archivo)

        for linea in archivo:
            datos = parsear_linea(linea)
            id_p = datos[0]

            if id_p not in participantes:
                participantes[id_p] = {
                    "id_participante": id_p,
                    "tiempo": [],
                    "valor": [],
                    "fase": [],
                    "condicion_experimental": [],
                    "hit": []
                }

            participantes[id_p]["tiempo"].append(datos[1])
            participantes[id_p]["valor"].append(datos[2])
            participantes[id_p]["fase"].append(datos[3])
            participantes[id_p]["condicion_experimental"].append(datos[4])
            participantes[id_p]["hit"].append(datos[5])

    return list(participantes.values())#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:37 2026

@author: giuliamaniotti
"""
