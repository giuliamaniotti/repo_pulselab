#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:17:09 2026

@author: giuliamaniotti
"""

def detectar_picos_qrs(tiempos: list, senal: list, umbral: float = 0.9, distancia_minima: float = 0.3) -> list:
    """
    Qué hace la función:
    Detecta picos en la señal ECG usando un umbral y una distancia mínima entre picos.

    Parámetros:
    - tiempos: list. Lista de tiempos.
    - senal: list. Lista de valores de la señal.
    - umbral: float. Valor mínimo para considerar un pico.
    - distancia_minima: float. Tiempo mínimo entre picos consecutivos.

    Retorna:
    - list: lista con los tiempos donde se detectaron picos.
    """
    picos = []

    if not isinstance(tiempos, list) or not isinstance(senal, list):
        return picos

    if len(tiempos) == 0 or len(senal) == 0:
        return picos

    if len(tiempos) != len(senal):
        return picos

    if distancia_minima < 0:
        return picos

    for i in range(1, len(senal) - 1):
        es_pico = senal[i] > umbral and senal[i] > senal[i - 1] and senal[i] > senal[i + 1]

        if es_pico:
            if len(picos) == 0:
                picos.append(tiempos[i])
            else:
                if tiempos[i] - picos[-1] >= distancia_minima:
                    picos.append(tiempos[i])

    return picos
