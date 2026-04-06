#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:43 2026

@author: giuliamaniotti
"""

from src.utils_ecg import detectar_picos_qrs


def calcular_promedio_senal(datos: dict) -> float:    
    
    """
    Qué hace la función:
    Calcula el promedio de los valores de la señal ECG.

    Parámetros:
    - datos: list o dict. Datos del participante.

    Retorna:
    - float. Promedio de la señal.
    """
    senal = datos["valor"]

    if len(senal) == 0:
        return 0

    return sum(senal) / len(senal)


def calcular_minimo_senal(datos: dict) -> float:
    """
    Qué hace la función:
    Calcula el valor mínimo de la señal ECG.

    Parámetros:
    - datos: list o dict. Datos del participante.

    Retorna:
    - float. Valor mínimo de la señal.
    """
    senal = datos["valor"]

    if len(senal) == 0:
        return 0

    return min(senal)


def calcular_maximo_senal(datos: dict) -> float:
    """
    Qué hace la función:
    Calcula el valor máximo de la señal ECG.

    Parámetros:
    - datos: list o dict. Datos del participante.

    Retorna:
    - float. Valor máximo de la señal.
    """
    senal = datos["valor"]

    if len(senal) == 0:
        return 0

    return max(senal)


def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Qué hace la función:
    Calcula la frecuencia cardíaca en latidos por minuto
    a partir de la lista de picos detectados.

    Parámetros:
    - picos: list. Lista de tiempos donde se detectaron picos.

    Retorna:
    - float. Frecuencia cardíaca en BPM.
    """
    if len(picos) < 2:
        return 0

    tiempo_total = picos[-1] - picos[0]

    if tiempo_total <= 0:
        return 0

    intervalos = len(picos) - 1
    frecuencia = (intervalos / tiempo_total) * 60

    return frecuencia


def calcular_fc_desde_datos(datos: dict) -> float:
    """
    Qué hace la función:
    Extrae los tiempos y la señal ECG de un participante,
    detecta los picos QRS y calcula la frecuencia cardíaca.

    Parámetros:
    - datos: list o dict. Datos del participante.

    Retorna:
    - float. Frecuencia cardíaca en BPM.
    """
    tiempos = datos["tiempo"]
    senal = datos["valor"]

    picos = detectar_picos_qrs(tiempos, senal)

    return calcular_frecuencia_cardiaca(picos)