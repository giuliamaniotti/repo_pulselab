#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:37 2026

@author: giuliamaniotti
"""

def parsear_linea(linea: str) -> list:
    """
    Qué hace la función:
    Separa una línea del archivo CSV en campos, convierte cada valor
    al tipo de dato correspondiente y devuelve una lista con los datos parseados.

    Parámetros:
    - linea: str. Una línea del archivo de datos.

    Retorna:
    - list. Lista con los valores parseados en este orden:
      [id_participante, tiempo, valor, fase, condicion_experimental, hit]
    """
    partes = linea.strip().split(",")

    id_participante = int(partes[0])
    tiempo = float(partes[1])
    valor = float(partes[2])
    fase = partes[3]
    condicion_experimental = partes[4]
    hit = int(partes[5])

    return [id_participante, tiempo, valor, fase, condicion_experimental, hit]
